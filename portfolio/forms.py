from django import forms
from .models import Contact
from .models import Review



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class Reviewform(forms.ModelForm):
    class Meta:
        model =Review
        fields = ['name', 'message']
        # widgets = {
        #     'name': forms.TextInput(attrs={
        #         'class': 'form-input',
        #         'placeholder': 'Your name'
        #     }),
        #     'message': forms.Textarea(attrs={
        #         'class': 'form-textarea',
        #         'placeholder': 'Your review...'
        #     }),
        # }
