from django.db import models

# Create your models here.
class Note(models.Model):
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True)