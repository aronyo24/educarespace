from django.db import models

# Create your models here.
class Blooklist(models.Model):
    blooklist_id = models.BigAutoField(primary_key=True,unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='blooklists/images/',default='default.jpg',blank=True, null=True)

    def __str__(self):
        return self.title