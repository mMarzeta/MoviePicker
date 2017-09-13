import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


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

    fuz_year['verry old'] = fuzz.gaussmf(fuz_year.universe, 0, 1.5)
    fuz_year['old'] = fuzz.gaussmf(fuz_year.universe, 3.5, 1.5)
    fuz_year['average'] = fuzz.gaussmf(fuz_year.universe, 7., 1.5)
    fuz_year['new'] = fuzz.gaussmf(fuz_year.universe, 10.5, 1.5)
    fuz_year['verry new'] = fuzz.gaussmf(fuz_year.universe, 15., 2)

    fuz_output['poor'] = fuzz.gaussmf(fuz_output.universe, 0, 2.5)
    fuz_output['good'] = fuzz.gaussmf(fuz_output.universe, 5, 2.5)
    fuz_output['masterpiece'] = fuzz.gaussmf(fuz_output.universe, 10, 2.5)

    #rule set
    rules1 = ctrl.Rule(fuz_duration['short'] & (fuz_quality['horrible'] | fuz_quality['bad'] | fuz_quality['average']), fuz_output['poor'])
    rules2 = ctrl.Rule(fuz_duration['short'] & fuz_quality['good'] & (fuz_year['verry old'] | fuz_year['old']), fuz_output['poor'])
    rules3 = ctrl.Rule(fuz_duration['short'] & fuz_quality['good'] & (fuz_year['average'] | fuz_year['new'] | fuz_year['verry new']), fuz_output['good'])
    rules4 = ctrl.Rule(fuz_duration['short'] & fuz_quality['masterpiece'] & (fuz_year['verry old'] | fuz_year['old'] | fuz_year['average'] | fuz_year['new']), fuz_output['good'])
    rules5 = ctrl.Rule(fuz_duration['short'] & fuz_quality['masterpiece'] & fuz_year['verry new'], fuz_output['masterpiece'])

    rulem1 = ctrl.Rule(fuz_duration['medium'] & (fuz_quality['horrible'] | fuz_quality['bad']), fuz_output['poor'])
    rulem2 = ctrl.Rule(fuz_duration['medium'] & fuz_quality['average'] & (fuz_year['verry old'] | fuz_year['old'] | fuz_year['average']), fuz_output['poor'])
    rulem3 = ctrl.Rule(fuz_duration['medium'] & fuz_quality['average'] & (fuz_year['new'] | fuz_year['verry new']), fuz_output['good'])
    rulem4 = ctrl.Rule(fuz_duration['medium'] & fuz_quality['good'], fuz_output['good'])
    rulem5 = ctrl.Rule(fuz_duration['medium'] & fuz_quality['masterpiece'] & (fuz_year['verry old'] | fuz_year['old'] | fuz_year['average']), fuz_output['good'])
    rulem6 = ctrl.Rule(fuz_duration['medium'] & fuz_quality['masterpiece'] & (fuz_year['new'] | fuz_year['verry new']), fuz_output['masterpiece'])

    #control system
    movie_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    picker = ctrl.ControlSystemSimulation(movie_ctrl)

    #symulation
    picker.input['duration'] = duration
    picker.input['quality'] = quality
    picker.input['year'] = year

    picker.compute()

    #shows output space
    fuz_output.view(sim=picker)

    return picker.output['movie rank']

