from django.db import models





class School(models.Model):


    name = models.CharField(

        max_length=200

    )


    address = models.TextField(

        blank=True,

        null=True

    )


    phone = models.CharField(

        max_length=30,

        blank=True,

        null=True

    )


    logo = models.ImageField(

        upload_to="school/logo/",

        blank=True,

        null=True

    )


    email = models.EmailField(

        blank=True,

        null=True

    )


    created_at = models.DateTimeField(

        auto_now_add=True

    )


    def __str__(self):

        return self.name






class AcademicYear(models.Model):


    name = models.CharField(

        max_length=50

    )


    start_date = models.DateField()


    end_date = models.DateField()


    is_current = models.BooleanField(

        default=False

    )


    def __str__(self):

        return self.name






class ClassRoom(models.Model):


    school = models.ForeignKey(

        School,

        on_delete=models.CASCADE,

        related_name="classrooms",

        null=True,

        blank=True

    )


    name = models.CharField(

        max_length=100

    )


    section = models.CharField(

        max_length=50,

        blank=True,

        null=True

    )


    academic_year = models.ForeignKey(

        AcademicYear,

        on_delete=models.SET_NULL,

        null=True,

        blank=True

    )


    capacity = models.IntegerField(

        default=40

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


    description = models.TextField(

        blank=True,

        null=True

    )


    is_active = models.BooleanField(

        default=True

    )


    def __str__(self):

        return self.name
