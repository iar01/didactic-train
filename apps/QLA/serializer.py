from rest_framework import serializers
from .models import *
from ..Users.serializers import CompactUserSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StudentYearGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentYearGrade
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class ExamBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamBoard
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class MockExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockExam
        fields = '__all__'


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class MockExamResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockExamResults
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


# Compact / nested Serializers

class StudentYearGradeSerializerData(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = StudentYearGrade
        fields = '__all__'


class LevelSerializerData(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Level
        fields = '__all__'


class SchoolSerializerData(serializers.ModelSerializer):
    country = CountrySerializer()
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = School
        fields = '__all__'


class TeacherSerializerData(serializers.ModelSerializer):
    school = SchoolSerializer()
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializerData(serializers.ModelSerializer):
    school = SchoolSerializer()
    year_grade = StudentYearGradeSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class ClassSerializerData(serializers.ModelSerializer):
    school = SchoolSerializer()
    subject = SubjectSerializer()
    year_grade = StudentYearGradeSerializer()
    teacher = TeacherSerializer()
    students = StudentSerializer(many=True)

    class Meta:
        model = Class
        fields = '__all__'


class ExamSerializerData(serializers.ModelSerializer):
    PaperFile = serializers.SerializerMethodField()
    exam_board = ExamBoardSerializer()
    subject = SubjectSerializer()
    level = LevelSerializer()

    class Meta:
        model = Exam
        fields = '__all__'

    def get_PaperFile(self, Exam):
        request = self.context.get('request')
        PaperFile = Exam.PaperFile.url
        return request.build_absolute_uri(PaperFile)


class MockExamSerializerData(serializers.ModelSerializer):
    classes = ClassSerializer(many=True)
    school = SchoolSerializer()
    exam = ExamSerializer()

    class Meta:
        model = MockExam
        fields = '__all__'


class PaperSerializerData(serializers.ModelSerializer):
    pdf = serializers.SerializerMethodField()
    subject = SubjectSerializer()
    exam_board = ExamBoardSerializer()
    exam = ExamSerializer()

    class Meta:
        model = Paper
        fields = '__all__'

    def get_pdf(self, Paper):
        request = self.context.get('request')
        pdf = Paper.pdf.url
        return request.build_absolute_uri(pdf)


class TopicSerializerData(serializers.ModelSerializer):
    level = LevelSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Topic
        fields = '__all__'


class QuestionSerializerData(serializers.ModelSerializer):
    paper = PaperSerializer()
    topics = TopicSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class MockExamResultsSerializerData(serializers.ModelSerializer):
    school = SchoolSerializer()
    mock_exam = MockExamSerializer()
    student = StudentSerializer()
    paper = PaperSerializer()
    question = QuestionSerializer()

    class Meta:
        model = MockExamResults
        fields = '__all__'


class PostSerializerData(serializers.ModelSerializer):
    author = CompactUserSerializer()
    owner = CompactUserSerializer()
    creator = CompactUserSerializer()
    teachers = TeacherSerializer(many=True)
    school = SchoolSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Post
        fields = '__all__'
