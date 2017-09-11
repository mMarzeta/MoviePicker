from django.shortcuts import render

from fuzzy.forms import MovieForm
from fuzzy.models import Movie


def user_input(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            output = {}
            output['color'] = form.cleaned_data['color']
            output['directory'] = form.cleaned_data['directory']
            output['duration'] = form.cleaned_data['duration']
            output['imdb_score'] = form.cleaned_data['imdb_score']
            output['year'] = form.cleaned_data['year']
            return render(request, 'result.html', output)
    else:
        form = MovieForm()

    return render(request, 'index.html', {'form': form})
