from django import forms
from .models import *
  
class DetectionForm(forms.ModelForm):
  
    class Meta:
        model = Detection
        fields = ['name', 'image']