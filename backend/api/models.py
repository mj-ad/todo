from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
