from django import forms
from django.forms.widgets import NumberInput

from movie_picker.fuzzy.models import Movies


class RangeInput(NumberInput):
    input_type = 'range'


class MovieForm(forms.Form):
    choices = (('Mystery', 'Mystery'),
               ('Horror', 'Horror'),
               ('Short', 'Short'),
               ('Sport', 'Sport'),
               ('Drama', 'Drama'),
               ('Musical', 'Musical'),
               ('History', 'History'),
               ('War', 'War'),
               ('Animation', 'Animation'),
               ('Family', 'Family'),
               ('Romance', 'Romance'),
               ('Western', 'Western'),
               ('Crime', 'Crime'),
               ('Action', 'Action'),
               ('Film-Noir', 'Film-Noir'),
               ('Thriller', 'Thriller'),
               ('News', 'News'),
               ('Adventure', 'Adventure'),
               ('Documentary', 'Documentary'),
               ('Game-Show', 'Game-Show'),
               ('Sci-Fi', 'Sci-Fi'),
               ('Comedy', 'Comedy'),
               ('Fantasy', 'Fantasy'),
               ('Reality-TV', 'Reality-TV'),
               ('Music', 'Music'),
               ('Biography', 'Biography'),
               )

    genre = forms.ChoiceField(choices=choices)

    duration = forms.FloatField(widget=RangeInput,
                                  label='Duration: <br>Short <---------> Long')

    imdb_score = forms.FloatField(widget=RangeInput, label="Quality:<br> Horrible  <---------> Masterpiece")

    year = forms.FloatField(widget=RangeInput, label="Year of production:<br> Very old  <---------> Very new")
