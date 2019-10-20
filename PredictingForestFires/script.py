import csv
import matplotlib.pyplot as plot 
import numpy as np 
import pandas as pd 
import sys 
import math 

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



def main():

    raw_data_set = 'hw3_question1.csv'
    shuffled_data_set = 'shuffled_q1_data.csv'
    small_data_set = 'small_data_subset.csv'
    even_smaller_data_set = 'even_smaller_data_subset.csv'
    
    # generateHistogramUsingOutputFrom(raw_data_set)
    

    data = pd.read_csv(even_smaller_data_set, header = None)
    num_rows = len(data)
    num_data_chunks = 3
    num_data_partitions = math.ceil(num_rows / num_data_chunks)

    
    chunk_start_index = 0
    data_chunk_size = math.ceil(num_rows / num_data_partitions)
    chunk_end_index = data_chunk_size - 1
    for n in range(0, num_rows, data_chunk_size):
        Xs = data.drop(data.index[chunk_start_index:chunk_end_index + 1])
        Ys = data.loc[chunk_start_index:chunk_end_index]
        chunk_start_index += data_chunk_size
        chunk_end_index += data_chunk_size
        print("Xs")
        print(Xs)
        print()
        print("Ys")
        print(Ys)
        print("----------------")
        print()
    
    # print("number of rows: " + str(num_rows))
    print("size of data chunk: " + str(data_chunk_size))
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