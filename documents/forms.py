from django.forms import ModelForm
from django import forms
import datetime
from .models import *

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'featured_image']

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'form-control'})

        self.fields['title'].widget.attrs.update(
            {'class': 'input'})

        self.fields['description'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Short Description'})

# Leave Section
class LeaveForm(ModelForm):
    class Meta:
        model = Leave
        fields = ['leave', 'startdate', 'enddate', 'reason']

    def __init__(self, *args, **kwargs):
        super(LeaveForm, self).__init__(*args, **kwargs)

        self.fields['leave'].widget.attrs.update(
            {'class': 'input'})

        self.fields['startdate'].widget.attrs.update(
            {'class': 'input', 'placeholder': '2022-06-23'})

        self.fields['enddate'].widget.attrs.update(
            {'class': 'input', 'placeholder': '2022-06-23'})

        self.fields['reason'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Reason..'})

        
