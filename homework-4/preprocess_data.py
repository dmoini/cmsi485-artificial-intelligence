from sklearn import preprocessing
from sklearn.impute import SimpleImputer, MissingIndicator
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import Normalizer




def preprocess(data_file):
    data = np.genfromtxt(data_file, dtype=str, delimiter=',')
    data = [[feature.strip(' ') for feature  in line] for line in data]
    # print(data)
    df = pd.DataFrame(data, dtype=str)
    imp = SimpleImputer(missing_values='?', strategy='most_frequent')    
    impdf = imp.fit_transform(df)
    

# Normalizer scales each row of X to unit norm. A separate scaling
# is applied for the two first and two last elements of each
# row independently.

    # indicator = MissingIndicator(missing_values='?', features='all')
    # mask_all = indicator.fit_transform(df)
    # print(mask_all)
    # print(imp)
    # imp.fit(data)
    # print(imp.fit(data))
    # imp = SimpleImputer(missing_values='?', strategy="most_frequent")
    # print(imp)    
    
    # NOTE: SAFE BELOW
    enc = preprocessing.OrdinalEncoder()
    enc.fit(data)
    ordinal_data = enc.transform(data)
    #print(data)
    # 0, 3, 9, 10, 11 --> normalize continuous data
    ct = ColumnTransformer([("continuous", Normalizer(norm='l1'), [0, 1]),("categorical", Normalizer(norm='l1'), [0, 3, 9, 10, 11])])
    ct.fit_transform(ordinal_data)    
    print(ct.fit_transform(ordinal_data))

    est = preprocessing.KBinsDiscretizer(n_bins=[3, 8, 16, 3, 6, 14, 6, 5, 2, 2, 2, 3, 195, 2], encode='ordinal').fit(ordinal_data)
    # print(est.transform(data))
    # print( [[b[13]] for b in est.transform(ordinal_data)])
    return est.transform(ordinal_data)

preprocess('income-training.csv')