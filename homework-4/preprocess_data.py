from sklearn import preprocessing
import numpy as np

def process():
    data = np.genfromtxt('income-training.csv', dtype=str, delimiter=',')
    # X = np.array([[ -3., 5., 15 ], [  0., 6., 14 ], [  6., 3., 11 ]])
    enc = preprocessing.OrdinalEncoder()
    enc.fit(data)
    print(enc.transform(data))
    # est = preprocessing.KBinsDiscretizer(n_bins=[3, 8, 16, 3, 6, 14, 6, 5, 2, 2, 2, 3, 195, 2], encode='ordinal').fit(data)
    # print(data)
    # print(est)

process()