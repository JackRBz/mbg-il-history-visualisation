#from turtle import color
import matplotlib.pyplot as plt
import numpy as np
#import itertools
from datetime import date
import csv

def main():
    print("main func")

    ##functions appended with testfunc are experimental functions exploring tests, not for final use
    #plot_hardcoded_data_testfunc()
    #read_from_csv_testfunc()
    timedelta_testfunc()

def plot_hardcoded_data_testfunc():
    print("This is the plotting testfunc")
    ##Full values (of winding road, B23 in this instance)
    y_values = [12.839,11.629,10.375,10.35,10.325,10.312,10.29,10.25,10.233,10.209,10.203,10.202,10.186,10.155,10.149,10.124,10.093,9.915,9.880,9.875,9.778,9.749,9.678,9.657]
    x_values = ["2004-08-04","2005-08-30","2006-02-26","2006-02-26","2006-06-XX","2006-08-25","2007-10-24","2007-10-25","2007-10-25","2007-10-25","2009-01-18","2009-01-18","2009-01-18","2011-08-20","2013-11-15","2014-08-06","2014-08-12","2019-03-06","2020-04-13","2020-04-15","2020-04-16","2020-04-25","2020-04-25","2021-08-25"]
    #might be better to convert dates into discrete values, i.e. days since the first wr
    #Plotting scatter, showing graph
    #TODO: Work out how to do itertools to cycle through colours
    plt.scatter(x_values,y_values, color="r")
    #Editing graph visual data
    plt.xticks(rotation=75) #Change label rotation, to make it properly visible
    #Labels+Title
    plt.xlabel("Date (YYYY-MM-DD")
    plt.ylabel("Time")
    plt.title("Winding Road IL Record History")
    #Showing and saving for testing purposes
    plt.savefig('tempgraph.png')
    plt.show()

def timedelta_testfunc():
    print("This is the timedelta testfunc")
    #TODO: Do find out how to calculate time delta
    #https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
    #Procedure: If day is missing, should I edit the csv or edit on the fly? And what day, default to 01?
    date_values_full_list = ["2004-08-04","2005-08-30","2006-02-26","2006-02-26","2006-06-XX","2006-08-25","2007-10-24","2007-10-25","2007-10-25","2007-10-25","2009-01-18","2009-01-18","2009-01-18","2011-08-20","2013-11-15","2014-08-06","2014-08-12","2019-03-06","2020-04-13","2020-04-15","2020-04-16","2020-04-25","2020-04-25","2021-08-25"]
    d1 = date_values_full_list[0]
    print(d1)
    d2 = date_values_full_list[1]
    print(d2)
    ##Need to convert string dates into split numbers? cannot use int func, use string slices to extract YYYY-MM-DD separately?
    # print(d1[:4]) #The year
    # print(d1[5:7]) #The month
    # print(d1[-2:]) #The day
    d1_year, d1_month, d1_day = d1[:4], d1[5:7], d1[-2:]
    d2_year, d2_month, d2_day = d2[:4], d2[5:7], d2[-2:]




def read_from_csv_testfunc():
    print("this is reading from csv file testfunc")
    with open('test.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row['Column1'], row['Column2'], row['Column3'])
            row1, row2, row3 = row['Column1'], row['Column2'], row['Column3']
            print(row1, row2, row3) #Damn can't believe this actually works!!


print("not in main func")

## Writeup of the steps needed to create the necessary program

#Step 1: Getting the MBG IL data from the shared spreadsheet and, eventually into a csv file (try hardcoding it first?)
#Note: Will likely scrape an interesting individual level (or a couple) and use as example, extend to all levels in due time
#Note2:- Listing the number of WR changes i.e. number of changes to pick a representative? ones
""" Note: (-3) indicates number of wr changeovers removed due to banned glitch
Dated: 15/04/2022
B1: 17, B2: 24, B3: 20, B4: 21, B5: 11 (-3), B6: 18, B7: 20 (-2), B8: 16, B9: 24, B10: 28, B11: 30, B12: 26, B13: 25, B14: 21, B15: 13, B16: 15, B17: 17, B18: 23, B19: 30, B20: 17, B21: 25, B22: 16, B23: 24, B24: 33
Average changes: 514/24 ~= 21.41666 -> Pick Winding Road?
I1: 32, I2: 17, I3: 40, I4: 33, I5: 22 (-1), I6: 15, I7: 17, I8: 29, I9: 30, I10: 13 (-3), I11: 21, I12: 53, I13: 16, I14: 24, I15: 28, I16: 20, I17: 22, I18: 16, I19: 28, I20: 13 (-1), I21: 18, I22: 15, I23: 14, I24: 21
Average changes: 557/24 ~= 23.208333 -> Pick I14?
A1: 20, A2: 23 (-1), A3: 19, A4: 18, A5: 13 (-2), A6: 27, A7: 11 (-1), A8: 20, A9: 20, A10: 22, A11: 17, A12: 20 (-1), A13: 15, A14: 24, A15: 25, A16: 24, A17: 22, A18: 15, A19: 27, A20: 19, A21: 11, A22: 20, A23: 20, A24: 13, A25: 22, A26: 17, A27: 23, A28: 29, A29: 13 (-2), A30: 15, A31: 15, A32: 25, A33: 17, A34: 21, A35: 12, A36: 25, A37: 21, A38: 24, A39: 27, A40: 19 (-1), A41: 21, A42: 30, A43: 22, A44: 10, A45: 31, A46: 20, A47: 15, A48: 28, A49: 14, A50: 31 (-1), A51: 17, A52: 22 (-2)
Average changes: 1051/52 ~= 20.211538... -> Pick A1? Thrill Ride
"""

#Step 1.25 Get data into a csv file and get python to read from that instead

#Step 1.5: Determine if any data cleanup is needed (been thinking about using dates vs. just plotting date since Michael McFadden's times)

#Step 2: Determine the best plotting function/graphing function for this data e.g. scatter function, step function
#Note: Are there other types of plotting functions that might be useful?

#Step 3: Determine a line/curve of best fit for these data points
#Note: A curve fitting must be decreasing linearly, at least, 

#Step ???: Work out important speedrunning events/discoveries, for example WRR's releasing, new startpad tricks discovered, TAS beginnings

if __name__ == "__main__":
    main()