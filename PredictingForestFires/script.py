import csv
import matplotlib.pyplot as plot 
import numpy as np 
import pandas as pd 
import math 
from sklearn.linear_model import LogisticRegression

def generateHistogramUsingOutputFrom(data):
    with open(data) as d:
        CsvData = csv.reader(d, delimiter = ',')

        # 13th data point in each row represents burned area
        burnedAreaIndex = 12  
        burnedAreaFrequency = []
        for i, row in enumerate(CsvData):
            # skip first row (contains feature titles)
            if i == 0:
                continue
            burnedAreaFrequency.append(float(row[burnedAreaIndex]))
        plot.hist(burnedAreaFrequency, color = 'blue', bins = 100)
        plot.xlabel('Burned Area (ha)')
        plot.ylabel('Frequency')
        plot.show()

def classifyOutcomesOf(data):
    classificationList = []
    for x in data.values.tolist():
        if (float(x[0]) > 0.0):
            classificationList.append(1)
        else:
            classificationList.append(0)
    return classificationList

def main():
    # raw_data_set = 'hw3_question1.csv'
    # generateHistogramUsingOutputFrom(raw_data_set)

    shuffled_data_set = 'shuffled_q1_data.csv'
    data = pd.read_csv(shuffled_data_set, header = None)

    # cross-validation implementation
    num_rows = len(data)
    num_folds = 10
    fold_size = math.ceil(num_rows / num_folds)
    fold_start_index = 0
    fold_end_index = fold_size - 1
    loopIteration = 0
    for _ in range(0, num_rows, fold_size):
        loopIteration += 1

        x_train_data = data.drop(data.index[fold_start_index:fold_end_index + 1])
        x_train_data = x_train_data.drop([data.columns[0], data.columns[13]], axis = 1)

        y_train_data = data.drop(data.index[fold_start_index:fold_end_index + 1])
        y_train_data = y_train_data.drop(data.columns[0:13], axis = 1)

        x_test_data = data.loc[fold_start_index:fold_end_index]
        x_test_data = x_test_data.drop([data.columns[0], data.columns[13]], axis = 1)

        y_test_data = data.loc[fold_start_index:fold_end_index]
        y_test_data = y_test_data.drop(data.columns[0:13], axis = 1)

        fold_start_index += fold_size
        fold_end_index += fold_size

        regression = LogisticRegression(solver = 'lbfgs')
        y_train = classifyOutcomesOf(y_train_data)
        regression.fit(x_train_data, y_train)

        y_test = classifyOutcomesOf(y_test_data)
        accuracy = regression.score(x_test_data, y_test)
        print("Round " + str(loopIteration) + " prediction accuracy was: " + str(accuracy))

if __name__ == '__main__':
    main()