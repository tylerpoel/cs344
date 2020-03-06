'''
This implements a Bayesian network that represents a happiness domain.
This answers questions to 5.3 in lab05 for CS 344

Created by: Tyler Poel, for lab05 in CS 344 at Calvin University
Date: March 6, 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
])

# P(Raise | sunny)
print("5.3 ai: \t" + enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
# P(Raise | happy ^ sunny)
print("5.3 aii:\t" + enumeration_ask('Raise', dict(Sunny=T, Happy=T), happiness).show_approx())
'''
Hand Calculations:
5.3 ai.
    P(Raise | Sunny) - confounding variable Happy
    = α Σ P( R, S, H)
    = α Σ P(R) * P(S) * P(H | R, S)
    = α < P(R) * P(S) * (P(H) + P(not H)), P(not R) * P(S) * (P(H) + P(not H)) >
    = α <0.007, 0.093>
    = <0.01, 0.99>
    
'''

# P(Raise | happy)
print("5.3 bi: \t" + enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
# P(Raise | happy ^ ¬sunny)
print("5.3 bii:\t" + enumeration_ask('Raise', dict(Sunny=F, Happy=T), happiness).show_approx())
