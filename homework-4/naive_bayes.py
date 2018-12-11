import preprocess_data
from sklearn import datasets
from sklearn.naive_bayes import ComplementNB

def train_NBC():
    data = preprocess_data.preprocess('income-training.csv')
    # print(data)
    X = [[a for a in b[:13]] for b in data[:10]]
    Y = [[b[13]] for b in data[:10]]
    # print(X)
    print(Y)
    # test_data = preprocess_data.preprocess('income-test.csv')
    # clf = ComplementNB()
    # print(clf.fit(X, Y))

    
    # print(data)
    # iris = datasets.load_iris()
    # print(iris.data)


    # gnb = GaussianNB()
    # y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
    # y_pred = gnb.fit(data, test_data).predict(data)
    # print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))

train_NBC()