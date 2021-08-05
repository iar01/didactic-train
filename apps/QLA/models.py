from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from location_field.models.plain import PlainLocationField


class Subject(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

    def class_name(self):
        return self.__class__.__name__


# Dataset taken from https://gist.github.com/tadast/8827699
class Country(models.Model):
    name = models.CharField(max_length=200, null=False)
    code_alpha2 = models.CharField(max_length=2, null=False, default="")
    code_alpha3 = models.CharField(max_length=3, null=False, default="")
    numeric_code = models.IntegerField(default=0, null=True)
    Location = models.CharField(max_length=255, null=True)
    city = PlainLocationField(based_fields=['Location'], zoom=7, null=True)

    def __str__(self):
        return self.name

    def class_name(self):
        return self.__class__.__name__


class StudentYearGrade(models.Model):
    # name of the year/grade  eg Year 7  or Grade 6
    name = models.CharField(max_length=100)

    # different countries have varying names Year 1, Grade 5 etc
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True)

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.name


# Level such as GCSE, A-level, BTec, IB etc
class Level(models.Model):
    # the name of the Level eg "GCSE"
    name = models.CharField(max_length=255, null=True)

    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True)

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.name


class School(models.Model):
    # school name
    name = models.CharField(max_length=255, null=False, unique=True)
    urn = models.CharField(max_length=255, null=True, blank=True)

    # ISO 3 char country code
    # TODO this should use the country table model as foriegnkey
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)  # models.CharField(max_length=3, null=False)

    # website url for the school
    url = models.CharField(max_length=255, null=True)

    # logo for the school
    school_logo = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)

    # the school already have users with an account in the system
    is_active = models.BooleanField(default=False, null=False)

    # this value is set to False when a user registers and their school is not in the drop down list and they add it
    # as a new school. QLA admin staff will then check it is a proper school and will manually set to True.
    is_validated = models.BooleanField(default=True, null=False)

    # This will be used to determine the subscription plan for the school. We will offer on a per subject basis
    subjects = models.ManyToManyField(Subject, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.pk, self.name)

    def class_name(self):
        return self.__class__.__name__


class Teacher(models.Model):
    # the name of the teacher
    name = models.CharField(max_length=255, null=False)
    school = models.ForeignKey(School, on_delete=models.SET_DEFAULT,
                               default=1)  # this is so it easier to filter teachers based on school and not via the users profile object

    subjects = models.ManyToManyField(Subject)

    # TODO need to figure out how to get as a string the subjects currently self.subjects
    ## evaluates to qla.Subject.None
    def __str__(self):
        outst = ''
        for s in self.subjects.all():
            outst += ' ' + s.name

        return "{} - {} - {}".format(self.name, self.school.pk, outst)

    def class_name(self):
        return self.__class__.__name__


class Student(models.Model):
    class Meta:
        ordering = ['year_grade', 'firstname']

    # firstname of the student
    firstname = models.CharField(max_length=255, null=False)

    # surname of the student
    surname = models.CharField(max_length=255, null=False)

    # school the student belongs to
    school = models.ForeignKey(School, on_delete=models.SET_DEFAULT, default=1)

    # reference number of student the school's interal reference ID for the student
    student_ref_number = models.CharField(max_length=255, null=False)

    # to differenicate between students with exact same name
    dob = models.DateField()

    # yeargroup
    # TODO system needs to have an option where this value will be autocalculated based on DOB
    year_grade = models.ForeignKey(StudentYearGrade, on_delete=models.DO_NOTHING, null=True, blank=True)

    # TODO
    # target grade for subject

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return "{} {} - ({}) - {}".format(self.firstname, self.surname, self.student_ref_number, self.year_grade)


