from rest_framework.views import APIView
from rest_framework.response import Response


from accounts.permissions import (

    IsAdmin,

    IsTeacher,

    IsStudent

)


from accounts.models import User

from students.models import StudentProfile

from teachers.models import Teacher

from exams.models import Exam

from reports.models import ReportCard

from professional.models import LessonPlan, CPD





# =========================
# ADMIN DASHBOARD
# =========================

class AdminDashboardView(APIView):


    permission_classes = [

        IsAdmin

    ]



    def get(self, request):


        return Response({

            "role": "ADMIN",

            "message": "Admin control panel",


            "statistics": {

                "total_users":
                User.objects.count(),


                "total_students":
                StudentProfile.objects.count(),


                "total_teachers":
                Teacher.objects.count(),


                "total_exams":
                Exam.objects.count(),


                "total_reports":
                ReportCard.objects.count(),

            },


            "permissions": [

                "Manage users",

                "Manage teachers",

                "Manage students",

                "Manage exams",

                "Manage reports",

                "System settings"

            ]

        })







# =========================
# TEACHER DASHBOARD
# =========================

class TeacherDashboardView(APIView):


    permission_classes = [

        IsTeacher

    ]



    def get(self, request):


        return Response({

            "role": "TEACHER",


            "message": "Teacher dashboard",



            "statistics": {


                "my_exams":

                Exam.objects.filter(

                    teacher=request.user

                ).count(),



                "my_lesson_plans":

                LessonPlan.objects.filter(

                    teacher=request.user

                ).count(),



                "my_cpd":

                CPD.objects.filter(

                    teacher=request.user

                ).count(),


            },



            "permissions": [

                "Create exam",

                "Create questions",

                "View class roster",

                "Lesson plan",

                "CPD management"

            ]

        })








# =========================
# STUDENT DASHBOARD
# =========================

class StudentDashboardView(APIView):


    permission_classes = [

        IsStudent

    ]



    def get(self, request):


        return Response({

            "role": "STUDENT",


            "message": "Student dashboard",



            "statistics": {


                "available_exams":

                Exam.objects.filter(

                    is_published=True

                ).count(),



                "my_results":

                ReportCard.objects.filter(

                    student=request.user

                ).count(),

            },



            "permissions": [

                "View profile",

                "Take exam",

                "Save answer",

                "View result",

                "Download report card"

            ]

        })
