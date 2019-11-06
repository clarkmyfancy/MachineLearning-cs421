import pandas as pd
import csv
import numpy as np
import math

def main():
    train_data_set = 'OnlineNewsPopularityTrain_small_subset.csv'
    test_data_set = 'OnlineNewsPopularityTest_small_subset.csv'
    train_data = pd.read_csv(train_data_set, header = None)
    test_data = pd.read_csv(test_data_set, header = None)


    # cross-validation implementation
    num_rows = len(train_data)
    num_folds = 5
    fold_size = math.ceil(num_rows / num_folds)
    fold_start_index = 0
    fold_end_index = fold_size - 1
    loopIteration = 0
    for _ in range(0, num_rows, fold_size):
        loopIteration += 1

        x_train_data = train_data.drop(train_data.index[fold_start_index:fold_end_index + 1])
        x_train_data = x_train_data.drop([train_data.columns[0], train_data.columns[13]], axis = 1)


        fold_start_index += fold_size
        fold_end_index += fold_size
if __name__ == '__main__': 
    main()


    #     y_train_data = data.drop(data.index[fold_start_index:fold_end_index + 1])
    #     y_train_data = y_train_data.drop(data.columns[0:13], axis = 1)

    #     x_test_data = data.loc[fold_start_index:fold_end_index]
    #     x_test_data = x_test_data.drop([data.columns[0], data.columns[13]], axis = 1)

    #     y_test_data = data.loc[fold_start_index:fold_end_index]
    #     y_test_data = y_test_data.drop(data.columns[0:13], axis = 1)



    #     regression = LogisticRegression(solver = 'lbfgs')
    #     y_train = classifyOutcomesOf(y_train_data)
    #     regression.fit(x_train_data, y_train)

    #     y_test = classifyOutcomesOf(y_test_data)
    #     accuracy = regression.score(x_test_data, y_test)
    #     print("Round " + str(loopIteration) + " prediction accuracy was: " + str(accuracy))