class Class(models.Model):
    name = models.CharField(max_length=255, null=False)
    # M:1 relationship. Each class can only have 1 school
    school = models.ForeignKey(School, on_delete=models.SET_DEFAULT, default=1)

    subject = models.ForeignKey(Subject, on_delete=models.SET_DEFAULT, default=1)

    # class name

    # StudentYearGrade for the Class. This is so that its value automatically updates with time. Eg in July 2021 Class is Year 10, in September 2021 Class is Year 11 for new academic year
    year_grade = models.ForeignKey(StudentYearGrade, on_delete=models.SET_DEFAULT, default=1)

    teacher = models.ManyToManyField(Teacher, blank=True)

    students = models.ManyToManyField(Student, blank=True)

    def class_name(self):
        return self.__class__.__name__

    def get_absolute_url(self):
        return reverse('class-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{} - {}".format(self.name, self.year_grade)


class ExamBoard(models.Model):
    # exam board name eg AQA
    name = models.CharField(max_length=255, null=False)

    # eg AQA fullame = Assessment and Qualifications Alliance
    fullname = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.pk)

    def class_name(self):
        return self.__class__.__name__

    # def label_from_instance(self, obj):
    #    return obj.name


class Exam(models.Model):
    # name of the exam
    name = models.CharField(max_length=255, null=False)

    # M:1 the exam board the paper belongs to
    exam_board = models.ForeignKey(ExamBoard, on_delete=models.CASCADE)

    # THIS FIELD IS NOT NEEDED. Moved to MockExam model
    # This will shift the grade boundaries, so if in the real exam grade 9 was 95 this will increase or reduce by #% to it to make getting the grade more or less challenging
    threshold_buffer = models.FloatField(default=0)

    # grade_boundaries for the exam as set by the exam board
    # note that each paper will also have its own grade boundaries
    # Different exams will have different grade boundaries  and grade labels
    # A,B,C etc  versus the new system in the UK i.e Grade 1,2,3..9
    # Example JSON structure object
    #   {
    #       {
    #           grade_label: 'A',
    #           grade_mark: 90,
    #           grade_order: 1,
    #       }
    #       {
    #           grade_label: 'B',
    #           grade_mark: 75,
    #           grade_order: 2,
    #       }
    #       {
    #           grade_label: 'C',
    #           grade_mark: 60,
    #           grade_order: 3,
    #       }
    #
    #   }
    grade_boundaries = models.CharField(max_length=100, null=True, blank=True)

    # Year date of the exam. The specific date and time sit at the Paper
    ## TODO this would pull into the year from the papers associated with this exam
    ## Most exams sit within a given year Eg Maths Paper 1, 2, & 3 all in 2019
    ## However, some may cross the year eg Paper 1 in November 2018, but Paper 2 in January 2019 and Paper 3 in March 2019
    ## So value here would be "2018/2019"
    exam_date = models.DateField(null=True, blank=True)

    CHOICES = (
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),

    )

    exam_year = models.CharField(max_length=300, choices=CHOICES, blank=True)

    # this is a sum of the marks of each of the papers.
    # TODO  we need to automate this based on summing of the paper.totalMarks in the papers
    total_marks = models.FloatField(default=0, null=False, blank=True)

    # A unique reference for an exam. This is not alway present or easily discernable from the exam papers.
    reference = models.CharField(max_length=255, null=True, blank=True)

    # Subject of the exam
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=False)
    PaperFile = models.FileField(null=True, blank=True)

    # Level or Qualification of the Exam eg GCSE, A-level etc
    level = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=False, default=1, related_name='level_rn')

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return "{} - {}".format(self.name, self.pk)


class MockExam(models.Model):
    # name of the mock exam
    name = models.CharField(max_length=255, null=False)

    # M:M the classes who will be taking this MockExam
    classes = models.ManyToManyField(Class)

    # M:1 relationship. Each MockExam can only have 1 school
    school = models.ForeignKey(School, on_delete=models.SET_DEFAULT, default=1)

    # TODO how much of the Exam class behavoiour needs to be here? For example if the mock exam was taking a full
    #  exam (ie using the exam and all its papers as set by the exam board) the we would need the grade boundaries
    #  for that exam.

    # This will shift the grade boundaries, so if in the real exam grade 9 was 95 this will increase or reduce by #% to it to make getting the grade more or less challenging
    threshold_buffer = models.FloatField(default=0)

    # M:1 relationship. Each MockExam can be linked to an existing Exam proper Exam. If the Exam is "Custom" then
    exam = models.ForeignKey(Exam, on_delete=models.SET_DEFAULT, default=1)

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return "{} - ".format(self.name)


