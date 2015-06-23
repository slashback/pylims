from django import forms
from datetime import date
from journal.models import MeasurementResult


class RegistrationForm(forms.Form):
    last_name = forms.CharField(max_length=64, label='Фамилия')
    first_name = forms.CharField(max_length=64, label='Имя')
    middle_name = forms.CharField(max_length=64, label='Отчество')
    gender = forms.IntegerField(label='Пол')
    birth_date = forms.DateField(initial=date.today, label='Дата рождения')
    tests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                      label="Исследования:")


class MeasurementResultForm(forms.ModelForm):
    class Meta:
        model = MeasurementResult
        fields = ['measurement', 'value']
        readonly_fields = ('measurement',)
