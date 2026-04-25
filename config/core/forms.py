from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message','honeypot']