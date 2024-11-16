from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 100:
            raise forms.ValidationError("Message must be at least 100 characters long.")
        return message


# here i'll handle task creation and updates
# from django import forms
# from .models import Task

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title','completed']