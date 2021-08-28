from django.db.models import fields
from django.forms import ModelForm
from .models import Appointment

class Orderform(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'