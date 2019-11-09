import pandas as pd
import csv
import numpy as np
import math
from sklearn.tree import DecisionTreeRegressor

def printVariables(variables):
    for i, var in enumerate(variables):
        print(var)
        print(variables[var])
        if i == len(variables) - 1:
            break
        print("___________")
        print()

def main():
    train_data_set = 'OnlineNewsPopularityTrain_small_subset.csv'
    test_data_set = 'OnlineNewsPopularityTest_small_subset.csv'
    train_data = pd.read_csv(train_data_set, header = None)
    test_data = pd.read_csv(test_data_set, header = None)


    # cross-validation implementation
    num_rows = len(train_data)
    num_folds = 2
    fold_size = math.ceil(num_rows / num_folds)
    fold_start_index = 0
    fold_end_index = fold_size - 1
    foldNum = 0
    for _ in range(0, num_rows, fold_size):
        foldNum += 1
        print("Fold: " + str(foldNum))

        test_fold_x = test_data.loc[fold_start_index:fold_end_index]
        x_test = test_fold_x.drop([test_data.columns[0], test_data.columns[60]], axis = 1)
        train_fold_x = train_data.drop(train_data.index[fold_start_index:fold_end_index + 1])
        x_train = train_fold_x.drop([train_data.columns[0], train_data.columns[60]], axis = 1)

        test_fold_y = test_data.loc[fold_start_index:fold_end_index]
        y_test = test_fold_y.drop(test_data.columns[0:60], axis = 1)
        train_fold_y = train_data.drop(train_data.index[fold_start_index:fold_end_index + 1])
        y_train = train_fold_y.drop(train_data.columns[0:60], axis = 1)

        vars = {
            "X Test Data": x_test,
            "X Train Data": x_train, 
            "Y Test Data": y_test, 
            "Y Train Data": y_train
        }
        printVariables(vars)
        print("**************")
        print()

        regression = DecisionTreeRegressor()
        # y_train = classifyOutcomesOf(y_train_data)
        # regression.fit(x_train_data, y_train)

        fold_start_index += fold_size
        fold_end_index += fold_size

if __name__ == '__main__': 
    main()


   

    #     y_test = classifyOutcomesOf(y_test_data)
    #     accuracy = regression.score(x_test_data, y_test)
    #     print("Round " + str(loopIteration) + " prediction accuracy was: " + str(accuracy))