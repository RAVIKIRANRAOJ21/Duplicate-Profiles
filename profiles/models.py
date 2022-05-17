from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    date_of_birth = models.DateField(null=True) # format will be YYYY-MM-DD
    class_year = models.PositiveIntegerField(null=True)
    email_field = models.EmailField()