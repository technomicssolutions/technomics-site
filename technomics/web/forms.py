from django import forms
from django.forms import ModelForm
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Div, Fieldset, Layout, Submit

# from crispy_forms.bootstrap import FormActions

from .models import Candidate

class CommentForm(forms.Form):
    author = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class CandidateFreshersForm(ModelForm):

    class Meta:
        model = Candidate
        fields = ('name', 'email','phone', 'address','qualification','resume')


class CandidateExperiencedForm(ModelForm):

    class Meta:
        model = Candidate
        fields = ('name', 'email','phone', 'address','qualification','resume')
