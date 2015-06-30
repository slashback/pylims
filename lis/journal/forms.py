from django import forms
from datetime import date
from journal.models import MeasurementResult
from django.utils.safestring import mark_safe
from django.forms.models import modelformset_factory


class RegistrationForm(forms.Form):
    GENDER_FEMALE = 0
    GENDER_MALE = 1
    GENDER_UNDEFINED = 2
    GENDER_LIST = (
        (GENDER_FEMALE, 'Жен.'),
        (GENDER_MALE, 'Муж'),
        (GENDER_UNDEFINED, 'Не указано'),
    )
    last_name = forms.CharField(max_length=64, label='Фамилия')
    first_name = forms.CharField(max_length=64, label='Имя')
    middle_name = forms.CharField(max_length=64, label='Отчество')
    gender = forms.ChoiceField(choices=GENDER_LIST,
                               initial=GENDER_UNDEFINED,
                               label='Пол'
                               )
    birth_date = forms.DateField(initial=date.today, label='Дата рождения')
    biomaterials = forms.ChoiceField(label='Биоматериал')
    tests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                      label="Исследования:")


class SpanWidget(forms.Widget):
    '''Renders a value wrapped in a <span> tag.
    Requires use of specific form support. (see ReadonlyForm
    or ReadonlyModelForm)
    '''

    def render(self, name, value, attrs=None):
        return mark_safe(u'<span>%s</span>' % (
            self.original_value))

    def value_from_datadict(self, data, files, name):
        return self.original_value


class SpanField(forms.Field):
    '''A field which renders a value wrapped in a <span> tag.
    Requires use of specific form support. (see ReadonlyForm
    or ReadonlyModelForm)
    '''

    def __init__(self, *args, **kwargs):
        kwargs['widget'] = kwargs.get('widget', SpanWidget)
        super(SpanField, self).__init__(*args, **kwargs)


class Readonly(object):
    '''Base class for ReadonlyForm and ReadonlyModelForm which provides
    the meat of the features described in the docstings for those classes.
    '''

    class NewMeta:
        readonly = tuple()

    def __init__(self, *args, **kwargs):
        super(Readonly, self).__init__(*args, **kwargs)
        readonly = self.NewMeta.readonly
        if not readonly:
            return
        for name, field in self.fields.items():
            if name in readonly:
                field.widget = SpanWidget()
            elif not isinstance(field, SpanField):
                continue
            field.widget.original_value = str(getattr(self.instance, name))


class ReadonlyForm(Readonly, forms.ModelForm):
    pass


class ReadonlyModelForm(Readonly, forms.ModelForm):
    pass


class MeasurementResultForm(ReadonlyModelForm):
    class Meta:
        model = MeasurementResult
        fields = ['measurement', 'value']

    class NewMeta:
        readonly = ('measurement',)

    def clean(self):
        super(MeasurementResultForm, self).clean()
        if 'measurement' in self._errors:
            del self._errors['measurement']
        return self.cleaned_data


ResultFormSetBase = modelformset_factory(
  MeasurementResult, extra=0, form=MeasurementResultForm)


class ResultFormSet(ResultFormSetBase):
    def add_fields(self, form, index):
        super(ResultFormSet, self).add_fields(form, index)
        form.fields['is_checked'] = forms.BooleanField(required=False, label='')
