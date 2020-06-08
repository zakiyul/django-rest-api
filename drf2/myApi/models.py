from django.db import models

class Framework(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  language = models.CharField(max_length=50)

  def __str__(self):
    return self.name