class Paper(models.Model):
    # the subject of the paper , maths, english etc
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    # the name of the paper eg "Paper 3 (Calculator) Foundation Tier"
    name = models.CharField(max_length=255, null=True)

    # The reference used for the paper eg 1MA1/1F
    paper_reference = models.CharField(max_length=255, null=True, blank=True)

    # The barcode used for the paper eg P55584A0120
    paper_code = models.CharField(max_length=255, null=True, blank=True)

    # Length in minutes of the paper
    length = models.FloatField(default=0, null=True, blank=True)

    # date of the test for this paper
    date = models.DateField(null=True, blank=True)

    # M:1 the exam board the paper belongs to
    exam_board = models.ForeignKey(ExamBoard, on_delete=models.DO_NOTHING)

    # M:1 The exam this paper belongs to e.g in maths for a given exam there are 3 papers
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)

    # total marks for this paper
    total_marks = models.FloatField(default=0, null=False)

    # total number of questions
    # TODO this need to be calculated based on the number of questions objects for this paper
    total_questions = models.IntegerField(default=0, null=False)

    # the actual PDF of the paper from the exam board
    pdf = models.FileField(blank=True, null=True)

    # grade_boundaries for the paper as set by the exam board
    # note that each paper will also have its own grade boundaries
    # Example JSON structure object
    #   {
    #       {
    #           grade: '9',
    #           grade_mark: 90,
    #           grade_order: 1,
    #       }
    #       {
    #           grade: '8',
    #           grade_mark: 75,
    #           grade_order: 2,
    #       }
    #       {
    #           grade: '7',
    #           grade_mark: 60,
    #           grade_order: 3,
    #       }
    #
    #   }
    grade_boundaries = models.CharField(max_length=100, null=True, blank=True)

    # This will shift the grade boundaries for the paper, so if in the real paper grade 9 was 75 this will increase or reduce by #% to it to make getting the grade more or less challenging
    threshold_buffer = models.FloatField(default=0)

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return "{} {} {} - {}".format(self.subject, self.paper_reference, self.name, self.pk)


class Topic(models.Model):
    # the name of the topic eg "Addition"
    name = models.CharField(max_length=255, null=True)

    # Specify the level for this topic Eg GCSE, A-level etc
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING, null=True, blank=True)

    # Specify subject for the topic
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True, blank=True, default=1)

    # For a given topic then we have the Topic Questions PDF and
    topic_questions = models.FileField(blank=True, upload_to='Topic/')

    # For a given topic then we have the Topic Questions&Solutions PDF and
    topic_solutions = models.FileField(blank=True, upload_to='Topic/')

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return "{} - {}".format(self.name, self.pk)


class Question(models.Model):
    # M:1 the paper this question belongs to
    paper = models.ForeignKey(Paper, on_delete=models.DO_NOTHING)

    # The ordinal number of the question, first, second etc
    position = models.IntegerField(default=1, null=False)

    #  the text lable as it is in the paper Eg 1, 2a, 5A) 6b ii) etc
    question_label = models.CharField(max_length=10, null=False)

    # the number of marks available for the question
    marks = models.FloatField(default=0, null=False)

    #  topics
    #
    #  TODO linked topics, if  two adajcent questions have the same topic paper then
    #  we should not duplicate the topic questions in the output
    #

    # We use a M:M because for subjective areas such as English, Geography the big mark questions will probably cover
    # multiple topics. Unlike Maths where the relationship between question and topic is more direct
    topics = models.ManyToManyField(Topic)

    class Meta:
        ordering = ['question_label']  # TODO should probably use position

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return "{} - {}".format(self.question_label, self.pk)


class MockExamResults(models.Model):
    school = models.ForeignKey(School, on_delete=models.SET_DEFAULT, default=1)
    mock_exam = models.ForeignKey(MockExam, on_delete=models.DO_NOTHING)

    student = models.ForeignKey(Student, on_delete=models.SET_DEFAULT, default=1)

    paper = models.ForeignKey(Paper, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)

    student_mark = models.FloatField(default=0, null=False)

    @property
    def available_marks(self):
        return self.question.marks

    def class_name(self):
        return self.__class__.__name__


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=1, related_name='author')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=1, related_name='owner')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=1)
    teachers = models.ManyToManyField(Teacher)
    school = models.ForeignKey(School, on_delete=models.SET_DEFAULT, default=1)
    subject = models.ForeignKey(Subject, on_delete=models.SET_DEFAULT, default=1)

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
