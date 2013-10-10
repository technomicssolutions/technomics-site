from django import forms
from django.forms import ModelForm
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Div, Fieldset, Layout, Submit

# from crispy_forms.bootstrap import FormActions

from .models import Candidate
DEGREE = (
       (1, ("B.Tech")),
       (2, ("B.Sc")), 
   )

class CommentForm(forms.Form):
    author = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class FresherForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    degree = forms.ChoiceField(choices=DEGREE, required=True)
    marks = forms.IntegerField(required=True)
    percentage = forms.FloatField(required=True)
    resume = forms.FileField(required=True)

    def clean(self):
        upload_to = 'uploads/images/'
        upload_to += self.cleaned_data['resume'].name

class CandidateExperiencedForm(ModelForm):

    class Meta:
        model = Candidate
        fields = ('name', 'email','phone', 'address','qualification','resume')