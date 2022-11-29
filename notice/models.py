from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField()
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
