from django import forms
from .models import PersonalInfo


class PersonalInfoCreateForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['first_name', 'last_name', 'job_title', 'email',
                  'mobile', 'address', 'personal_profile', 'image']





