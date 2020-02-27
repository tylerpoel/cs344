"""

Created by: Tyler Poel, for CS344, Homework01, at Calvin University
Date: February 27, 2020
# if A == 'cs108' and a != 'Vanderlinden':
        #     return False
        # if B == 'cs108' and b != 'Vanderlinden':
        #     return False
        # if A == 'cs344' and a != 'Vanderlinden':
        #     return False
        # if B == 'cs344' and b != 'Vanderlinden':
        #     return False
        # if A == 'cs374' and a != 'Adams':
        #     return False
        # if B == 'cs374' and b != 'Adams':
        #     return False
        # if A == 'cs112' and a != 'Adams':
        #     return False
        # if B == 'cs112' and b != 'Adams':
        #     return False
        # if A == 'cs212' and a != 'Plantinga':
        #     return False
        # if B == 'cs212' and b != 'Plantinga':
        #     return False
        # if A == 'cs214' and a != 'Schuurman':
        #     return False
        # if B == 'cs214' and b != 'Schuurman':
        #     return False
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
        domains[course] = times + rooms

    domains['cs108'].append('Vanderlinden')
    domains['cs344'].append('Vanderlinden')
    domains['cs112'].append('Adams')
    domains['cs374'].append('Adams')
    domains['cs212'].append('Plantinga')
    domains['cs214'].append('Schuurman')


    # neighbors = {}
    # for course in classes:
    #     neighbors[course] = classes

    neighbors = parse_neighbors("""
            cs108: cs112 cs214 cs374 cs344 cs212;
            cs112: cs214 cs374 cs344 cs212;
            cs214: cs374 cs344 cs212;
            cs374: cs344 cs212;
            cs344: cs212;
            cs212: """)

    def schedule_constraint(A, a, B, b):
        if a == 'mwf9' and b != 'mwf9':
            return True
        if a == 'mwf10' and b != 'mwf10':
            return True
        if a == 'mwf11' and b != 'mwf11':
            return True
        if a == 'mwf12' and b != 'mwf12':
            return True
        if a == 'nh253' and b == 'sb382':
            return True


    return CSP(classes, domains, neighbors, schedule_constraint)


if __name__ == '__main__':
    # classes = 'cs108 cs112 cs214 cs374 cs344 cs212'.split()
    # faculty = 'Schuurman Adams Vanderlinden Plantinga'.split()
    # times = 'mwf9 mwf10 mwf11 mwf12'.split()
    # rooms = 'nh253 sb382'.split()
    #
    # domains = {}
    # for course in classes:
    #     domains[course] = times + rooms
    #
    # domains['cs108'].append('Vanderlinden')
    # domains['cs344'].append('Vanderlinden')
    # domains['cs112'].append('Adams')
    # domains['cs374'].append('Adams')
    # domains['cs212'].append('Plantinga')
    # domains['cs214'].append('Schuurman')
    #
    # # neighbors = {}
    # # for course in classes:
    # #     neighbors[course]
    # neighbors = parse_neighbors("""
    #         cs108: cs112 cs214 cs374 cs344 cs212;
    #         cs112: cs214 cs374 cs344 cs212;
    #         cs214: cs374 cs344 cs212;
    #         cs374: cs344 cs212;
    #         cs344: cs212;
    #         cs212: """)
    #
    # print(domains.items())
    # print(neighbors.items())

    puzzle = schedule()

    # result = depth_first_graph_search(puzzle)
    result = AC3(puzzle)
    # result = backtracking_search(puzzle)
    # result = min_conflicts(puzzle, max_steps=1000)

    if puzzle.goal_test(puzzle.infer_assignment()):
        print("Solution:\n")
        # print_solution(result)
    else:
        print("failed...")
        print(puzzle.curr_domains)
        puzzle.display(puzzle.infer_assignment())
