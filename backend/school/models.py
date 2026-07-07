from django.db import models


class School(models.Model):

    name = models.CharField(
        max_length=200
    )

    address = models.TextField(
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    logo = models.ImageField(
        upload_to="school/logo/",
        blank=True,
        null=True
    )


    def __str__(self):
        return self.name



class AcademicYear(models.Model):

    name = models.CharField(
        max_length=50
    )

    start_date = models.DateField()

    end_date = models.DateField()


    def __str__(self):
        return self.name



class ClassRoom(models.Model):

    name = models.CharField(
        max_length=100
    )

    section = models.CharField(
        max_length=50,
        blank=True
    )


    def __str__(self):
        return self.name



class Subject(models.Model):

    name = models.CharField(
        max_length=100
    )

    code = models.CharField(
        max_length=20,
        unique=True
    )


    def __str__(self):
        return self.name
