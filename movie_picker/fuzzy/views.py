from django.shortcuts import render

from movie_picker.fuzzy.forms import Movies
from movie_picker.fuzzy.forms import MovieForm
from movie_picker.fuzzy.fuzzy_logic import fuzzyfy


def user_input(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            result = {}
            result['genre'] = form.cleaned_data['genre']
            duration = form.cleaned_data['duration'] / 100 * 15
            imdb_score = form.cleaned_data['imdb_score'] / 100 * 15
            year = form.cleaned_data['year'] / 100 * 15

            result['result'] = fuzzyfy(duration, imdb_score, year)
            result['queryset'] = Movies.objects.all()[1:10]

            return render(request, 'result.html', result)
    else:
        form = MovieForm()

    return render(request, 'index.html', {'form': form})
