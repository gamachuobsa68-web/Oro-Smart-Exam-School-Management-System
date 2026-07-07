from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.utils import timezone


from .models import (
    Exam,
    Question,
    ExamAttempt,
    StudentAnswer,
    ExamResult
)


from .serializers import (
    ExamSerializer,
    ExamAttemptSerializer,
    ExamResultSerializer
)


from accounts.permissions import (
    IsTeacher,
    IsStudent
)



# =========================
# TEACHER CREATE / VIEW EXAM
# =========================

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





# =========================
# STUDENT VIEW PUBLISHED EXAM
# =========================

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





# =========================
# START EXAM TIMER
# =========================

class StartExamView(APIView):

    permission_classes = [
        IsStudent
    ]


    def post(self, request):

        exam_id = request.data.get(
            "exam_id"
        )


        exam = Exam.objects.get(
            id=exam_id
        )


        already_started = ExamAttempt.objects.filter(
            student=request.user,
            exam=exam
        ).exists()


        if already_started:

            return Response(
                {
                    "message":
                    "Exam already started"
                },
                status=400
            )



        attempt = ExamAttempt.objects.create(

            student=request.user,

            exam=exam

        )


        return Response(

            {
                "attempt":
                ExamAttemptSerializer(attempt).data,

                "duration_minutes":
                exam.duration_minutes

            }

        )





# =========================
# SAVE ANSWER BUTTON
# =========================

class SaveAnswerView(APIView):

    permission_classes = [
        IsStudent
    ]


    def post(self, request):

        question_id = request.data.get(
            "question_id"
        )


        exam_id = request.data.get(
            "exam_id"
        )


        answer = request.data.get(
            "answer"
        )


        question = Question.objects.get(
            id=question_id
        )


        exam = Exam.objects.get(
            id=exam_id
        )


        StudentAnswer.objects.update_or_create(

            student=request.user,

            exam=exam,

            question=question,

            defaults={

                "answer": answer

            }

        )


        return Response(

            {
                "message":
                "Answer saved"
            }

        )





# =========================
# SUBMIT EXAM + AUTO MARK
# =========================

class SubmitExamView(APIView):

    permission_classes = [
        IsStudent
    ]


    def post(self, request):

        exam_id = request.data.get(
            "exam_id"
        )


        exam = Exam.objects.get(
            id=exam_id
        )


        answers = StudentAnswer.objects.filter(

            student=request.user,

            exam=exam

        )


        total = 0



        for item in answers:


            if item.answer == item.question.correct_answer:


                item.is_correct = True

                item.mark_obtained = (
                    item.question.mark
                )

                total += item.question.mark


            else:

                item.is_correct = False

                item.mark_obtained = 0



            item.save()



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



        attempt = ExamAttempt.objects.filter(

            student=request.user,

            exam=exam

        ).first()



        if attempt:

            attempt.submitted = True

            attempt.submitted_at = timezone.now()

            attempt.save()



        return Response(

            ExamResultSerializer(result).data

                )
