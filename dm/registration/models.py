from django.db import models

# Create your models here.
class Company(models.Model):
  company = models.CharField(max_length=100)
  email = models.EmailField(max_length=254)
  responsible = models.CharField(max_length=100)


  def __str__(self):
      return self.company
  