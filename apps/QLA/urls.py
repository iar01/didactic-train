from django.urls import path
from rest_framework import routers

from .api import *

urlpatterns = [
    path('Subject/', SubjectCreate.as_view(), name='Subject Create'),
    path('Subject/<int:pk>/', SubjectData.as_view(), name='Subject RUD'),
    path('Country/', CountryCreate.as_view(), name='Country Create'),
    path('Country/<int:pk>/', CountryData.as_view(), name='Country RUD'),
    path('StudentYearGrade/', StudentYearGradeCreate.as_view(), name='StudentYearGrade Create'),
    path('StudentYearGrade/<int:pk>/', StudentYearGradeData.as_view(), name='StudentYearGrade RUD'),
    path('Level/', LevelCreate.as_view(), name='Level Create'),
    path('Level/<int:pk>/', LevelData.as_view(), name='Level RUD'),
    path('School/', SchoolCreate.as_view(), name='School Create'),
    path('School/<int:pk>/', SchoolData.as_view(), name='School RUD'),
    path('Teacher/', TeacherCreate.as_view(), name='Teacher Create'),
    path('Teacher/<int:pk>/', TeacherData.as_view(), name='Teacher RUD'),
    path('Student/', StudentCreate.as_view(), name='Student Create'),
    path('Student/<int:pk>/', StudentData.as_view(), name='Student RUD'),
    path('Class/', ClassCreate.as_view(), name='Class Create'),
    path('Class/<int:pk>/', ClassData.as_view(), name='Class RUD'),
    path('ExamBoard/', ExamBoardCreate.as_view(), name='ExamBoard Create'),
    path('ExamBoard/<int:pk>/', ExamBoardData.as_view(), name='ExamBoard RUD'),
    path('Exam/', ExamCreate.as_view(), name='Exam Create'),
    path('Exam/<int:pk>/', ExamData.as_view(), name='Exam RUD'),
    path('MockExam/', MockExamCreate.as_view(), name='MockExam Create'),
    path('MockExam/<int:pk>/', MockExamData.as_view(), name='MockExam RUD'),

    path('Paper/', PaperCreate.as_view(), name='Paper Create'),
    path('Paper/<int:pk>/', PaperData.as_view(), name='Paper RUD'),
    path('Topic/', TopicCreate.as_view(), name='Topic Create'),
    path('Topic/<int:pk>/', TopicData.as_view(), name='Topic RUD'),
    path('Question/', QuestionCreate.as_view(), name='Question Create'),
    path('Question/<int:pk>/', QuestionData.as_view(), name='Question RUD'),
    path('MockExamResults/', MockExamResultsCreate.as_view(), name='MockExamResults Create'),
    path('MockExamResults/<int:pk>/', MockExamResultsData.as_view(), name='MockExamResults RUD'),
    path('Post/', PostCreate.as_view(), name='Post Create'),
    path('Post/<int:pk>/', PostData.as_view(), name='Post RUD'),
]
