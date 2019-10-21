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

    raw_data_set = 'hw3_question1.csv'
    shuffled_data_set = 'shuffled_q1_data.csv'
    # small_data_set = 'small_data_subset.csv'
    # even_smaller_data_set = 'even_smaller_data_subset.csv'
    
    # generateHistogramUsingOutputFrom(raw_data_set)
    
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

        # y_train = []
        # for x in y_train_data.values.tolist():
        #     if (float(x[0]) > 0.0):
        #         y_train.append(1)
        #     else:
        #         y_train.append(0)
        regression.fit(x_train_data, y_train)

        y_test = classifyOutcomesOf(y_test_data)
        # y_test = []
        # for x in y_test_data.values.tolist():
        #     if (float(x[0]) > 0.0):
        #         y_test.append(1)
        #     else:
        #         y_test.append(0)
        accuracy = regression.score(x_test_data, y_test)
        print("Round " + str(loopIteration) + " prediction was: " + str(accuracy))
        
        # print("X Train Data")
        # print(x_train_data)
        # print()
        # print("X Test Data")
        # print(x_test_data)
        # print()
        # print("Y Train Data")
        # print(y_train_data)
        # print()
        # print("Y Test Data")
        # print(y_test_data)
        # print()
        # print("Y train data as array")
        # print(y_train_data.values.tolist())
        # mergeList = []
        # for x in y_train_data.values.tolist():
        #     mergeList += x
        # print(mergeList)
        # print()
        # print(type(y_train_data.values))
        # print(np.stack(y_train_data.values))
        # print("----------------")
        # print()
    
    # print("number of rows: " + str(num_rows))
    # print("size of data chunk: " + str(data_chunk_size))
    # print(num_data_partitions)
    # print(Xs)
    # print(Ys)
    

    print("no errors")



if __name__ == '__main__':
    main()


    # features = [
    #     'x-axis spatial coordinate of forest',    # [1,9]
    #     'y-axis spatial coordinate of forest',    # [2,9]
    #     'Month',                                  # [1,12]
    #     'Day',                                    # [1,7]    
    #     'FFMC',                                   # (index from FWI system)
    #     'DMC',                                    # (...)
    #     'DC',                                     # (...)
    #     'ISI',                                    # (...)
    #     'Temperature',                            # in Celcius
    #     'Relative Humidity',
    #     'Wind Speed',                             # km/h   
    #     'Rain',                                   # mm/m^2
    #     'Area Burned'
    # ]