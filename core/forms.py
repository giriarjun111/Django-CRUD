from django import forms
from .models import Employee, Contact

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['position'].required = True


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    