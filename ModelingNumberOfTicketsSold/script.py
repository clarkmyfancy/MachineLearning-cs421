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

def getFirstMonthsSales(data):
     with open(data) as d:
        CsvData = csv.reader(d, delimiter = ',')
        datetimes = []
        ticketsSold = []
        endDatetime = datetime.strptime('25-09-2012 00:00', '%d-%m-%Y %H:%M')
        for i, row in enumerate(CsvData):
            # skip first row (contains feature titles)
            if i == 0:
                continue

            currentRowDatetime = datetime.strptime(row[0], '%d-%m-%Y %H:%M')
            if currentRowDatetime >= endDatetime:
                break
            datetimes.append(currentRowDatetime)
            ticketsSold.append(int(row[1]))
        plot.bar(datetimes, ticketsSold, color = 'blue')
        plot.xlabel('DateTime')
        plot.ylabel('TicketsSold')
        plot.show()
            

def main():

    data_set = 'ticket_sales_data.csv'
    data_subset = 'ticket_sales_data_small_subset.csv'
    # generateHistogramFrom(data_set)

    # first_month_sales = getFirstMonthsSales(data_set)
    getFirstMonthsSales(data_set)

if __name__ == '__main__':
    main()