from django import forms


class MovieForm(forms.Form):
    color_choice = (('BW', 'Black and white'), ('CLR', 'Color'),)
    color = forms.ChoiceField(choices=color_choice)

    directory = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    duration_choice = ((1, 'Short'), (2, 'Medium'), (3, 'Long')) #podane w godzinach
    duration = forms.ChoiceField(choices=duration_choice)

    rate_choice = ((2, 'Horrible'), (3, 'Bad'), (5, 'Average'), (7, 'Good'), (9, 'Masterpiece'))
    imdb_score = forms.ChoiceField(choices=rate_choice, label="Quality")

    year_choice = ((1950, 'Very old'), (1970, 'Old'), (1990, 'A little old'), (2005, 'Average'), (2010, 'New'), (2015, 'Very new'))
    year = forms.ChoiceField(choices=year_choice)