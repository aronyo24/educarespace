from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.PositiveBigIntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    subject = models.CharField(max_length=100,blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='teachers/images/',default='default.jpg',blank=True, null=True)

    def __str__(self):
        return self.name
