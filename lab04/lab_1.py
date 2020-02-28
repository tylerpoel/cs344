'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013

Updated by: Tyler Poel, for CS 344, lab04, at Calvin University
Date: February 28, 2020

Exercise 4.1b (hand calculation):
P(Cavity|catch) = P(Cavity ^ Catch) / P(catch) = 0.18 / 0.34 = 0.529
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print('P(Cavity|Toothache=T):\t' + PC.show_approx())

# Compute P(Cavity|catch). Should match calculation in header comments.
PC1 = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print('P(Cavity|catch):\t' + PC1.show_approx())

# Joint Probability Distribution for two coin flips
P1 = JointProbDist(['Coin1', 'Coin2'])
H, T = 'heads', 'tails'
P1[H, H] = 0.25; P1[H, T] = 0.25
P1[T, T] = 0.25; P1[T, H] = 0.25

# Compute P(Coin2|coin1=heads)
PC2 = enumerate_joint_ask('Coin2', {'Coin1': H}, P1)
print('P(Coin2|coin1=heads):\t' + PC2.show_approx())
"""This answer aligns with what I already thought to be true about flipping coins. It shows how the 
    events of one coin flip do not affect the probability of another coin flips outcome. Two coin flips
    are independent of each other. There is also only ever one outcome for a coin flip: heads or tails,
    with a 50% chance of either happening."""

"""Full joint isn't generally used, because after one adds more dimensions, and moves away from this simple
    problem space, the probability calculations quickly become very hard, and not practically worth it. To 
    simulate real world probabilities and events one needs a lot of different dimensions, and this exceeds 
    the helpfulness of a full joint distribution."""
