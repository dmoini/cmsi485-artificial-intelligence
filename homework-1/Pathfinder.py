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


def reachable(problem, goal):
    return len(problem.transitions(goal)) > 0


def a_star(problem, initial, goal):
    q = PriorityQueue()
    q.put((0, SearchTreeNode(initial, None, None, 0, 0)))
    visited = set()
    while q and reachable(problem, goal):
        current = q.get()[1]
        if current.state == goal:
            return (find_path(current), current.totalCost)
        for action, cost, state in problem.transitions(current.state):
            new_cost = cost + current.totalCost
            if current.state not in visited or new_cost < current.totalCost:
                heuristic_cost = get_heuristic_cost(state, goal)
                priority = cost + current.totalCost + heuristic_cost
                q.put((priority, SearchTreeNode(state, action, current, new_cost, heuristic_cost)))
        visited.add(current.state)
    return None


def create_path(goals):
    goal_list = []
    for goal in goals:
        goal_list.append(list(goal))
    return goal_list


def solve(problem, initial, goals):
    valid_goals = [g for g in goals if reachable(problem, g)]
    goal_permutations = create_path(itertools.permutations(valid_goals))
    optimal_solutions = PriorityQueue()
    for goal in goal_permutations:
        goal.insert(0, initial)
        paths = []
        priority = 0
        for i in range(len(goal) - 1):
            solved = a_star(problem, goal[i], goal[i + 1])
            paths.extend(solved[0])
            priority += solved[1]
        optimal_solutions.put((priority, paths))
    return optimal_solutions.get()[1]


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
        self.assertTrue(soln)

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


if __name__ == '__main__':
    unittest.main()
