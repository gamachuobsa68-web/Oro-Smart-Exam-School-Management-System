from django.db import models

from accounts.models import User

from school.models import Subject



class Teacher(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


    employee_id = models.CharField(
        max_length=50,
        unique=True
    )


    subjects = models.ManyToManyField(
        Subject,
        blank=True
    )


    phone = models.CharField(
        max_length=30,
        blank=True
    )


    def __str__(self):

        return self.employee_id
