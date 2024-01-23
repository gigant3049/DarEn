from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    created_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/articles')

    def __str__(self):
        return self.title


