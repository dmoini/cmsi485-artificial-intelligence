'''
MazeProblem Formalization:
MazeProblems represent 2D pathfinding problems, as programmatically
formalized via:

=== Mazes ===
Represented as a list of strings in which:
  X = impassable wall
  * = the initial state
  . = open cells
  G = goal states
All valid mazes have:
  - At most 1 initial state
  - At least 1 goal state
  - A border of walls (plus possibly other walls)
  - A solution
(We'll ignore invalid maze states as possible inputs, for simplicity)

Maze elements are indexed starting at (0, 0) [top left of maze]. E.g.,
["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"] is interpretable as:
  01234
0 XXXXX
1 X..GX
2 X...X
3 X*..X
4 XXXXX

=== States ===
Representing the position of the agent, as tuples in which:
(x, y) = (col, row)
(0, 0) is located at the top left corner; Right is +x, and Down is +y

=== Actions ===
Representing the allowable Up, Down, Left, and Right movement capabilities
of the agent in the 2D Maze; we'll simply use string representations:
"U", "D", "L", "R"

=== Transitions ===
Given some state s, the transitions will be represented as a list of tuples
of the format:
[(action1, result(action1, s)), ...]
For example, if an agent is at state (1, 1), and can only move right and down,
then the transitions for that s = (1, 1) would be:
[("R", (2, 1)), ("D", (1, 2))]
'''
class MazeProblem:

    # MazeProblem Constructor:
    # Constructs a new pathfinding problem from a maze, described above
    def __init__(self, maze):
        self.maze = maze
        # self.initial = [(y, x) for x, i in enumerate(maze) for y, j in enumerate(i) if j == "*"]
        self.initial = None
        # self.goals = [(y, x) for x, i in enumerate(maze) for y, j in enumerate(i) if j == "G"]
        self.goals = []

        for y, line in enumerate(maze):
            for x, spot in enumerate(line):
                if spot == "*":
                    self.initial = (x, y)
                if spot == "G":
                    self.goals.append((x, y))

    # goalTest is parameterized by a state, and
    # returns True if the given state is a goal, False otherwise
    def goalTest(self, state):
        x, y = state
        return self.maze[y][x] == "G"

    # returns dictionary where:
    # key is a string of format "DIRECTION"
    # value is tuple of format (x, y)
    # each tuple is an available movement from the given state
    def possible_states(self, s):
        x, y = s
        possible_states = {}
        if y != 0 and self.maze[y - 1][x] != 'X':  # UP?
            possible_states['U'] = (x, y - 1)
            print('U: ' + str(possible_states['U']))
        if y != len(self.maze) - 1 and self.maze[y + 1][x] != 'X':  # DOWN
            possible_states['D'] = (x, y + 1)
            print('D: ' + str(possible_states['D']))
        if x != 0 and self.maze[y][x - 1] != 'X':  # LEFT
            possible_states['L'] = (x - 1, y)
            print('L: ' + str(possible_states['L']))
        if x != len(self.maze[0]) - 1 and self.maze[y][x + 1] != 'X':  # RIGHT
            possible_states['R'] = (x + 1, y)
            print('R: ' + str(possible_states['R']))
        return possible_states

    # transitions returns a list of tuples in the format:
    # [(action1, result(action1, s)), ...]
    # corresponding to allowable actions of the given state, as well
    # as the next state the action leads to
    def transitions(self, state):
        possible_states = self.possible_states(state)
        return [(k, v) for k, v in possible_states.items()]

    # returns tuple of format (x, y) where returned tuple
    # is the resulting state of a given action and a given state
    # def result(self, action1, s):
    #     if action1 == 'U':
    #         return (s[0], s[1] - 1)
    #     if action1 == 'D':
    #         return (s[0], s[1] + 1)
    #     if action1 == 'L':
    #         return (s[0] - 1, s[1])
    #     if action1 == 'R':
    #         return (s[0] + 1, s[1])
    #     return s  # if not possible states, return current state

    # solnTest will return a tuple of the format (cost, isSoln) where:
    # cost = the total cost of the solution,
    # isSoln = true if the given sequence of actions of the format:
    # [a1, a2, ...] successfully navigates to a goal state from the initial state
    # If NOT a solution, return a cost of -1
    def solnTest(self, soln):
        trans = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
        s = self.initial
        for m in soln:
            s = (s[0] + trans[m][0], s[1] + trans[m][1])
            if self.maze[s[1]][s[0]] == "X":
                return (-1, False)
        return (len(soln), self.goalTest(s))

    def print_maze(self, maze):
        print('  01234')
        print(f'0 {maze[0]}')
        print(f'1 {maze[1]}')
        print(f'2 {maze[2]}')
        print(f'3 {maze[3]}')
        print(f'4 {maze[4]}')


maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
testMaze = MazeProblem(maze)
print(f'Maze: {testMaze.maze}')
testMaze.print_maze(maze)
print(f'Initial: {testMaze.initial}')
print(f'Goals: {testMaze.goals}')
# print(testMaze.goalTest(testMaze.goals[0]))
print(testMaze.transitions(testMaze.initial))
# mydict = {'U': (1, 0), 'D': (1, 2), 'L': (0, 1), 'R': (2, 1)}
# mylist = [(k, v) for k, v in mydict.items()]
# print(mylist)