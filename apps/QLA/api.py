from rest_framework import generics
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SubjectCreate(APIView):
    serializer_class = SubjectSerializer

    def get(self, request, format=None):
        data = Subject.objects.all()
        serializer = SubjectSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Subject.objects.filter(id=self.kwargs['pk'])

    serializer_class = SubjectSerializer


class CountryCreate(APIView):
    serializer_class = CountrySerializer

    def get(self, request, format=None):
        data = Country.objects.all()
        serializer = CountrySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Country.objects.filter(id=self.kwargs['pk'])

    serializer_class = CountrySerializer


class StudentYearGradeCreate(APIView):
    serializer_class = StudentYearGradeSerializer

    def get(self, request, format=None):
        data = StudentYearGrade.objects.all()
        serializer = StudentYearGradeSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentYearGradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentYearGradeData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return StudentYearGrade.objects.filter(id=self.kwargs['pk'])

    serializer_class = StudentYearGradeSerializer


class LevelCreate(APIView):
    serializer_class = LevelSerializer

    def get(self, request, format=None):
        data = Level.objects.all()
        serializer = LevelSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LevelData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Level.objects.filter(id=self.kwargs['pk'])

    serializer_class = LevelSerializer


class SchoolCreate(APIView):
    serializer_class = SchoolSerializer

    def get(self, request, format=None):
        data = School.objects.all()
        serializer = SchoolSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolCreateTest(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return School.objects.filter(id=self.kwargs['pk'])

    serializer_class = SchoolSerializer


class TeacherCreate(APIView):
    serializer_class = TeacherSerializer

    def get(self, request, format=None):
        data = Teacher.objects.all()
        serializer = TeacherSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Teacher.objects.filter(id=self.kwargs['pk'])

    serializer_class = TeacherSerializer


class StudentCreate(APIView):
    serializer_class = StudentSerializer

    def get(self, request, format=None):
        data = Student.objects.all()
        serializer = StudentSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Student.objects.filter(id=self.kwargs['pk'])

    serializer_class = StudentSerializer


class ClassCreate(APIView):
    serializer_class = ClassSerializer

    def get(self, request, format=None):
        data = Class.objects.all()
        serializer = ClassSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Class.objects.filter(id=self.kwargs['pk'])

    serializer_class = ClassSerializer


class ExamBoardCreate(APIView):
    serializer_class = ExamBoardSerializer

    def get(self, request, format=None):
        data = ExamBoard.objects.all()
        serializer = ExamBoardSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExamBoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamBoardData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return ExamBoard.objects.filter(id=self.kwargs['pk'])

    serializer_class = ExamBoardSerializer


class ExamCreate(APIView):
    serializer_class = ExamSerializer

    def get(self, request, format=None):
        data = Exam.objects.all()
        serializer = ExamSerializerData(data, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Exam.objects.filter(id=self.kwargs['pk'])

    serializer_class = ExamSerializer


class MockExamCreate(APIView):
    serializer_class = MockExamSerializer

    def get(self, request, format=None):
        data = MockExam.objects.all()
        serializer = MockExamSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MockExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MockExamData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return MockExam.objects.filter(id=self.kwargs['pk'])

    serializer_class = MockExamSerializer


class PaperCreate(APIView):
    serializer_class = PaperSerializer

    def get(self, request, format=None):
        data = Paper.objects.all()
        serializer = PaperSerializerData(data, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaperData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Paper.objects.filter(id=self.kwargs['pk'])

    serializer_class = PaperSerializer


class TopicCreate(APIView):
    serializer_class = TopicSerializer

    def get(self, request, format=None):
        data = Topic.objects.all()
        serializer = TopicSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopicData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Topic.objects.filter(id=self.kwargs['pk'])

    serializer_class = TopicSerializer


class QuestionCreate(APIView):
    serializer_class = QuestionSerializer

    def get(self, request, format=None):
        data = Question.objects.all()
        serializer = QuestionSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Question.objects.filter(id=self.kwargs['pk'])

    serializer_class = QuestionSerializer


class MockExamResultsCreate(APIView):
    serializer_class = MockExamResultsSerializer

    def get(self, request, format=None):
        data = MockExamResults.objects.all()
        serializer = MockExamResultsSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MockExamResultsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MockExamResultsData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return MockExamResults.objects.filter(id=self.kwargs['pk'])

    serializer_class = MockExamResultsSerializer


class PostCreate(APIView):
    serializer_class = PostSerializer

    def get(self, request, format=None):
        data = Post.objects.all()
        serializer = PostSerializerData(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs['pk'])

    serializer_class = PostSerializer
