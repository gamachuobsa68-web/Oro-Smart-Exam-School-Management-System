from django.db import models

from accounts.models import User

from school.models import (
    Subject,
    ClassRoom
)



class Teacher(models.Model):


    user = models.OneToOneField(

        User,

        on_delete=models.CASCADE,

        related_name="teacher_profile"

    )


    employee_id = models.CharField(

        max_length=50,

        unique=True

    )


    subjects = models.ManyToManyField(

        Subject,

        blank=True,

        related_name="teachers"

    )


    classrooms = models.ManyToManyField(

        ClassRoom,

        blank=True,

        related_name="teachers"

    )


    phone = models.CharField(

        max_length=30,

        blank=True,

        null=True

    )


    qualification = models.CharField(

        max_length=200,

        blank=True,

        null=True

    )


    experience_years = models.IntegerField(

        default=0

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

            self.user.get_full_name()

            or self.user.username

        )
