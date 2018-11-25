import pandas as pd
from NavieBayesModel import NaiveBayesModel
import numpy as np
from read_data import read_data
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score


class SentimentClassification(object):
    def __init__(self):
        self.test = None

    def get_train_data(self, txt):
        # init model naive bayes
        model = NaiveBayesModel()
        path_train = 'dataset/train.csv'
        path_test = 'dataset/test.csv'

        X_train, y_train = read_data(path_train)
        X_test, y_test = read_data(path_test)
        clf = model.clf.fit(X_train, y_train)

        y_predic = clf.predict(X_test)
        print("size of test: " + str(len(y_test)))

        accuracy = accuracy_score(y_test, y_predic)
        print("accuracy: " + str(accuracy))
        # Tạo test data
        test_data = []
        test_data.append({"Rate": 9.0, "Review": txt, "Label": "pos"})
        # test_data.append({"Rate": 3.0, "Review": u"phục vụ rất tệ", "Label": "neg"})
        # test_data.append({"Rate": 10.0, "Review": u"hihi", "Label": "neu"})
        # test_data.append({"Rate": 10.0, "Review": u"ngon lắm luôn ý", "Label": "pos"})
        df_test = pd.DataFrame(test_data)

        predicted = clf.predict(df_test["Review"])

        # Print predicted result
        # print(predicted)
        # print(clf.predict_proba(df_test["Review"]))

        precision = precision_score(y_test, y_predic, average=None)
        f1 = f1_score(y_test, y_predic, average=None)
        recall = recall_score(y_test, y_predic, average=None)
        print("accuracy of precision: " + str(precision))
        print("accuracy of f1: " + str(f1))
        print("accuracy of recall: " + str(recall))

        # return test data with a sentence
        return predicted[0]


if __name__ == '__main__':
    tcp = SentimentClassification()
    tcp.get_train_data('Ngon quá')
