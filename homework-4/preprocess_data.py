from sklearn import preprocessing
from sklearn.impute import SimpleImputer, MissingIndicator
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import OrdinalEncoder


def preprocess(training, test):
    training_data = stripQuotes(np.genfromtxt(
        training, dtype=str, delimiter=','))
    test_data = stripQuotes(np.genfromtxt(test, dtype=str, delimiter=','))
    training_df = pd.DataFrame(training_data, dtype=str)
    test_df = pd.DataFrame(test_data, dtype=str)
    imputer = SimpleImputer(
        missing_values='?', strategy='most_frequent').fit(training_df)
    imp_training = imputer.transform(training_df)
    imp_test = imputer.transform(test_df)
    ct = ColumnTransformer(
        [("age", KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='kmeans'), [0]),
         ("work/edu", OrdinalEncoder(), [1, 2]),
         ("edu-num", KBinsDiscretizer(n_bins=5,
                                      encode='ordinal', strategy='kmeans'), [3]),
         ("mar/occ/rel/race/sex", OrdinalEncoder(), [4, 5, 6, 7, 8]),
         ("cg", KBinsDiscretizer(n_bins=3,
                                 encode='ordinal', strategy='kmeans'), [9]),
         ("cl", KBinsDiscretizer(n_bins=3,
                                 encode='ordinal', strategy='kmeans'), [10]),
         ("hrs", KBinsDiscretizer(n_bins=3,
                                  encode='ordinal', strategy='kmeans'), [11]),
         ("nat", OrdinalEncoder(), [12])], remainder='passthrough').fit(imp_training)
    ct_training = ct.transform(imp_training)
    ct_test = ct.transform(imp_test)
    return (ct_training, ct_test)


def stripQuotes(data):
    return [[feature.strip(' ') for feature in line] for line in data]
