from django.db import models

# Create your models here.
class Mail(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  file = models.FileField()
  


  def __str__(self):
      return self.title