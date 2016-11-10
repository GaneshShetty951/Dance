from django.core.validators import RegexValidator
from django.db import models
# Create your models here.


class UpComingEvents(models.Model):
    EventDate = models.DateTimeField(primary_key=True)
    EventName = models.CharField(max_length=100, default="ABC")
    EventVenue = models.CharField(max_length=100, default='Bangalore')
    EventImage = models.ImageField(upload_to='', blank=True, null=True)
    EventOrganiser = models.CharField(max_length=100, default="XYZ")
    ShowCategory = models.CharField(max_length=7, default='Free', choices=(('Free', 'Free'), ('Passes', 'Passes'), ('Private', 'Private')))
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '1234567890'. Up to 10 digits allowed.")
    EventContact = models.CharField(max_length=10, validators=[phone_regex], blank=True) # validators should be a list
    EventLink = models.URLField(default='http://127.0.0.1:8000/')

class Awards(models.Model):
    Award_Name=models.CharField(max_length=100)