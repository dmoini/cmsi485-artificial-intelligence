from sklearn import preprocessing
from sklearn.impute import SimpleImputer, MissingIndicator
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import OrdinalEncoder


def preprocess(data_file):
    data = np.genfromtxt(data_file, dtype=str, delimiter=',')
    data = [[feature.strip(' ') for feature in line] for line in data]
    df = pd.DataFrame(data, dtype=str)
    imp = SimpleImputer(missing_values='?', strategy='most_frequent')
    impdf = imp.fit_transform(df)
    ct = ColumnTransformer(
        [("age", KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='kmeans'), [0]),
         ("work/edu", OrdinalEncoder(), [1, 2]),
         ("edu-num", KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='kmeans'), [3]),
         ("mar/occ/rel/race/sex", OrdinalEncoder(), [4, 5, 6, 7, 8]),
         ("cg", KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='kmeans'), [9]),
         ("cl", KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='kmeans'), [10]),
         ("hrs", KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='kmeans'), [11]),
         ("nat", OrdinalEncoder(), [12])], remainder='passthrough')
    return ct.fit_transform(impdf)

preprocess('income-training.csv')
