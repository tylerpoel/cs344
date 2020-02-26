"""
This implements a travelling salesperson problem, which is solved using local search,
    with both AIMA hill-climbing and simulated annealing

Created by: Tyler Poel, for CS344, Homework01, at Calvin University
Date: February 25, 2020
"""

from search import UndirectedGraph, GraphProblem, Problem, hill_climbing, simulated_annealing, exp_schedule
import itertools
import math

TSP_world = UndirectedGraph(dict(
    A=dict(B=1, C=7, D=3),
    B=dict(C=5, D=2),
    C=dict(D=8)))


class TSP(Problem):
    """
    This implements the traveling-sales person problem for local search.
    It requires an undirected graph, with distances between cities.

    State representation:
        [city1, city2, ... , cityn]
        A list of the progression from city to city
    Action representation:

    """
    def __init__(self, initial, graph):
        self.initial = initial
        self.graph = graph
        self.cost = 0

    def actions(self, state):
        """Actions returns a list of possible cities to go to"""

    def result(self, state, action):
        """ header """
        new_state = state[:]
        new_state.append(action[0])

    def value(self, state):
        """ header """





