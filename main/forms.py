from django import forms
from main.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'image', 'subject']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your email address'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your message here'
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your subject'
        })

    def save(self, commit=True):
        instance = super(ContactForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance

