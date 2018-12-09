from sklearn import preprocessing
from sklearn.impute import SimpleImputer, MissingIndicator
import numpy as np
import pandas as pd

def process():
    data = np.genfromtxt('income-training.csv', dtype=str, delimiter=',')
    # print(data)
    # 
    df = pd.DataFrame(data, dtype=str)
    imp = SimpleImputer(missing_values='?', strategy='constant', fill_value=-1)    
    impdf = imp.fit_transform(df)
    print(impdf)

    # indicator = MissingIndicator(missing_values='?', features='all')
    # mask_all = indicator.fit_transform(df)
    # print(mask_all)




    # print(imp)
    # imp.fit(data)
    # print(imp.fit(data))
    # imp = SimpleImputer(missing_values='?', strategy="most_frequent")
    # print(imp)
    
    
    # NOTE: SAFE BELOW
    # enc = preprocessing.OrdinalEncoder()
    # enc.fit(data)
    # data = enc.transform(data)
    # est = preprocessing.KBinsDiscretizer(n_bins=[3, 8, 16, 3, 6, 14, 6, 5, 2, 2, 2, 3, 195, 2], encode='ordinal').fit(data)
    # print(est.transform(data))

process()