from django.forms.fields import MultipleChoiceField
from django.db.models import fields
from django import forms

from . import models


class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',
            'order',
            'total_questions',
        ]

        # so basically you could just exclude the fields you don't want to be displayed
        # and all other attributes of your form model would be displayed in a form
        # but it's considering a bad practice because "explicit is better than implicit"
        # yes, exclude is faster, but it's also dangerous
        # any attributes to your model would be automatically added to your displayed form

        # exclude = [
        #     'course',
        # ]


class TrueFalseQuestionForm(forms.ModelForm):
    class Meta:
        model = models.TrueFalseQuestion
        fields = [
            'order',
            'prompt',
        ]


class MultipleChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = [
            'order',
            'prompt',
            'shuffle_answers'
        ]
