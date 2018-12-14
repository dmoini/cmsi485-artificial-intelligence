# Donovan Moini, Ian Lizarda, Tyler Edmiston

import preprocess_data
from sklearn.naive_bayes import MultinomialNB

def train_NBC():
    data = preprocess_data.preprocess('income-training.csv', 'income-test.csv')
    training_X, training_Y = data[0][:,0:13], data[0][:,13]
    test_X, test_Y = data[1][:,0:13], data[1][:,13]
    clf = MultinomialNB().fit(training_X, training_Y)
    return clf.score(test_X, test_Y)