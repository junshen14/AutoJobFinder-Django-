from django.db import models


# Create your models here.


class Resume(models.Model):
    about = models.TextField()
    name = models.CharField(max_length=200, default="")
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, default="")
    contact = models.CharField(max_length=10, default="")
    address = models.TextField(default="")
    email = models.EmailField(default="")
    achievement1 = models.TextField(default="", blank=True, null=True)
    achievement2 = models.TextField(default="", blank=True, null=True)
    achievement3 = models.TextField(default="", blank=True, null=True)
    certificate1 = models.TextField(default="")
    certificate2 = models.TextField(default="", blank=True, null=True)
    experience1 = models.TextField(default="", blank=True, null=True)
    experience2 = models.TextField(default="", blank=True, null=True)
    experience3 = models.TextField(default="", blank=True, null=True)
    skills = models.TextField(default="")
    interest = models.TextField(default="")
    reference = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name
