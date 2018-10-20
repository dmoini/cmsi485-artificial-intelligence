'''
maze_knowledge_base.py

Specifies a simple, Conjunctive Normal Form Propositional
Logic Knowledge Base for use in Grid Maze pathfinding problems
with side-information.
'''
from maze_clause import MazeClause
from itertools import combinations
import unittest

class MazeKnowledgeBase:

    def __init__(self):
        self.clauses = set()

    def tell(self, clause):
        """
        Adds the given clause to the CNF MazeKnowledgeBase
        Note: we expect that no clause added this way will ever
        make the KB inconsistent (you need not check for this)
        """
        self.clauses.add(clause)

    def ask(self, query):
        """
        Given a MazeClause query, returns True if the KB entails
        the query, False otherwise
        """
        # TODO: Implement resolution inference here!
        # This is currently implemented incorrectly; see
        # spec for details!
        # self = KB, query = α
        negated_query = self.negate(query) #DON'T ADD NEGATED QUERY
        new_clauses = set()
        # for clause in self.clauses:
        #     resolvent = m

        return False

    def negate(self, clause):
        props = clause.props
        negated_clauses = set()
        for k, v in props.items():
            print(str(MazeClause([(k, v)])))
            negated_clauses.add(MazeClause([(k, not v)]))
        return negated_clauses


kb = MazeKnowledgeBase()
clauses = kb.negate(MazeClause([(("Z", (1, 1)), True), (("W", (1, 1)), True)]))
for c in clauses:
    print(str(c))


# class MazeKnowledgeBaseTests(unittest.TestCase):
#     def test_mazekb1(self):
#         kb = MazeKnowledgeBase()
#         kb.tell(MazeClause([(("X", (1, 1)), True)]))
#         self.assertTrue(kb.ask(MazeClause([(("X", (1, 1)), True)])))
#
#     def test_mazekb2(self):
#         kb = MazeKnowledgeBase()
#         kb.tell(MazeClause([(("X", (1, 1)), False)]))
#         kb.tell(MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), True)]))
#         self.assertTrue(kb.ask(MazeClause([(("Y", (1, 1)), True)])))
#
#     def test_mazekb3(self):
#         kb = MazeKnowledgeBase()
#         kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True)]))
#         kb.tell(MazeClause([(("Y", (1, 1)), False), (("Z", (1, 1)), True)]))
#         kb.tell(MazeClause([(("W", (1, 1)), True), (("Z", (1, 1)), False)]))
#         kb.tell(MazeClause([(("X", (1, 1)), True)]))
#         self.assertTrue(kb.ask(MazeClause([(("W", (1, 1)), True)])))
#         self.assertFalse(kb.ask(MazeClause([(("Y", (1, 1)), False)])))
#
#     def test_mazekb4(self):
#         kb = MazeKnowledgeBase()
#         kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), True)]))
#         kb.tell(MazeClause([(("W", (1, 1)), False), (("Z", (1, 1)), False), (("S", (1, 1)), True)]))
#         kb.tell(MazeClause([(("S", (1, 1)), False), (("T", (1, 1)), False)]))
#         kb.tell(MazeClause([(("X", (1, 1)), True), (("T", (1, 1)), True)]))
#         kb.tell(MazeClause([(("W", (1, 1)), True)]))
#         kb.tell(MazeClause([(("T", (1, 1)), True)]))
#         self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), False)])))
#
#     def test_mazekb5(self):
#         kb = MazeKnowledgeBase()
#         kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), True)]))
#         kb.tell(MazeClause([(("W", (1, 1)), False), (("Z", (1, 1)), False), (("S", (1, 1)), True)]))
#         kb.tell(MazeClause([(("S", (1, 1)), False), (("T", (1, 1)), False)]))
#         kb.tell(MazeClause([(("X", (1, 1)), True), (("T", (1, 1)), True)]))
#         kb.tell(MazeClause([(("W", (1, 1)), True)]))
#         kb.tell(MazeClause([(("T", (1, 1)), True)]))
#         self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), True), (("W", (1, 1)), True)])))
#
#     def test_mazekb6(self):
#         kb = MazeKnowledgeBase()
#         kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), False),
#                             (("Z", (1, 1)), False)]))
#         kb.tell(MazeClause([(("X", (1, 1)), True)]))
#         self.assertFalse(kb.ask(MazeClause([(("Z", (1, 1)), False)])))
#         kb.tell(MazeClause([(("Y", (1, 1)), True)]))
#         self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), False)])))
#
#
# if __name__ == "__main__":
#     unittest.main()
