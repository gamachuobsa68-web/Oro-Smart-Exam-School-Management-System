from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):

    ROLE_CHOICES = (

        ("ADMIN", "Admin"),

        ("TEACHER", "Teacher"),

        ("STUDENT", "Student"),

    )


    role = models.CharField(

        max_length=20,

        choices=ROLE_CHOICES,

        default="STUDENT"

    )


    phone = models.CharField(

        max_length=50,

        blank=True

    )


    def __str__(self):

        return self.username
