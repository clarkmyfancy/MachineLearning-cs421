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

    test_data = 'hw3_question1.csv'
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
    
    generateHistogramUsingOutputFrom(test_data)

    print("no errors")



if __name__ == '__main__':
    main()