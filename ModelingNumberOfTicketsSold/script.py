import csv
import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plot 
import numpy as np 
from datetime import datetime

import math 
from sklearn.linear_model import LogisticRegression

def generateHistogramFrom(data):
    with open(data) as d:
        CsvData = csv.reader(d, delimiter = ',')
        datetimes = []
        ticketsSold = []
        for i, row in enumerate(CsvData):
            # skip first row (contains feature titles)
            if i == 0:
                continue
            datetimes.append(datetime.strptime(row[0], '%d-%m-%Y %H:%M'))
            ticketsSold.append(row[1])
        plot.bar(datetimes, ticketsSold, color = 'blue')
        plot.xlabel('DateTime')
        plot.ylabel('TicketsSold')
        plot.show()

def main():

    data_set = 'ticket_sales_data.csv'
    data_subset = 'ticket_sales_data_small_subset.csv'
    plot.scatter
    generateHistogramFrom(data_set)

if __name__ == '__main__':
    main()