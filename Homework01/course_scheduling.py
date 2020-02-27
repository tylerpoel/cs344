"""
Uses the CSP set-up to create a schedule constraint problem.
Classes are the variables, and the different faculty, class times, and classrooms are values that
    the classes can take on.

Created by: Tyler Poel, for CS344, Homework01, at Calvin University
Date: February 27, 2020
"""

from csp import CSP,  min_conflicts, backtracking_search, AC3, parse_neighbors
from search import depth_first_graph_search

def schedule():
    """CSP set-up for a class scheduling problem."""

    classes = 'cs108 cs112 cs214 cs374 cs344 cs212'.split()
    faculty = 'Schuurman Adams Vanderlinden Plantinga'.split()
    times = 'mwf9 mwf10 mwf11 mwf12'.split()
    rooms = 'nh253 sb382'.split()

    # create every [professor, time, room] combo
    combo = [0] * 32
    i = 0
    for x in range(len(faculty)):
        for y in range(len(times)):
            for z in range(len(rooms)):
                combo[i] = [faculty[x], times[y], rooms[z]]
                i += 1

    # Each class gets every single combination
    domains = {}
    for course in classes:
        domains[course] = combo

    # Everyone is a neighbor with everyone but themselves
    neighbors = parse_neighbors("""
            cs108: cs112 cs214 cs374 cs344 cs212;
            cs112: cs214 cs374 cs344 cs212;
            cs214: cs374 cs344 cs212;
            cs374: cs344 cs212;
            cs344: cs212;
            cs212: """)

    def schedule_constraint(A, a, B, b):
        """Codes the constraints the problem must follow"""
        # There can only be one instance of a class
        if A == B:
            return False

        # Certain professors only teach certain classes
        if A == 'cs108' and a[0] != 'Vanderlinden':
            return False
        if B == 'cs108' and b[0] != 'Vanderlinden':
            return False
        if A == 'cs344' and a[0] != 'Vanderlinden':
            return False
        if B == 'cs344' and b[0] != 'Vanderlinden':
            return False
        if A == 'cs374' and a[0] != 'Adams':
            return False
        if B == 'cs374' and b[0] != 'Adams':
            return False
        if A == 'cs112' and a[0] != 'Adams':
            return False
        if B == 'cs112' and b[0] != 'Adams':
            return False
        if A == 'cs212' and a[0] != 'Plantinga':
            return False
        if B == 'cs212' and b[0] != 'Plantinga':
            return False
        if A == 'cs214' and a[0] != 'Schuurman':
            return False
        if B == 'cs214' and b[0] != 'Schuurman':
            return False

        # a professor cannot teach two classes at the same time
        if a[0] == b[0] and a[1] == b[1]:
            return False
        # Two classes cannot be in the same room at the same time
        if a[1] == b[1] and a[2] == b[2]:
            return False

        return True

    return CSP(classes, domains, neighbors, schedule_constraint)


result = min_conflicts(schedule(), max_steps=1000)

if result is None:
    print("No solution found")
else:
    print("Solution!")
    print(result)