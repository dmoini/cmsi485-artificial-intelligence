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
    print('-------------------------------------------------------------------------')
    ct = ColumnTransformer(
        [("ordinal", OrdinalEncoder(), [1, 2, 4, 5, 6, 7, 8, 12]),
         ("age/edu",
          KBinsDiscretizer(n_bins=[3, 3], encode='ordinal'), [0, 3]),
         ("cg/cl/hrs", KBinsDiscretizer(n_bins=[3, 2, 3], encode='ordinal'), [9, 10, 11])], remainder='passthrough')
    print(ct.fit_transform(impdf))
    # return est.transform(ordinal_data)


preprocess('income-training.csv')
