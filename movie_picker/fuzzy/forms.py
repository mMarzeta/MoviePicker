from django import forms

class UserChoices(forms.Form):
    color_choice = [('Black and white', 'Color')]
    color = forms.ChoiceField(choices=color_choice)