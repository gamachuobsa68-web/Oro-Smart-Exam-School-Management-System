from django.db import models

from accounts.models import User

from school.models import (
    Subject,
    ClassRoom
)



class TeacherAssistant(models.Model):

    teacher = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


    qualification = models.CharField(
        max_length=200
    )


    specialization = models.CharField(
        max_length=200
    )


    phone = models.CharField(
        max_length=50,
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.teacher.username





class LessonPlan(models.Model):

    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )


    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )


    topic = models.CharField(
        max_length=200
    )


    objective = models.TextField()


    teaching_method = models.TextField()


    learning_activity = models.TextField()


    assessment = models.TextField()


    date = models.DateField()



    def __str__(self):

        return self.topic





class CPD(models.Model):

    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    title = models.CharField(
        max_length=200
    )


    description = models.TextField()


    month = models.CharField(
        max_length=50
    )


    hours = models.IntegerField(
        default=0
    )


    status = models.CharField(
        max_length=50,
        default="Pending"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title





class CPDReport(models.Model):

    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    month = models.CharField(
        max_length=50
    )


    completed_cpd = models.IntegerField(
        default=0
    )


    total_hours = models.IntegerField(
        default=0
    )


    comment = models.TextField(
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.teacher.username
