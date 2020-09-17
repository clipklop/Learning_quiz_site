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


class QuestionForm(forms.ModelForm):
    class Media:
        css = {'all': ('courses/css/order.css')}
        js = (
            'courses/js/vendor/jquery.fn.sortable.min.js',
            'courses/js/order.js'
        )


class TrueFalseQuestionForm(QuestionForm):
    class Meta:
        model = models.TrueFalseQuestion
        fields = [
            'order',
            'prompt',
        ]


class MultipleChoiceQuestionForm(QuestionForm):
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = [
            'order',
            'prompt',
            'shuffle_answers'
        ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            'order',
            'text',
            'correct'
        ]


AnswerFormSet = forms.modelformset_factory(
    models.Answer,
    form=AnswerForm,
    extra=2,
)


AnswerInlineFormSet = forms.inlineformset_factory(
    models.Question,
    models.Answer,
    extra=2,
    fields=('order', 'text', 'correct'),
    formset=AnswerFormSet,
    min_num=1,
)
