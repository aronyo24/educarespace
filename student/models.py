from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True,unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='students/images/',default='default.jpg',blank=True, null=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"