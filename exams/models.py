from django.utils import timezone
from django.db import models

class Examination(models.Model):
    exam_id=models.AutoField
    student_name=models.CharField(max_length=50, default="")
    roll_number = models.IntegerField( default="")
    sub1_name=models.CharField(max_length=50, default="")
    sub2_name=models.CharField(max_length=50, default="")
    sub3_name=models.CharField(max_length=50, default="")
    sub1_marks = models.IntegerField( default="")
    sub2_marks = models.IntegerField(default="")
    sub3_marks = models.IntegerField( default="")
    pub_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.student_name


