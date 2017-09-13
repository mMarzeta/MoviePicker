import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


#takes duration, quality, year - returns computed value 0-10
#duration - [0, 15], as well as quality and year.
#gaussian functions to be modified i guess.
def fuzzyfy(duration, quality, year):
    fuz_duration = ctrl.Antecedent(np.arange(0, 16, 0.001), 'duration')
    fuz_quality = ctrl.Antecedent(np.arange(0, 16, 0.001), 'quality')
    fuz_year = ctrl.Antecedent(np.arange(0, 16, 0.001), 'year')

    fuz_output = ctrl.Consequent(np.arange(0, 11, 0.001), 'movie rank')

    #assigning membership functions
    fuz_duration['short'] = fuzz.gaussmf(fuz_duration.universe, 2.5, 2.5)
    fuz_duration['medium'] = fuzz.gaussmf(fuz_duration.universe, 7.5, 2.5)
    fuz_duration['long'] = fuzz.gaussmf(fuz_duration.universe, 12.5, 2.5)

    fuz_quality['horrible'] = fuzz.gaussmf(fuz_quality.universe, 2., 1.)
    fuz_quality['bad'] = fuzz.gaussmf(fuz_quality.universe, 4., 1.)
    fuz_quality['average'] = fuzz.gaussmf(fuz_quality.universe, 6., 1.)
    fuz_quality['good'] = fuzz.gaussmf(fuz_quality.universe, 8., 1.)
    fuz_quality['masterpiece'] = fuzz.gaussmf(fuz_quality.universe, 13., 2.)

    fuz_year['verry old'] = fuzz.gaussmf(fuz_year.universe, 2., 1.)
    fuz_year['old'] = fuzz.gaussmf(fuz_year.universe, 5., 1.5)
    fuz_year['average'] = fuzz.gaussmf(fuz_year.universe, 8., 1.)
    fuz_year['new'] = fuzz.gaussmf(fuz_year.universe, 10., 1.)
    fuz_year['verry new'] = fuzz.gaussmf(fuz_year.universe, 13., 2.)


    fuz_output.automf(number=3, names=['poor', 'good', 'masterpiece'])

    #rule set
    rule1 = ctrl.Rule(fuz_duration['short'] & (fuz_quality['horrible'] | fuz_quality['bad']), fuz_output['poor'])
    rule2 = ctrl.Rule(fuz_quality['average'] | fuz_quality['good'], fuz_output['good'])
    rule3 = ctrl.Rule(fuz_quality['masterpiece'] & fuz_duration['long'], fuz_output['masterpiece'])
    rule4 = ctrl.Rule((fuz_year['verry old'] | fuz_year['old']) & (fuz_quality['horrible'] | fuz_quality['bad']), fuz_output['poor'] )

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

