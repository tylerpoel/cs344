''''
This program models a Bayesian Network, as shown in figure 14.12a of the AIMA textbook

Created by: Tyler Poel, for Homework02 in CS 344, at Calvin University
Date: March 10, 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask, likelihood_weighting, rejection_sampling

# Utility variables
T, F = True, False

weather = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.1, F: 0.5}),
    ('Rain', 'Cloudy', {T: 0.8, F: 0.2}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.9, (F, T): 0.9, (F, F): 0.0})
])


# P(Cloudy)
print('P(Cloudy): ' + enumeration_ask('Cloudy', dict(), weather).show_approx())

# P(Sprinkler | cloudy)
print('P(Sprinkler | cloudy): ' + enumeration_ask('Sprinkler', dict(Cloudy=T), weather).show_approx())

# P(Cloudy| the sprinkler is running and it’s not raining)
print('P(Cloudy | sprinkler ^ ¬rain): ' + enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), weather).show_approx())

# P(WetGrass | it’s cloudy, the sprinkler is running and it’s raining)
print('P(WetGrass | cloudy ^ sprinkler ^ rain): ' + enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T),
                                                                    weather).show_approx())
# P(Cloudy | the grass is not wet)
print('P(Cloudy | ¬WetGrass): ' + enumeration_ask('Cloudy', dict(WetGrass=F), weather).show_approx())
