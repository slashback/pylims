from django import forms

class UserlistForm(forms.Form):
    last_name = forms.CharField(max_length=100)
    first_name = forms.CharField()
    users = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Notify and subscribe users to this post:")