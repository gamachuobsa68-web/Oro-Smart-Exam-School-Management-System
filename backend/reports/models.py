from django.db import models

from accounts.models import User

from school.models import AcademicYear



class SchoolProfile(models.Model):

    name = models.CharField(
        max_length=200
    )

    logo = models.ImageField(
        upload_to="school_logo/",
        blank=True,
        null=True
    )

    address = models.CharField(
        max_length=300,
        blank=True
    )


    phone = models.CharField(
        max_length=50,
        blank=True
    )


    def __str__(self):

        return self.name





class ReportCard(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE
    )


    total_mark = models.FloatField(
        default=0
    )


    average = models.FloatField(
        default=0
    )


    rank = models.IntegerField(
        default=0
    )


    grade = models.CharField(
        max_length=5,
        blank=True
    )


    status = models.CharField(
        max_length=20,
        default="FAIL"
    )


    teacher_comment = models.TextField(
        blank=True
    )


    principal_comment = models.TextField(
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )



    def save(self,*args,**kwargs):

        if self.average >= 80:
            self.grade="A"

        elif self.average >=70:
            self.grade="B"

        elif self.average >=60:
            self.grade="C"

        elif self.average >=50:
            self.grade="D"

        else:
            self.grade="F"



        if self.average >=50:
            self.status="PASS"

        else:
            self.status="FAIL"



        super().save(*args,**kwargs)



    def __str__(self):

        return self.student.username
