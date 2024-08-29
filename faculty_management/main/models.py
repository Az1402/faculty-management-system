from django.db import models


# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class Dean(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=255)

class Department(models.Model):
    name = models.CharField(max_length=100)
    hod = models.OneToOneField(User, related_name='hod', on_delete=models.CASCADE)
    teachers = models.ManyToManyField(User, related_name='teachers')

class Announcement(models.Model):
    dean = models.ForeignKey(Dean, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Complaint(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
