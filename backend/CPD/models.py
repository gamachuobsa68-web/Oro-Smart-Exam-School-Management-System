from django.db import models


class CPDPlan(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    month = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CPDActivity(models.Model):
    plan = models.ForeignKey(
        CPDPlan,
        on_delete=models.CASCADE,
        related_name="activities"
    )
    teacher = models.CharField(max_length=150)
    activity = models.TextField()
    date = models.DateField()
    status = models.CharField(
        max_length=50,
        default="Pending"
    )

    def __str__(self):
        return self.activity
