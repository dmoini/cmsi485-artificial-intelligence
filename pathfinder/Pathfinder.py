# Donovan Moini
'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import queue
import unittest


class Pathfinder:
    # solve is parameterized by a maze pathfinding problem
    # (see MazeProblem.py and unit tests below), and will
    # return a list of actions that solves that problem. An
    # example returned list might look like:
    # ["U", "R", "R", "U"]
    def solve(problem):
        q = queue.Queue()
        q.put(SearchTreeNode(problem.initial, None, None))
        visited = set()
        while q:
            current = q.get()
            if problem.goalTest(current.state):
                return Pathfinder.get_path(current)
            for action, state in problem.transitions(current.state):
                if state not in visited:
                    q.put(SearchTreeNode(state, action, current))
            visited.add(current.state)
        return []

    # STN is a SearchTreeNode
    # get_path returns a list of "DIRECTION" where
    # STN is the SearchTreeNode given
    # and path is the path from the goal state to the initial state
    def get_path(STN):
        path = []
        current = STN
        while current.parent:
            path.append(current.action)
            current = current.parent
        return path[::-1]


class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX",
                "X..GX",
                "X...X",
                "X*..X",
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX",
                "XG..X",
                "XX..X",
                "X*..X",
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze3(self):
        maze = ["XXXXX",
                "XG..X",
                "XX..X",
                "X*.GX",
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 2)

    def test_maze4(self):
        maze = ["XXXXXXX",
                "X..*..X",
                "XXX.XXX",
                "X.....X",
                "X.X.XGX",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 5)

    def test_maze5(self):
        maze = ["XXXXXXX",
                "X..*..X",
                "XXX.XXX",
                "XG....X",
                "X.X.XGX",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze6(self):
        maze = ["XXXXXXX",
                "XGX...X",
                "XXX...X",
                "X..*..X",
                "X.....X",
                "X....GX",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze7(self):
        maze = ["XXXXXXX",
                "X..G..X",
                "X.....X",
                "X.G*.GX",
                "X.....X",
                "X..G..X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 1)

    def test_maze8(self):
        maze = ["XXXXXXX",
                "X*....X",
                "XXXXX.X",
                "X.....X",
                "X.XXXXX",
                "X....GX",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 16)


if __name__ == '__main__':
    unittest.main()
