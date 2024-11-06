from django import forms
from .models import Employee


class add_employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'contact', 'city']
