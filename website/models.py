from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email