'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013

Updated by: Tyler Poel, for lab05 in CS 344, at Calvin University
Date: March 6, 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask, likelihood_weighting, rejection_sampling

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.

# rejection_sampling() and likelihood_weighting() are also approximation algorithms.
print(rejection_sampling('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
print(likelihood_weighting('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

# P(Alarm | burglary ∧ ¬earthquake)
print('5.1 i:  \t' + enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# P(John | burglary ∧ ¬earthquake)
print('5.1 ii: \t' + enumeration_ask('John', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# P(Burglary | alarm)
print('5.1 iii:\t' + enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

'''
Answers to section 5.4 of lab05, for CS 344:
The approximation algorithms give answers that one would expect given their name. They're approximately the right 
answer, but not exactly. These algorithms also don't return the same answer every time, but bounce around in 
proximity to the true answer. This is because these algorithms work using random sampling. Every time they're run, 
they will be computing from a different random sample, which changes the answer. This is also why the answer isn't
exactly the same as the true answer. These algorithms are doing things to decrease the problem space in different
ways, mostly by not using certain probabilities or variables and through sampling, and not computing from the entire
problem space. Because of this the approximation algorithms are always going to give an answer slightly different than
the true answer.
'''