from django import forms


class MovieForm(forms.Form):
    color_choice = (('BW', 'Black and white'), ('CLR', 'COLOR'),)
    color = forms.ChoiceField(choices=color_choice)
    directory = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    duration = forms.DecimalField(max_digits=4, decimal_places=1)
    imdb_score = forms.DecimalField(max_digits=3, decimal_places=1)
    year = forms.IntegerField()