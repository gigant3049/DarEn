from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/main', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
