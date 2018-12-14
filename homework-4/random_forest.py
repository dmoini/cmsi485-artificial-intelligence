import preprocess_data
from sklearn.ensemble import RandomForestClassifier

def train_random_forest():
    data = preprocess_data.preprocess('income-training.csv', 'income-test.csv')
    training_X, training_Y = data[0][:,0:13], data[0][:,13]
    test_X, test_Y = data[1][:,0:13], data[1][:,13]
    clf = RandomForestClassifier().fit(training_X, training_Y)
    return clf.score(test_X, test_Y)