"""

Created by: Tyler Poel, for CS344, Homework01, at Calvin University
Date: February 27, 2020
"""

from csp import min_conflicts, backtracking_search, AC3, parse_neighbors
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

        return 0



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

