from operator import imod
from django.core import validators
from django import forms


def must_be_empty(value):
    """A custom validator for your honeypot field."""
    if value:
        raise forms.ValidationError('is not empty')


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(
        required=False, widget=forms.HiddenInput, label='Leave empty', validators=[must_be_empty])#validators=[validators.MaxLengthValidator(0)])

    # just a maunal way to valid our honeypot field
    # def clean_honeypot(self):
    #     honeypot = self.cleaned_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError(
    #             'honeypot should be left empty. Bad bot!'
    #     )
    #     return honeypot
