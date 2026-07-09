from django.db import models

from accounts.models import User





class CPDPlan(models.Model):


    title = models.CharField(

        max_length=200

    )


    description = models.TextField()


    month = models.CharField(

        max_length=50

    )


    created_at = models.DateTimeField(

        auto_now_add=True

    )


    def __str__(self):

        return self.title







class CPDActivity(models.Model):


    plan = models.ForeignKey(

        CPDPlan,

        on_delete=models.CASCADE,

        related_name="activities"

    )


    teacher = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

        related_name="cpd_activities"

    )


    activity = models.TextField()


    date = models.DateField()


    STATUS_CHOICES = (

        ("Pending", "Pending"),

        ("Completed", "Completed"),

    )


    status = models.CharField(

        max_length=50,

        choices=STATUS_CHOICES,

        default="Pending"

    )


    created_at = models.DateTimeField(

        auto_now_add=True

    )


    def __str__(self):

        return f"{self.teacher.username} - {self.activity}"
