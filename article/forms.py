from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'image', 'content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your email address'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your image',
            'id': 'file'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your content',
            'cols': 100,
            'rows': 7,
            'id': 'comment'
        })