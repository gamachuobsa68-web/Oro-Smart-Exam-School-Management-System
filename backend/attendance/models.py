from django.db import models

from accounts.models import User

from school.models import ClassRoom





class Attendance(models.Model):

    STATUS_CHOICES = (

        ("PRESENT", "Present"),

        ("ABSENT", "Absent"),

        ("LATE", "Late"),

    )


    student = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

        related_name="attendance_records"

    )


    classroom = models.ForeignKey(

        ClassRoom,

        on_delete=models.CASCADE

    )


    date = models.DateField(

        auto_now_add=True

    )


    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="PRESENT"

    )


    marked_by = models.ForeignKey(

        User,

        on_delete=models.SET_NULL,

        null=True,

        related_name="attendance_marked"

    )


    created_at = models.DateTimeField(

        auto_now_add=True

    )



    def __str__(self):

        return (
            self.student.username
            + "-"
            + self.status
        )
