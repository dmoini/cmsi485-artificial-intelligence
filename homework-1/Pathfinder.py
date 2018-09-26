# Donovan Moini
'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to all
of the goals with optimal cost.

This task is done in the solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest
from queue import PriorityQueue


def heuristic_cost(a, b):
    (x1, y1), (x2, y2) = a, b
    return abs(x1 - x2) + abs(y1 - y2)


def find_path(search_node):
    path = []
    curr_node = search_node
    print(curr_node.state)
    while curr_node.parent:
        path.append(curr_node.action)
        curr_node = curr_node.parent
    return path[::-1]


def best_path(paths):
    lowest_cost, best_path = paths[0].totalCost, None  # TODO: find something for math.max
    for path in paths:
        if path.totalCost < lowest_cost:
            lowest_cost = path.totalCost
            best_path = path
    return best_path

# TODO: remove print statements


def solve(problem, initial, goals):
    frontier = PriorityQueue()
    frontier.put((0, SearchTreeNode(initial, None, None, 0, 0)))
    visited = set()
    goal = goals[0]  # TODO: remove
    # TODO: test it again
    best_path_per_goal = []
    # for goal in goals:
    while frontier:
        curr_node = frontier.get()[1]
        if curr_node.state == goal:
            return find_path(curr_node)
        for action, cost, state in problem.transitions(curr_node.state):
            new_cost = cost + curr_node.totalCost
            if curr_node.state not in visited or new_cost < curr_node.totalCost:
                heuristicCost = heuristic_cost(state, goal)
                priority = cost + curr_node.totalCost + heuristicCost
                frontier.put((priority, SearchTreeNode(state, action, curr_node, new_cost, heuristicCost)))
        visited.add(curr_node.state)
    return []

# NOTE: tests
class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals = [(5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 8)

    def test_maze2(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals = [(3, 2)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 5)

    # def test_maze3(self):
    #     maze = ["XXXXXXX",
    #             "X.....X",
    #             "X.M.M.X",
    #             "X.X.X.X",
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     initial = (1, 3)
    #     goals = [(3, 3), (5, 3)]
    #     soln = solve(problem, initial, goals)
    #     (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
    #     print((soln_cost, is_soln))
    #     self.assertTrue(is_soln)
    #     self.assertEqual(soln_cost, 12)
    #
    # def test_maze4(self):
    #     maze = ["XXXXXXX",
    #             "X.....X",
    #             "X.M.MMX",
    #             "X...M.X",
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     initial = (5, 1)
    #     goals = [(5, 3), (1, 3), (1, 1)]
    #     soln = solve(problem, initial, goals)
    #     (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
    #     self.assertTrue(is_soln)
    #     self.assertEqual(soln_cost, 12)
    #
    # def test_maze5(self):
    #     maze = ["XXXXXXX",
    #             "X.....X",
    #             "X.M.XXX",
    #             "X...X.X",
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     initial = (5, 1)
    #     goals = [(5, 3), (1, 3), (1, 1)]
    #     soln = solve(problem, initial, goals)
    #     self.assertTrue(soln)


if __name__ == '__main__':
    unittest.main()
