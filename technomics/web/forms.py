from django import forms
from django.forms import ModelForm

from .models import Blog, Comment, Candidate, Contactus

class ContactUsForm(ModelForm):

    class Meta:
        model = Contactus
        fields = ('name', 'email_id','subject' , 'message')
        

class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'description')

    
class BlogCommentForm(ModelForm):

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
