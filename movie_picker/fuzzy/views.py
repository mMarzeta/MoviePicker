from django.shortcuts import render

from movie_picker.fuzzy.forms import MovieForm


def user_input(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            output = {}
            output['color'] = form.cleaned_data['color']
            output['directory'] = form.cleaned_data['directory']
            output['duration'] =  round(form.cleaned_data['duration'] / 100 * 15, 4)
            output['imdb_score'] = round(form.cleaned_data['imdb_score'] / 100 * 15, 4)
            output['year'] = round(form.cleaned_data['year'] / 100 * 15, 4)
            return render(request, 'result.html', output)
    else:
        form = MovieForm()

    return render(request, 'index.html', {'form': form})
