from django import forms
from django.forms import ModelForm
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Div, Fieldset, Layout, Submit

# from crispy_forms.bootstrap import FormActions

from .models import Blog, Comment, Candidate

class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ('author', 'title', 'description')#, 'created_date')


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('description',)


class CandidateFreshersForm(ModelForm):

    class Meta:
        model = Candidate
        fields = ('name', 'email','phone', 'address','qualification','resume')


class CandidateExperiencedForm(ModelForm):

    class Meta:
        model = Candidate
        fields = ('name', 'email','phone', 'address','qualification','resume')
