'''
hw_3_grading.py

Due to some ambiguities in the spec, I decided to be err on the
side of fairness and simply test some extensions of the original
dataset and accompanying structure
'''
import unittest
from ad_engine import AdEngine

class AdEngineTests(unittest.TestCase):
    def test_defendotron_ad_engine_t1(self):
        engine = AdEngine(
            data_file = 'hw3_data.csv',
            dec_vars = ["Ad1", "Ad2"],
            # Structure encoded from what we found in Tetrad
            structure = ((), (), (0,9), (6,), (0,1), (1,8), (), (2,5), (), ()),
            # Utility map corresponds to spec's dollar amounts for each sale condition
            util_map = {"S": {0: 0, 1: 5000, 2: 17760}}
        )
        self.assertEqual(engine.decide({"T": 1}), {"Ad1": 0, "Ad2": 1})
        self.assertIn(engine.decide({"F": 1}), [{"Ad1": 1, "Ad2": 0},{"Ad1": 1, "Ad2": 1}])
        self.assertEqual(engine.decide({"G": 1, "T": 0}), {"Ad1": 1, "Ad2": 1})
        self.assertEqual(engine.decide({"A": 1, "P": 1}), {"Ad1": 1, "Ad2": 1})
        self.assertEqual(engine.decide({"A": 0, "P": 0}), {"Ad1": 0, "Ad2": 1})
        
    def test_defendotron_ad_engine_t2(self):
        engine = AdEngine(
            data_file = 'hw3_data.csv',
            dec_vars = ["Ad1"],
            structure = ((), (), (0,9), (6,), (0,1), (1,8), (), (2,5), (), ()),
            util_map = {"S": {0: 0, 1: 5000, 2: 17760}}
        )
        self.assertEqual(engine.decide({"A": 1}), {"Ad1": 0})
        self.assertEqual(engine.decide({"P": 1, "A": 0}), {"Ad1": 1})
        self.assertIn(engine.decide({"A": 1, "G": 0, "T": 1}), [{"Ad1": 0}, {"Ad1": 1}])
        self.assertEqual(engine.decide({"A": 1, "P": 1}), {"Ad1": 1})
        self.assertEqual(engine.decide({"A": 0, "P": 0}), {"Ad1": 0})

if __name__ == "__main__":
    unittest.main()