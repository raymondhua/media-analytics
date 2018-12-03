from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField(null=True)
    text = models.TextField(null=True)
    author = models.TextField(null=True)
    date = models.DateField(null=True)
    section = models.TextField(null=True)
    url = models.TextField(null=True)