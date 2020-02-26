"""
This implements a travelling salesperson problem, which is solved using local search,
    with both AIMA hill-climbing and simulated annealing

Created by: Tyler Poel, for CS344, Homework01, at Calvin University
Date: February 25, 2020
"""

from search import UndirectedGraph, Problem, hill_climbing, simulated_annealing, exp_schedule
import random

# Uses an undirected graph to create the "world" in which our problem resides.
TSP_world = UndirectedGraph(dict(
    A=dict(B=1, C=7, D=3, E=6, F=22),
    B=dict(C=5, D=2, E=14, F=3),
    C=dict(D=8, E=12, F=15),
    D=dict(E=10, F=25),
    E=dict(F=20)))

romania = UndirectedGraph(dict(
    arad=dict(zerind=75, sibiu=140, timisoara=118),
    bucharest=dict(urziceni=85, pitesti=101, giurgiu=90, fagaras=211),
    craiova=dict(dobreta=120, rimnicuvilcea=146, pitesti=138),
    dobreta=dict(mehadia=75),
    eforie=dict(hirsova=86),
    fagaras=dict(sibiu=99),
    hirsova=dict(urziceni=98),
    iasi=dict(vaslui=92, neamt=87),
    lugoj=dict(timisoara=111, mehadia=70),
    oradea=dict(zerind=71, sibiu=151),
    pitesti=dict(rimnicuvilcea=97),
    rimnicuvilcea=dict(sibiu=80),
    urziceni=dict(vaslui=142)))


def interconnect(graph):
    """Interconnect takes a graph and makes it interconnected, connecting each node to every other node"""
    cities = graph.nodes()
    for x in range(len(cities)):
        for y in range(len(cities)):
            if graph.get(cities[x], cities[y]) == None:
                graph.connect(cities[x], cities[y])


class TSP(Problem):
    """
    This implements the traveling-sales person problem for local search.
    It requires an undirected graph, with distances between cities.

    State representation:
        [city1, city2, ... , cityn]
        A list of the progression from city to city
    Action representation:
        [index1, index2]
        The index spots of the cities to be swapped in the route order
    """
    def __init__(self, initial, graph):
        self.initial = initial
        self.graph = graph

    def actions(self, state):
        """Actions swaps two cities in the route list"""
        rand = random.randrange(0, len(state), 1)
        rand2 = random.randrange(0, len(state), 1)
        actions = [[rand, rand2]]
        return actions

    def result(self, state, action):
        """Makes the given action on a copy of the board"""
        new_state = state[:]
        temp = new_state[action[0]]
        new_state[action[0]] = new_state[action[1]]
        new_state[action[1]] = temp
        return new_state

    def goal_test(self, state):
        """Checks to see if every city was visited, and if the start and end city are the same"""
        # Get list of all cities
        cities = self.graph.nodes()
        # Check to see if each city is in the given state
        for iter in range(len(cities)):
            if cities[iter] not in state:
                return False

        # Make sure the start and end cities are the same
        if state[0] != state[-1]:
            return False

        return True

    def value(self, state):
        """Adds up the cost of the path for the given state"""
        cost = 0
        for index in range(len(state) - 1):
            if state[index] == state[index+1]: cost += 0
            else:
                cost += self.graph.get(state[index], state[index+1])
        return cost * -1


if __name__ == '__main__':
    # Initial route for very simple tsp world
    tsp_route = ['D', 'C', 'A', 'B','F', 'D']

    # Initial route for more complicated romania world
    interconnect(romania)
    romania_route = romania.nodes()
    # Make initial state start and end at the same city
    romania_route.append(romania_route[0])

    # create the problems
    # romania world: TSP(romania_route, romania)
    # tsp world: TSP(tsp_route, TSP_world)
    p = TSP(tsp_route, TSP_world)

    # Try solving the problem with hill climbing
    hill_solution = hill_climbing(p)
    print('\nHill-climbing:')
    print('\tSolution:\t' + str(hill_solution))
    print('\tValue:\t\t' + str(p.value(hill_solution)))
    print('\tGoal?\t\t' + str(p.goal_test(hill_solution)))

    # Try solving the problem with simulated annealing
    annealing_solution = \
        simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=10000))
    print('\nSimulated annealing:')
    print('\tSolution:\t' + str(annealing_solution))
    print('\tValue:\t\t' + str(p.value(annealing_solution)))
    print('\tGoal?\t\t' + str(p.goal_test(annealing_solution)))