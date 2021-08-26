from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    phone1 = PhoneNumberField()
    c_add = models.CharField(max_length=100)
    c_city = models.CharField(max_length=100)
    c_state = models.CharField(max_length=150)
    c_zip = models.IntegerField()
    p_add = models.CharField(max_length=100)
    p_city = models.CharField(max_length=100)
    p_state = models.CharField(max_length=150)
    p_zip = models.IntegerField()
    email = models.EmailField()
    messagees = models.TextField(max_length=500)
    a_date_time = models.DateTimeField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email
