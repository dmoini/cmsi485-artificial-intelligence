'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest


class Pathfinder:
    # solve is parameterized by a maze pathfinding problem
    # (see MazeProblem.py and unit tests below), and will
    # return a list of actions that solves that problem. An
    # example returned list might look like:
    # ["U", "R", "R", "U"]
    def solve(problem):
        queue = [SearchTreeNode(problem.initial, None, None)]
        graveyard = set()  # Contains states, not actual nodes
        while len(queue) != 0:
            current_node = queue.pop(0)
            # print(f'Current node: str(){current_node.state})')
            # front = path[-1]
            if problem.goalTest(current_node.state):
                print(str(graveyard))
                return Pathfinder.create_path(current_node)  # TODO: fix
            elif current_node.state not in graveyard:
                # parent = current_node
                for available_moves in problem.transitions(current_node.state):
                    # print(f'Available node: {available_moves[1]})')
                    # TODO: shorten code below into single line
                    next_state = available_moves[1]
                    action = available_moves[0]
                    parent = current_node
                    available_node = SearchTreeNode(next_state, action, parent)
                    if available_node.state not in graveyard:
                        # print("QUEUEEEED")
                        queue.append(available_node)
                    # new_path = [path]
                    # new_path.append(SearchTreeNode(available_move[1], available_move[0], parent))
                    # queue.append(new_path)
                graveyard.add(current_node.state)
        return []

    # STN is a SearchTreeNode
    # create_path returns a list of "DIRECTION" where
    # STN is the SearchTreeNode given
    # and path is the path from the goal state to the initial state
    def create_path(STN):
        path = []
        current_node = STN
        while current_node.parent is not None:
            path.insert(0, current_node.action)
            current_node = current_node.parent
        print(path)
        return path

    # def solve(start, end):
    #     queue = [SearchTreeNode(start, None, None)]
    #     graveyard = ()
    #     while len(queue) != 0:
    #         parent = queue.pop(0)
    #         for available_moves in transitions(parent):


class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    # TODO: Add more unit tests!


if __name__ == '__main__':
    unittest.main()
