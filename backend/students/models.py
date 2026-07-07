from django.db import models

from accounts.models import User

from school.models import ClassRoom



class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


    student_id = models.CharField(
        max_length=50,
        unique=True
    )


    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.SET_NULL,
        null=True
    )


    parent_name = models.CharField(
        max_length=100,
        blank=True
    )


    parent_phone = models.CharField(
        max_length=30,
        blank=True
    )


    date_of_birth = models.DateField(
        null=True,
        blank=True
    )


    def __str__(self):

        return self.student_id
