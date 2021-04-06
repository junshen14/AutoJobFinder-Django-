from django.db import models


# Create your models here.

JOB_CATEGORY = (('Accounting and Finance', 'Accounting and Finance'),
                ('Art/ Media/ Communication', 'Art/ Media/ Communication'),
                ('Computer/Information Technology',
                 'Computer/Information Technology'),
                ('Engineering', 'Engineering'))


class Resume(models.Model):
    category = models.CharField(
        max_length=200, choices=JOB_CATEGORY, default='Accounting and Finance')
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
