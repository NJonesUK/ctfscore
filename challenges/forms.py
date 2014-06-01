from django import forms

class AnswerForm(forms.Form):
    """
    Form used to process answers to challenges
    """
    answer = forms.CharField(max_length=200)