"""
This module implements local search on a sine function variant.
The function is a sin wave that grows larger from 0 to 30.

Created by: Tyler Poel, for CS344, lab02, at Calvin University
Date: February 14, 2020

Updated from given abs value function code:
@author: kvlinden
@version 6feb2013
"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class SineVariant(Problem):
    """
    State: x value for the sine function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':

    # Formulate a problem with a 2D sine function and a single maximum value.
    maximum = 30
    initial = randrange(0, maximum)
    p = SineVariant(initial, maximum, delta=1.0)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing, with random restarts
    hill_solution = hill_climbing(p)

    # simulates 20 random restarts
    best_val = 0
    best_x = 0
    for x in range(0, 20):
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.0)
        hill_solution = hill_climbing(p)
        if p.value(hill_solution) > best_val:
            best_val = p.value(hill_solution)
            best_x = hill_solution

    print('Hill-climbing solution       x: ' + str(best_x)
          + '\tvalue: ' + str(best_val)
          )

    # Solve the problem using simulated annealing.
    annealing_solution = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=1000)
    )

    # simulates 20 random restarts
    best_val = 0
    best_x = 0
    for x in range(0, 20):
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.0)
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        if p.value(annealing_solution) > best_val:
            best_val = p.value(annealing_solution)
            best_x = annealing_solution

    print('Simulated annealing solution x: ' + str(best_x)
          + '\tvalue: ' + str(best_val)
          )
