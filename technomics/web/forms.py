from django import forms
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
