from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class session(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    content = QuillField()


    def __str__(self):
        return self.title