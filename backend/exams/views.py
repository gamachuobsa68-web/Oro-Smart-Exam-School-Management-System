from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated


from .models import (
    Exam,
    Question,
    StudentAnswer,
    ExamResult
)


from .serializers import (
    ExamSerializer,
    ExamResultSerializer
)


from accounts.permissions import (
    IsTeacher,
    IsStudent
)





class TeacherExamView(APIView):

    permission_classes = [
        IsTeacher
    ]


    def get(self, request):

        exams = Exam.objects.filter(
            teacher=request.user
        )

        serializer = ExamSerializer(
            exams,
            many=True
        )

        return Response(
            serializer.data
        )



    def post(self, request):

        serializer = ExamSerializer(
            data=request.data
        )


        if serializer.is_valid():

            serializer.save(
                teacher=request.user
            )

            return Response(
                serializer.data,
                status=201
            )


        return Response(
            serializer.errors,
            status=400
        )







class StudentExamView(APIView):

    permission_classes = [
        IsStudent
    ]


    def get(self, request):

        exams = Exam.objects.filter(
            is_published=True
        )


        serializer = ExamSerializer(
            exams,
            many=True
        )


        return Response(
            serializer.data
        )







class SubmitExamView(APIView):

    permission_classes = [
        IsStudent
    ]



    def post(self, request):

        exam_id = request.data.get(
            "exam_id"
        )


        answers = request.data.get(
            "answers",
            []
        )


        exam = Exam.objects.get(
            id=exam_id
        )


        total = 0



        for item in answers:


            question = Question.objects.get(
                id=item["question"]
            )


            answer = item["answer"]


            correct = (
                answer ==
                question.correct_answer
            )


            mark = 0


            if correct:

                mark = question.mark

                total += mark



            StudentAnswer.objects.create(

                student=request.user,

                question=question,

                answer=answer,

                is_correct=correct,

                mark_obtained=mark

            )



        percentage = (
            total /
            exam.total_mark
        ) * 100



        result = ExamResult.objects.create(

            student=request.user,

            exam=exam,

            total_mark=total,

            percentage=percentage

        )


        return Response(
            ExamResultSerializer(result).data
            )
