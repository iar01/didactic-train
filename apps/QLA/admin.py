from django.contrib import admin
from .models import *


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_alpha2', 'code_alpha3', 'numeric_code', 'Location', 'city')
    search_fields = ('id', 'name', 'code_alpha2', 'code_alpha3', 'numeric_code', 'Location', 'city')


class StudentYearGradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('id', 'name', 'country')


class LevelYearGradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('id', 'name', 'country')


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'urn', 'country', 'school_logo', 'is_validated')
    search_fields = ('id', 'name', 'urn', 'country', 'school_logo', 'is_validated')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'school')
    search_fields = ('id', 'name', 'school')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'surname', 'school', 'student_ref_number', 'dob', 'year_grade')
    search_fields = ('id', 'firstname', 'surname', 'school', 'student_ref_number', 'dob', 'year_grade')


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'school', 'subject', 'year_grade')
    search_fields = ('id', 'name', 'school', 'subject', 'year_grade')


class ExamBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fullname')
    search_fields = ('id', 'name', 'fullname')


class ExamAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'exam_board', 'threshold_buffer', 'exam_date', 'exam_year', 'total_marks', 'reference', 'subject',
        'level')
    search_fields = (
        'id', 'name', 'exam_board', 'threshold_buffer', 'exam_date', 'exam_year', 'total_marks', 'reference', 'subject',
        'level')


class MockExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'school', 'threshold_buffer', 'exam')
    search_fields = ('id', 'name', 'school', 'threshold_buffer', 'exam')


class PaperAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'subject', 'paper_reference', 'paper_code', 'length', 'date', 'exam_board', 'exam', 'total_marks',
        'total_questions', 'pdf')
    search_fields = (
        'id', 'name', 'subject', 'paper_reference', 'paper_code', 'length', 'date', 'exam_board', 'exam', 'total_marks',
        'total_questions', 'pdf')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'subject', 'topic_questions', 'topic_solutions')
    search_fields = ('id', 'name', 'level', 'subject', 'topic_questions', 'topic_solutions')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'paper', 'position', 'question_label', 'marks')
    search_fields = ('id', 'paper', 'position', 'question_label', 'marks')


class MockExamResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'mock_exam', 'student', 'paper', 'question', 'student_mark')
    search_fields = ('id', 'school', 'mock_exam', 'student', 'paper', 'question', 'student_mark')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date_posted', 'author', 'owner', 'creator', 'school', 'subject')
    search_fields = ('id', 'title', 'content', 'date_posted', 'author', 'owner', 'creator', 'school', 'subject')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(StudentYearGrade, StudentYearGradeAdmin)
admin.site.register(Level, LevelYearGradeAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(ExamBoard, ExamBoardAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(MockExam, MockExamAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(MockExamResults, MockExamResultsAdmin)
admin.site.register(Post, PostAdmin)
