from django.shortcuts import render

from fuzzy.forms import MovieForm
from fuzzy.models import Movie


def user_input(request):
    if request.method == "POST":
        print('chuj')
        form = MovieForm(request.POST)
        if form.is_valid():
            print('dupa')
            movie = Movie.objects.create(color=request.color,
                                         directory=request.directory,
                                         country=request.country,
                                         duration=request.duration,
                                         imdb_score=request.imdb_score,
                                         year=request.year)
            movie.save()
            return render(request, 'templates/result.html', {'movie', movie})
    else:
        form = MovieForm()

    return render(request, 'index.html', {'form': form})
