# Donovan Moini and Ian Lizarda

'''
ad_engine.py

CMSI 485 HW 3: Advertisement engine that selects from two
ad traits to maximize expected utility of converting a sale
for the Forney Industries Protectron 3001
'''

import itertools
import unittest
import math
import numpy as np
from pomegranate import *

class AdEngine:
    
    """
    Responsible for initializing the Decision Network of the
    AdEngine from the structure discovered by Tetrad
    
    :param string data_file: path to csv file containing data on which
    the network's parameters are to be learned
    :param tuple structure: tuple of tuples specifying parental
    relationships between variables in the network; see Pomegranate docs
    for the expected format. Example:
        ((), (0), (1)) represents nodes: [0] -> [1] -> [2]
    :param list dec_vars: list of string names of variables to be
    considered decision points for the agent. Example:
        ["Ad1", "Ad2"]
    :param dict util_map: discrete, tabular, utility map whose keys
    are variables in network that are parents of a utility node, and
    values are dictionaries mapping that variable's values to a utility
    score, e.g.
        {
        "X": {0: 20, 1: -10}
        }
    represents a utility node with single parent X whose value of 0
    has a utility score of 20, and value 1 has a utility score of -10
    """

    def __init__(self, data_file, structure, dec_vars, util_map):
        data = np.genfromtxt(data_file, dtype=int, names=True, delimiter=',')
        self.names = data.dtype.names
        self.network = BayesianNetwork.from_structure(data.view((int, len(self.names))), structure, state_names=self.names)
        self.dec_vars = dec_vars
        self.dec_vars_values = [list(np.unique(data[v])) for v in dec_vars]
        self.structure = structure
        self.util_map = util_map
        
    def decide(self, evidence):
        """
        Given some observed demographic "evidence" about a potential
        consumer, selects the ad content that maximizes expected utility
        and returns a dictionary over any decision variables and their
        best values
        
        :param dict evidence: dict mapping network variables to their
        observed values, of the format: {"Obs1": val1, "Obs2": val2, ...}
        :return: dict of format: {"DecVar1": val1, "DecVar2": val2, ...}
        """
        best_combo, best_util = None, -math.inf
        possible_combos = itertools.product(*self.dec_vars_values)
        for combo in possible_combos:
            cpts = self.network.predict_proba(evidence)
            util_key = list(self.util_map.keys())[0]
            util_index = self.names.index(util_key)
            dec_dict = {d: combo[i] for i, d in enumerate(self.dec_vars)}
            new_evidence = {**dec_dict, **evidence}
            new_cpts = self.network.predict_proba(new_evidence)
            util = 0
            for u in cpts[util_index].parameters[0].keys():
                util += new_cpts[util_index].parameters[0][u] * self.util_map[util_key][u]
            if util > best_util:
                best_combo = dec_dict
                best_util = util
        return best_combo


class AdEngineTests(unittest.TestCase):
    def test_defendotron_ad_engine_t1(self):
        engine = AdEngine(
            data_file = 'hw3_data.csv',
            dec_vars = ['Ad1', 'Ad2'],
            #            P   A   G        I     T        F        H   S        Ad2 Ad1
            structure = ((), (), (0, 9,), (6,), (0, 1,), (1, 8,), (), (2, 5,), (), ()),
            util_map = {'S': {0: 0, 1: 5000, 2: 17760}}
        )
        self.assertEqual(engine.decide({'G': 0}), {'Ad1': 0, "Ad2": 1})
        self.assertEqual(engine.decide({'F': 1}), {'Ad1': 1, 'Ad2': 0})
        self.assertEqual(engine.decide({'G': 1, 'T': 0}), {'Ad1': 1, 'Ad2': 1})
        
    def test_defendotron_ad_engine_t2(self):
        engine = AdEngine(
            data_file = 'hw3_data.csv',
            # [!] Note: in this example, say we are only deciding upon the ad
            # video (Ad1); our engine's results should adapt accordingly (see
            # tests below)
            dec_vars = ['Ad1'],
            structure = ((), (), (0, 9,), (6,), (0, 1,), (1, 8,), (), (2, 5,), (), ()),
            util_map = {'S': {0: 0, 1: 5000, 2: 17760}}
        )
        self.assertEqual(engine.decide({'A': 1}), {'Ad1': 0})
        self.assertEqual(engine.decide({'P': 1, 'A': 0}), {'Ad1': 1})
        self.assertEqual(engine.decide({'A': 1, 'G': 1, 'T': 1}), {'Ad1': 0})

if __name__ == '__main__':
    unittest.main()
    