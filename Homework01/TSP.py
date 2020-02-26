"""
This implements a travelling-sales person problem, which is solved using local search,
    with both AIMA hill-climbing and simulated annealing

Created by: Tyler Poel, for CS344, Homework01, at Calvin University
Date: February 25, 2020
"""

from search import UndirectedGraph, GraphProblem, Problem, hill_climbing, simulated_annealing, exp_schedule
import itertools
import math

TSP_world = UndirectedGraph(dict(
    Boston=dict(NewYork=10, LA=3, GrandRapids=2),
    NewYork=dict(LA=7, Chicago=5),
    Chicago=dict(LA=12, Detroit=4),
    Detroit=dict(LA=15, GrandRapids=7),
    GrandRapids=dict(LA=5)))


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






