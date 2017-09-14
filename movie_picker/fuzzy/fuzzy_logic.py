import matplotlib
matplotlib.use('Agg')
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from movie_picker.fuzzy.models import Movies
from django.db.models import Q


#takes duration, quality, year - returns computed value 0-10
#duration - [0, 15], as well as quality and year.
#gaussian functions to be modified i guess.
def fuzzyfy(duration, quality, year):
    fuz_duration = ctrl.Antecedent(np.arange(0, 15, 0.001), 'duration')
    fuz_quality = ctrl.Antecedent(np.arange(0, 15, 0.001), 'quality')
    fuz_year = ctrl.Antecedent(np.arange(0, 15, 0.001), 'year')

    fuz_output = ctrl.Consequent(np.arange(0, 10, 0.001), 'movie rank')

    #assigning membership functions
    fuz_duration['short'] = fuzz.gaussmf(fuz_duration.universe, 0, 5)
    fuz_duration['medium'] = fuzz.gaussmf(fuz_duration.universe, 7.5, 2.5)
    fuz_duration['long'] = fuzz.gaussmf(fuz_duration.universe, 15, 5)

    fuz_quality['horrible'] = fuzz.gaussmf(fuz_quality.universe, 0, 1.5)
    fuz_quality['bad'] = fuzz.gaussmf(fuz_quality.universe, 3.5, 1.5)
    fuz_quality['average'] = fuzz.gaussmf(fuz_quality.universe, 7, 1.5)
    fuz_quality['good'] = fuzz.gaussmf(fuz_quality.universe, 10.5, 1.5)
    fuz_quality['masterpiece'] = fuzz.gaussmf(fuz_quality.universe, 15, 2)

    fuz_year['very old'] = fuzz.gaussmf(fuz_year.universe, 0, 1.5)
    fuz_year['old'] = fuzz.gaussmf(fuz_year.universe, 3.5, 1.5)
    fuz_year['average'] = fuzz.gaussmf(fuz_year.universe, 7., 1.5)
    fuz_year['new'] = fuzz.gaussmf(fuz_year.universe, 10.5, 1.5)
    fuz_year['very new'] = fuzz.gaussmf(fuz_year.universe, 15., 2)

    fuz_output['poor'] = fuzz.gaussmf(fuz_output.universe, 0, 2.5)
    fuz_output['good'] = fuzz.gaussmf(fuz_output.universe, 5, 2.5)
    fuz_output['masterpiece'] = fuzz.gaussmf(fuz_output.universe, 10, 2.5)

    #rule set
    rules1 = ctrl.Rule(fuz_duration['short'] & (fuz_quality['horrible'] | fuz_quality['bad'] | fuz_quality['average']), fuz_output['poor'])
    rules2 = ctrl.Rule(fuz_duration['short'] & fuz_quality['good'] & (fuz_year['very old'] | fuz_year['old']), fuz_output['poor'])
    rules3 = ctrl.Rule(fuz_duration['short'] & fuz_quality['good'] & (fuz_year['average'] | fuz_year['new'] | fuz_year['very new']), fuz_output['good'])
    rules4 = ctrl.Rule(fuz_duration['short'] & fuz_quality['masterpiece'] & (fuz_year['very old'] | fuz_year['old'] | fuz_year['average'] | fuz_year['new']), fuz_output['good'])
    rules5 = ctrl.Rule(fuz_duration['short'] & fuz_quality['masterpiece'] & fuz_year['very new'], fuz_output['masterpiece'])

    rulem1 = ctrl.Rule(fuz_duration['medium'] & (fuz_quality['horrible'] | fuz_quality['bad']), fuz_output['poor'])
    rulem2 = ctrl.Rule(fuz_duration['medium'] & fuz_quality['average'] & (fuz_year['very old'] | fuz_year['old'] | fuz_year['average']), fuz_output['poor'])
    rulem3 = ctrl.Rule(fuz_duration['medium'] & fuz_quality['average'] & (fuz_year['new'] | fuz_year['very new']), fuz_output['good'])
    rulem4 = ctrl.Rule(fuz_duration['medium'] & fuz_quality['good'], fuz_output['good'])
    rulem5 = ctrl.Rule(fuz_duration['medium'] & fuz_quality['masterpiece'] & (fuz_year['very old'] | fuz_year['old'] | fuz_year['average']), fuz_output['good'])
    rulem6 = ctrl.Rule(fuz_duration['medium'] & fuz_quality['masterpiece'] & (fuz_year['new'] | fuz_year['very new']), fuz_output['masterpiece'])

    # dla long
    tmp_quality = ['horrible', 'bad', 'average', 'good', 'masterpiece']
    tmp_year = ['very old', 'old', 'average', 'new', 'very new']
    rules_l = []

    # dla horrible i bad i wszystkich lat
    for i in range(2):
        for j in range(5):
            rules_l.append(ctrl.Rule(fuz_duration['long'] & fuz_quality[tmp_quality[i]] & fuz_year[tmp_year[j]], fuz_output['poor']))

    # dla average w latach very old, old, average
    for i in range(3):
        rules_l.append(ctrl.Rule(fuz_duration['long'] & fuz_quality['average'] & fuz_year[tmp_year[i]], fuz_output['poor']))
    rules_l.append(ctrl.Rule(fuz_duration['long'] & fuz_quality['average'] & fuz_year['new'], fuz_output['good']))
    rules_l.append(ctrl.Rule(fuz_duration['long'] & fuz_quality['average'] & fuz_year['very new'], fuz_output['good']))

    # dla good w latach od very_old do new
    for i in range(4):
        rules_l.append(ctrl.Rule(fuz_duration['long'] & fuz_quality['good'] & fuz_year[tmp_year[i]], fuz_output['good']))
    rules_l.append(ctrl.Rule(fuz_duration['long'] & fuz_quality['good'] & fuz_year['very new'], fuz_output['masterpiece']))

    # dla masterpiece w latach very old do average
    for i in range(3):
        rules_l.append(ctrl.Rule(fuz_duration['long'] & fuz_quality['masterpiece'] & fuz_year[tmp_year[i]], fuz_output['good']))
    rules_l.append(ctrl.Rule(fuz_duration['long'] & fuz_quality['masterpiece'] & fuz_year['new'], fuz_output['masterpiece']))
    rules_l.append(ctrl.Rule(fuz_duration['long'] & fuz_quality['masterpiece'] & fuz_year['very new'], fuz_output['masterpiece']))

    #create list from all rules.
    all_rules = [rules1, rules2, rules3, rules4, rules5, rulem1, rulem2, rulem3, rulem4, rulem5, rulem6]

    for rule in rules_l:
        all_rules.append(rule)

    #control system
    movie_ctrl = ctrl.ControlSystem(all_rules)
    picker = ctrl.ControlSystemSimulation(movie_ctrl)

    #symulation
    picker.input['duration'] = duration
    picker.input['quality'] = quality
    picker.input['year'] = year

    picker.compute()

    return picker.output['movie rank']

def actualise_fuzzy_movie_rank_db():
    records = Movies.objects.count()
    for i in range(1, 5000):
        try:
            movie = Movies.objects.get(id=i)
            movie.fuzzy_movie_rank = fuzzyfy(scale_duration(movie.duration), scale_quality(movie.imdb_score), scale_year(movie.title_year))
            movie.save()
            print(i)
        except Exception:
            print('no such id', i, sep=' ')

def scale_duration(duration):
    duration = float(duration)
    return 15./504. * duration - 5./24.

def scale_quality(quality):
    quality = float(quality)
    return 150./79. * quality - 240./79.

def scale_year(year):
    year = float(year)
    return 1./7. * year - 273.

def query_records_around_result(range, result, genre):
    records = []
    for record in Movies.objects.all():
        if record.fuzzy_movie_rank >= result-range and record.fuzzy_movie_rank <= result+range and record.genres.__contains__(genre):
            records.append(record)
    return records

