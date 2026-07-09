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

        max_length=20,

        blank=True,

        null=True

    )


    profile_image = models.ImageField(

        upload_to="profiles/",

        blank=True,

        null=True

    )


    school_name = models.CharField(

        max_length=200,

        blank=True,

        null=True

    )


    address = models.CharField(

        max_length=255,

        blank=True,

        null=True

    )


    date_of_birth = models.DateField(

        blank=True,

        null=True

    )


    is_verified = models.BooleanField(

        default=False

    )


    created_at = models.DateTimeField(

        auto_now_add=True

    )


    updated_at = models.DateTimeField(

        auto_now=True

    )


    def is_admin(self):

        return self.role == "ADMIN"



    def is_teacher(self):

        return self.role == "TEACHER"



    def is_student(self):

        return self.role == "STUDENT"



    def __str__(self):

        return f"{self.username} - {self.role}"
