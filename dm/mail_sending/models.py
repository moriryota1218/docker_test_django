from django.db import models

# Create your models here.
class Mail(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  file = models.FileField()
  start = models.DateTimeField('送信時間')


  def __str__(self):
    start = timezone.localtime(self.start).strftime('%Y/%m/%d %H:%M:%S')
    return self.title