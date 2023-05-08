from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)


class Student(models.Model):
    Student_ID = models.IntegerField(primary_key=True)
    Student_Name = models.CharField(max_length=50)
    Student_Department = models.CharField(max_length=50)
    Student_Grade = models.IntegerField()

    class Meta:
        db_table = 'student'
