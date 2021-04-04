from django import forms
from django.forms import ModelForm
from .models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        labels = {
            'birthdate': 'Your Birth Date : ',
            'name': 'Name : ',
            'about': 'Introduce about yourself : ',
            'contact': 'Phone Number : ',
            'address': 'Address : ',
            'email': 'Email : ',
            'achievement1': 'Achievement 1 : ',
            'achievement2': 'Achievement 2 : ',
            'achievement3': 'Achievement 3 : ',
            'certificate1': 'Educational Certificate 1 : ',
            'certificate2': 'Educational Certificate 2 : ',
            'experience1': 'Working Experience 1 :',
            'experience2': 'Working Experience 2 :',
            'experience3': 'Working Experience 3 :',
            'skills': 'Skill : ',
            'interest': 'Interest : ',
            'reference': 'Reference : '
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(format=('%d-%m-%Y'),
                                         attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'achievement1': forms.Textarea(attrs={'class': 'form-control'}),
            'achievement2': forms.Textarea(attrs={'class': 'form-control'}),
            'achievement3': forms.Textarea(attrs={'class': 'form-control'}),
            'certificate1': forms.Textarea(attrs={'class': 'form-control'}),
            'certificate2': forms.Textarea(attrs={'class': 'form-control'}),
            'experience1': forms.Textarea(attrs={'class': 'form-control'}),
            'experience2': forms.Textarea(attrs={'class': 'form-control'}),
            'experience3': forms.Textarea(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'interest': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'reference': forms.TextInput(attrs={'class': 'form-control'})
        }
