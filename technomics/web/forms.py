from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
