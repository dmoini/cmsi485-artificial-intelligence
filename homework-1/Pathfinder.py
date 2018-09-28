# Donovan Moini
'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to all
of the goals with optimal cost.

This task is done in the solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''
import itertools
from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest
from queue import PriorityQueue

def get_heuristic_cost(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def find_path(STN):
    path = []
    current = STN
    while current.parent:
        path.append(current.action)
        current = current.parent
    return path[::-1]

def a_star_search(problem, initial, goal):
    q = PriorityQueue()
    q.put((0, SearchTreeNode(initial, None, None, 0, 0)))
    visited = set()
    while not q.empty():
        current = q.get()[1]
        if current.state == goal:
            return (find_path(current), current.totalCost)
        for action, cost, state in problem.transitions(current.state):
            next_cost = cost + current.totalCost
            if current.state not in visited or next_cost < current.totalCost:
                heuristic_cost = get_heuristic_cost(state, goal)
                total_heuristic_cost = cost + current.totalCost + heuristic_cost
                q.put((total_heuristic_cost,
                       SearchTreeNode(state, action, current, next_cost, heuristic_cost)))
        visited.add(current.state)
    return None

def create_path(goals):
    return [list(goal) for goal in goals]

def solve(problem, initial, goals):
    goal_permutations = create_path(itertools.permutations(goals))
    solutions = PriorityQueue()
    for goal in goal_permutations:
        goal.insert(0, initial)
        paths = []
        total_heuristic_cost = 0
        for i in range(len(goal) - 1):
            solved = a_star_search(problem, goal[i], goal[i + 1])
            if solved is None:
                return None
            paths.extend(solved[0])
            total_heuristic_cost += solved[1]
        solutions.put((total_heuristic_cost, paths))
    return solutions.get()[1]


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

    def test_maze3(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals = [(3, 3), (5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze4(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.MMX",
                "X...M.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals = [(5, 3), (1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze5(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.XXX",
                "X...X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals = [(5, 3), (1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln is None)

    def test_maze6(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.....X",
                "X.....X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (3, 2)
        goals = [(1, 1), (5, 1), (1, 3), (5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 11)

    def test_maze7(self):
        maze = ["XXXXXXX",
                "X.....X",
                "XXXXXXX",
                "X.....X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (3, 1)
        goals = [(3, 3), (5, 1)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln is None)


if __name__ == '__main__':
    unittest.main()
