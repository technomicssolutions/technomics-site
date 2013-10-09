from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class FresherForm(forms.Form):
    name = forms.CharField(max_length=100)
    degree = forms.ChoiceField(choices= frozenset(['B.Tech', 'B.Sc']))
    mark = forms.IntegerField()
    percentage = forms.FloatField()
