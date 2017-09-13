import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# takes duration, quality, year - returns computed value 0-10
# duration - [0, 15], as well as quality and year.
# gaussian functions to be modified i guess.
def fuzzyfy(duration, quality, year):
    fuz_duration = ctrl.Antecedent(np.arange(0, 16, 0.001), 'duration')
    fuz_quality = ctrl.Antecedent(np.arange(0, 16, 0.001), 'quality')
    fuz_year = ctrl.Antecedent(np.arange(0, 16, 0.001), 'year')

    fuz_output = ctrl.Consequent(np.arange(0, 11, 0.001), 'movie rank')

    # assigning membership functions
    fuz_duration['short'] = fuzz.gaussmf(fuz_duration.universe, 2.5, 2.5)
    fuz_duration['medium'] = fuzz.gaussmf(fuz_duration.universe, 7.5, 2.5)
    fuz_duration['long'] = fuzz.gaussmf(fuz_duration.universe, 12.5, 2.5)

    fuz_quality['horrible'] = fuzz.gaussmf(fuz_quality.universe, 2., 1.)
    fuz_quality['bad'] = fuzz.gaussmf(fuz_quality.universe, 4., 1.)
    fuz_quality['average'] = fuzz.gaussmf(fuz_quality.universe, 6., 1.)
    fuz_quality['good'] = fuzz.gaussmf(fuz_quality.universe, 8., 1.)
    fuz_quality['masterpiece'] = fuzz.gaussmf(fuz_quality.universe, 13., 2.)

    fuz_year['very old'] = fuzz.gaussmf(fuz_year.universe, 2., 1.)
    fuz_year['old'] = fuzz.gaussmf(fuz_year.universe, 5., 1.5)
    fuz_year['average'] = fuzz.gaussmf(fuz_year.universe, 8., 1.)
    fuz_year['new'] = fuzz.gaussmf(fuz_year.universe, 10., 1.)
    fuz_year['very new'] = fuzz.gaussmf(fuz_year.universe, 13., 2.)

    fuz_output.automf(number=3, names=['poor', 'good', 'masterpiece'])

    # rule set
    rule1 = ctrl.Rule(fuz_duration['short'] & (fuz_quality['horrible'] | fuz_quality['bad']), fuz_output['poor'])
    rule2 = ctrl.Rule(fuz_quality['average'] | fuz_quality['good'], fuz_output['good'])
    rule3 = ctrl.Rule(fuz_quality['masterpiece'] & fuz_duration['long'], fuz_output['masterpiece'])
    rule4 = ctrl.Rule((fuz_year['very old'] | fuz_year['old']) & (fuz_quality['horrible'] | fuz_quality['bad']),
                      fuz_output['poor'])


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

    # control system
    rules_l.append(rule1)
    rules_l.append(rule2)
    rules_l.append(rule3)
    rules_l.append(rule4)

    movie_ctrl = ctrl.ControlSystem(rules_l)
    picker = ctrl.ControlSystemSimulation(movie_ctrl)

    # symulation
    picker.input['duration'] = duration
    picker.input['quality'] = quality
    picker.input['year'] = year

    picker.compute()

    # shows output space
    fuz_output.view(sim=picker)

    return picker.output['movie rank']
