from django.db import models

from accounts.models import User

from school.models import ClassRoom



class StudentProfile(models.Model):


    user = models.OneToOneField(

        User,

        on_delete=models.CASCADE,

        related_name="student_profile"

    )


    student_id = models.CharField(

        max_length=50,

        unique=True

    )


    classroom = models.ForeignKey(

        ClassRoom,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="students"

    )


    photo = models.ImageField(

        upload_to="students/",

        blank=True,

        null=True

    )


    parent_name = models.CharField(

        max_length=200,

        blank=True,

        null=True

    )


    parent_phone = models.CharField(

        max_length=50,

        blank=True,

        null=True

    )


    address = models.TextField(

        blank=True,

        null=True

    )


    date_of_birth = models.DateField(

        blank=True,

        null=True

    )


    gender = models.CharField(

        max_length=20,

        blank=True,

        null=True

    )


    is_active = models.BooleanField(

        default=True

    )


    created_at = models.DateTimeField(

        auto_now_add=True

    )


    updated_at = models.DateTimeField(

        auto_now=True

    )



    def __str__(self):

        return (

            self.student_id

            +

            " - "

            +

            self.user.username

        )
