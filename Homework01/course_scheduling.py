"""

Created by: Tyler Poel, for CS344, Homework01, at Calvin University
Date: February 27, 2020
"""

from csp import CSP,  min_conflicts, backtracking_search, AC3, parse_neighbors
from search import depth_first_graph_search

def schedule():
    """Header"""
    classes = 'cs108 cs112 cs214 cs374 cs344 cs212'.split()
    faculty = 'Schuurman Adams Vanderlinden Plantinga'.split()
    times = 'mwf9 mwf10 mwf11 mwf12'.split()
    rooms = 'nh253 sb382'.split()

    domains = {}
    for course in classes:
        domains[course] = [faculty, times, rooms]

    neighbors = {}
    for course in classes:
        neighbors[course] = classes

    def schedule_constraint(A, a, B, b):
        if A == 'cs108' and a != 'Vanderlinden':
            return False
        if B == 'cs108' and b != 'Vanderlinden':
            return False
        if A == 'cs344' and a != 'Vanderlinden':
            return False
        if B == 'cs344' and b != 'Vanderlinden':
            return False
        if A == 'cs374' and a != 'Adams':
            return False
        if B == 'cs374' and b != 'Adams':
            return False
        if A == 'cs112' and a != 'Adams':
            return False
        if B == 'cs112' and b != 'Adams':
            return False
        if A == 'cs212' and a != 'Plantinga':
            return False
        if B == 'cs212' and b != 'Plantinga':
            return False
        if A == 'cs214' and a != 'Schuurman':
            return False
        if B == 'cs214' and b != 'Schuurman':
            return False


    return CSP(classes, domains, neighbors, schedule_constraint)


if __name__ == '__main__':
    domains = {}
    classes = 'cs108 cs112 cs214 cs374 cs344 cs212'.split()
    faculty = 'Schuurman Adams Vanderlinden Plantinga'.split()
    times = 'mwf9 mwf10 mwf11 mwf12'.split()
    rooms = 'nh253 sb382'.split()
    for course in classes:
        domains[course] = rooms + times

    domains['cs108'] = 'Vanderlinden'

    neighbors = {}
    for course in classes:
        neighbors[course] = classes
    # for course in classes:
    #     for A in classes:
    #         if A != course:
    #             if course not in neighbors:
    #                 neighbors[course].append(A)

    print(neighbors.items())

