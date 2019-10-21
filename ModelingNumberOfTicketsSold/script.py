import csv
import matplotlib.pyplot as plot 
import numpy as np 
import pandas as pd 
import math 
from sklearn.linear_model import LogisticRegression

def main():

    data_set = 'ticket_sales_data.csv'
    data = pd.read_csv(data_set, header = None)

if __name__ == '__main__':
    main()