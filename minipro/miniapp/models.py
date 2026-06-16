from django import forms
from django.db import models
import uuid
# Create your models here.

class Register(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(widget=forms.PasswordInput)
    confirm_password = models.CharField(label="Confirm Password", widget=forms.PasswordInput)
    phone_number = models.IntegerField(max_length=15)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    def __str__(self):
        return self.username