from django import forms
from django.forms.widgets import NumberInput


class RangeInput(NumberInput):
    input_type = 'range'


class MovieForm(forms.Form):
    color_choice = (('BW', 'Black and white'), ('CLR', 'Color'),)
    color = forms.ChoiceField(choices=color_choice)

    directory = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    duration = forms.DecimalField(widget=RangeInput,
                                    label='Duration: <br>Short <---------> Long')

    imdb_score = forms.DecimalField(widget=RangeInput, label="Quality:<br> Horrible  <---------> Masterpiece")

    year = forms.DecimalField(widget=RangeInput, label="Year of production:<br> Very old  <---------> Very new")
