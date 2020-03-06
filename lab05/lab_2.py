'''
This implements a Bayesian network that represents a cancer domain.
This answers questions to part 5.2 of lab05 for CS 344.

Created by: Tyler Poel, for lab05 in CS 344 at Calvin University
Date: March 6, 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

# P(Cancer | positive result on both tests)
print("5.2 i:\t" + enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
# P(Cancer | a positive result on test 1, but a negative result on test 2)
print("5.2 ii:\t" + enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

'''
I'm slightly surprised by these answers. I thought that if both tests were positive there would be a high probability
of having cancer. However the True probability is only 0.17. I think the reason for this lies in the fact that 
the initial probability of cancer is alone is  only 0.01, so even with two positive tests the odds of having cancer
will be low. 
The effect of one failed test drastically lowers the chances of having cancer. With both tests being positive
the probability was 0.17, but after one test being negative the chances are dropped to 0.00565.

Hand Calculations:
5.2 i:
    P(C | T1, T2)
    = α P(C, T1, T2)
    = α P(C) * P(T1 | C) * P(T2 | C)
    = α <0.01 * 0.9 * 0.9, 0.99 * 0.2 * 0.2>
    = α <0.0081, 0.0396>
    = <0.17, 0.83>

5.2 ii:
    P(C | T1, not T2)
    = α P(C, T1, not T2)
    = α P(C) * P(T1 | C) * P(not T2 | C)
    = α <0.01 * 0.9 * 0.1, 0.99 * 0.2 * 0.8>
    = α <0.0009, 0.1584>
    = <0.00565, 0.994>
'''
