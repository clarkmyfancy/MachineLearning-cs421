import csv
import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plot 
import numpy as np 

import math 
from sklearn.linear_model import LogisticRegression

def generateHistogramFrom(data):
    with open(data) as d:
        CsvData = csv.reader(d, delimiter = ',')
        datetime = []
        ticketsSold = []
        for i, row in enumerate(CsvData):
            # skip first row (contains feature titles)
            if i == 0:
                continue
            datetime.append(row[0])
            ticketsSold.append(row[1])
        plot.plot_date(datetime, ticketsSold, color = 'blue')
        plot.xlabel('DateTime')
        plot.ylabel('TicketsSold')
        plot.show()

def main():

    data_set = 'ticket_sales_data.csv'
    plot.scatter
    generateHistogramFrom(data_set)

if __name__ == '__main__':
    main()