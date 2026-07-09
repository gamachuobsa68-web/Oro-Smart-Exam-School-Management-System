from django.db import models

from accounts.models import User





class AssistantRequest(models.Model):


    REQUEST_TYPES = (

        ("QUESTION", "Question Generator"),

        ("LESSON", "Lesson Helper"),

        ("EXAM", "Exam Helper"),

    )


    user = models.ForeignKey(

        User,

        on_delete=models.CASCADE

    )


    request_type = models.CharField(

        max_length=20,

        choices=REQUEST_TYPES

    )


    prompt = models.TextField()


    response = models.TextField(

        blank=True

    )


    created_at = models.DateTimeField(

        auto_now_add=True

    )



    def __str__(self):

        return self.request_type
