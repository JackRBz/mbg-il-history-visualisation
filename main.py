#from turtle import color
import matplotlib.pyplot as plt
import numpy as np
#import itertools
from datetime import date
import csv
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def main():
    print("main func")

    ##functions appended with testfunc are experimental functions exploring tests, not for final use
    #plot_hardcoded_data_testfunc()
    #read_from_csv_testfunc()
    #timedelta_testfunc()
    #timedelta_loop_testfunc()
    #read_from_multiple_csvs_testfunc()
    matplotlib_styling_testfunc()

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
    d3 = date_values_full_list[2]
    ##Need to convert string dates into split numbers? cannot use int func, use string slices to extract YYYY-MM-DD separately?

    #We also need a culmulative days counter, starting from 0
    days_culmulative_sum = 0

    d1_year, d1_month, d1_day = int(d1[:4]), int(d1[5:7]), int(d1[-2:])
    d2_year, d2_month, d2_day = int(d2[:4]), int(d2[5:7]), int(d2[-2:])
    d3_year, d3_month, d3_day = int(d3[:4]), int(d3[5:7]), int(d3[-2:])
    d1_date = date(d1_year, d1_month, d1_day)
    d2_date = date(d2_year, d2_month, d2_day)
    d3_date = date(d3_year, d3_month, d3_day)
    #calculate the delta, in days, between dates
    delta_d2d1 = d2_date - d1_date # later date first, avoid negatives
    delta_d2d1_int = int(delta_d2d1.days) #convert datetime.timedelta into an int, needed for plotting
    days_culmulative_sum += delta_d2d1_int
    print(days_culmulative_sum)
    #repeat process manually for d3-d2, but with culmulative sum
    delta_d3d2 = d3_date - d2_date
    delta_d3d2_int = int(delta_d3d2.days)
    delta_d3d2_int_culm = delta_d3d2_int + delta_d2d1_int
    days_culmulative_sum += delta_d3d2_int
    print(days_culmulative_sum)

    x_values_short = [12.839,11.629,10.375]
    y_values_short = [0, delta_d2d1_int, delta_d3d2_int_culm]
    plt.plot(y_values_short, x_values_short)
    plt.xlabel("Days since 2004-08-04 (Michael McFadden's Gold Time Guide Release Date)")
    plt.ylabel("Time")
    plt.savefig('tempgraph_timedelta.png')
    plt.show()

def timedelta_loop_testfunc():
    print("This is 2nd timedelta testfunc, experimenting with looping through larger data sample")
    #Question, how will this work when the delta is zero? hmmmm
    #I also need to make include a 'culmulative delta' variable like above
    #Use len as the looping parameter
    #Note we need 2 dates to calculate each delta, n-1 and n, or n and n+1

    # Replacing XX with an actual date, temp replacing it with 01
    raw_dates_needs_processing = ["2004-08-04","2005-08-30","2006-02-26","2006-02-26","2006-06-XX","2006-08-25","2007-10-24","2007-10-25","2007-10-25","2007-10-25","2009-01-18","2009-01-18","2009-01-18","2011-08-20","2013-11-15","2014-08-06","2014-08-12","2019-03-06","2020-04-13","2020-04-15","2020-04-16","2020-04-25","2020-04-25","2021-08-25"]
    raw_dates = ["2004-08-04","2005-08-30","2006-02-26","2006-02-26","2006-06-01","2006-08-25","2007-10-24","2007-10-25","2007-10-25","2007-10-25","2009-01-18","2009-01-18","2009-01-18","2011-08-20","2013-11-15","2014-08-06","2014-08-12","2019-03-06","2020-04-13","2020-04-15","2020-04-16","2020-04-25","2020-04-25","2021-08-25"]

    x_values = [0]
    y_values = [12.839,11.629,10.375,10.35,10.325,10.312,10.29,10.25,10.233,10.209,10.203,10.202,10.186,10.155,10.149,10.124,10.093,9.915,9.880,9.875,9.778,9.749,9.678,9.657]
    days_culm = 0

    for index in range(len(raw_dates) - 1):
        print(raw_dates[index])
        d0_year, d0_month, d0_day = int(raw_dates[index][:4]), int(raw_dates[index][5:7]), int(raw_dates[index][-2:])
        d1_year, d1_month, d1_day = int(raw_dates[index+1][:4]), int(raw_dates[index+1][5:7]), int(raw_dates[index+1][-2:])
        d0_date = date(d0_year, d0_month, d0_day)
        d1_date = date(d1_year, d1_month, d1_day)
        delta = d1_date - d0_date

        delta_temp = int(delta.days)
        delta_culm = days_culm + delta_temp
        x_values.append(delta_culm)

        days_culm += delta_temp

    print(x_values)
    
    plt.plot(x_values, y_values)
    plt.xlabel("Days since 2004-08-04")
    plt.ylabel("Time")
    plt.savefig("tempgraph_timedelta_loop.png")
    plt.show()
   
def read_from_csv_testfunc():
    print("this is reading from csv file testfunc")
    with open('test.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row['Column1'], row['Column2'], row['Column3'])
            row1, row2, row3 = row['Column1'], row['Column2'], row['Column3']
            print(row1, row2, row3) #Damn can't believe this actually works!!

def read_from_multiple_csvs_testfunc():
    print("multiple csv's? testfunc")
    #hardcoding this for now, not great but it makes this easier
    for num in range(1,4): #range function is (inclusive, exclusive)
        with open(f"csvs/{num}.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            runner, time, date = [], [], []
            for row in reader:
                runner.append(row['Runner'])
                time.append(row['Time'])
                date.append(row['Date'])
                #runner, time, date = row['Runner'], row['Time'], row['Date']
                #print(runner, time, date)

            #This stores each column, but is overwritten after iterating
            print(runner)
            print(time)
            print(date)

def matplotlib_styling_testfunc():
    print("this is the matplotlib testfunc")

    #placeholder values, calculated beforehand
    #hmm, do I need to make this a numpy array
    x_values = np.array([0, 391, 571, 571, 666, 751, 1176, 1177, 1177, 1177, 1628, 1628, 1628, 2572, 3390, 3654, 3660, 5327, 5731, 5733, 5734, 5743, 5743, 6230])
    y_values = np.array([12.839,11.629,10.375,10.35,10.325,10.312,10.29,10.25,10.233,10.209,10.203,10.202,10.186,10.155,10.149,10.124,10.093,9.915,9.880,9.875,9.778,9.749,9.678,9.657])

    #line of best fit? not curve! y = ax + b
    #I also think polyfit is deprecated but uh /shrug
    """ #Commenting this out because I'm testing higher polynomial curves
    a, b = np.polyfit(x_values, y_values, 1)
    print(a, b)
    plt.scatter(x_values, y_values, color='green')
    plt.plot(x_values, y_values)
    y_line_fit = a*x_values+b #put line in variable
    plt.plot(x_values, y_line_fit, color='steelblue', linestyle='--', linewidth=2)
    #Displaying the text of the line of best fit is a massive faff ngl
    plt.text(x_values[len(x_values) - (len(x_values)//2)], y_values[0], 'y = ' + '{:.2f}'.format(b) + ' + {:.2f}'.format(a) + 'x', size=10)
    plt.savefig("matplotlib_styling_tests_scatter_linebestfit.png")
    plt.show()
    """

    #Let's try a curve of best fit? 2nd poly => y = ax^2 + bx + c
    """
    a, b, c = np.polyfit(x_values, y_values, 2)
    print(a, b, c)
    plt.scatter(x_values, y_values, color='green')
    y_curve_fit = a*pow(x_values, 2) + b*x_values + c
    plt.plot(x_values, y_curve_fit, color='red', linestyle='--', linewidth=2)
    plt.savefig("matplotlib_styling_tests_scatter_curvebestfit.png")
    #plt.show()
    """

    #Curve, 3rd poly: y = ax^3 + bx^2 + cx + d
    #Odd polynomials are probably not very good, for monotonically decreasing curvefitting
    """
    a, b, c, d = np.polyfit(x_values, y_values, 3)
    print(a, b, c, d)
    plt.scatter(x_values, y_values, color='green')
    y_curve3_fit = a*pow(x_values, 3) + b*pow(x_values, 2) + c*x_values + d
    #plt.plot(x_values, y_curve3_fit, color='red', linestyle='--', linewidth=2)
    plt.savefig("matplotlib_styling_tests_scatter_curve3bestfit.png")
    #plt.show()
    """

    #4th degree polynomial gives leads to too-large numbers for the days e.g. 6000^4 = 1.296x10^15!!
    #Reversing x/y values would maybe work, although may run into floating point issues?
    #e.g. 11.629^4 = 18288.137658116881.... which is far smaller but has large remainder


    #Linear regression using sklearn? worth exploring
    x_values_lr = x_values.reshape(-1, 1)
    model = LinearRegression()
    #I need to refit to make this work -> save as a variable rather than do inline?
    # model.fit(x_values.reshape(-1, 1), y_values)
    model.fit(x_values_lr, y_values)

    #I can use model.predict for x values to predict y values i.e. days in future to predict a time value
    #print(model.predict([[7000]])) #7000 days after 2004/08/04 is 2023/10/04, prediction of 9.458


    #Potential TODO: Explore the reverse? have a time and predict when that may be achieved given past achievements? hmm
    sklearn_best_fit = model.predict(x_values_lr)
    print(f'The parameters of the line: {model.coef_}')

    #All potential methods for this model: fit, get_params, predict, score, set_params
    #print(model.get_params()) #prints params or the gradient: -0.00019086
    #print(model.score(x_values_lr, y_values)) #returns R^2 score: 0.391417 (not a great model, not surprised a linear model is poor for this)
    """
    plt.scatter(x_values, y_values, color='green')
    plt.plot(x_values, sklearn_best_fit)
    plt.savefig("matplotlib_styling_tests_sklearn_ln.png")
    plt.show()
    """
    #TODO: does sklearn allow for higher polynomial stuff?
    #or this to be honest https://data36.com/polynomial-regression-python-scikit-learn/
    #polynomial regression time!

    #This is going to repeated code, up to degree 10, purely for testing purposes pretty much
    """
    poly = PolynomialFeatures(degree=2, include_bias=False) #using 2 degree poly using scikit/sk
    poly_features = poly.fit_transform(x_values_lr)
    model.fit(poly_features, y_values)
    y_predict = model.predict(poly_features)
    print(y_predict)
    
    plt.scatter(x_values, y_values, color='green')
    plt.plot(x_values, y_predict)
    #plt.savefig("matplotlib_styling_tests_sklearn_poly")
    #plt.show()

    poly3 = PolynomialFeatures(degree=3, include_bias=False)
    poly3_features = poly3.fit_transform(x_values_lr)
    model.fit(poly3_features, y_values)
    y3_predict = model.predict(poly3_features)
    print(y3_predict)

    #plt.scatter(x_values, y_values, color='green')
    #plt.plot(x_values, y3_predict)
    plt.savefig("matplotlib_styling_tests_sklearn_poly3")
    #plt.show()

    poly4 = PolynomialFeatures(degree=4, include_bias=False)
    poly4_features = poly4.fit_transform(x_values_lr)
    model.fit(poly4_features, y_values)
    y4_predict = model.predict(poly4_features)
    print(y4_predict)

    #plt.scatter(x_values, y_values, color='green')
    #plt.plot(x_values, y4_predict)
    plt.savefig("matplotlib_styling_tests_sklearn_poly4")
    #plt.show()

    poly5 = PolynomialFeatures(degree=5, include_bias=False)
    poly5_features = poly5.fit_transform(x_values_lr)
    model.fit(poly5_features, y_values)
    y5_predict = model.predict(poly5_features)
    print(y5_predict)

    #plt.scatter(x_values, y_values, color='green')
    #plt.plot(x_values, y5_predict)
    plt.savefig("matplotlib_styling_tests_sklearn_poly5")
    #plt.show()

    poly6 = PolynomialFeatures(degree=6, include_bias=False)
    poly6_features = poly6.fit_transform(x_values_lr)
    model.fit(poly6_features, y_values)
    y6_predict = model.predict(poly6_features)
    print(y6_predict)

    #plt.scatter(x_values, y_values, color='green')
    #plt.plot(x_values, y6_predict)
    plt.savefig("matplotlib_styling_tests_sklearn_poly6")
    #plt.show()

    poly7 = PolynomialFeatures(degree=7, include_bias=False)
    poly7_features = poly7.fit_transform(x_values_lr)
    model.fit(poly7_features, y_values)
    y7_predict = model.predict(poly7_features)
    print(y7_predict)

    #plt.scatter(x_values, y_values, color='green')
    #plt.plot(x_values, y7_predict)
    plt.savefig("matplotlib_styling_tests_sklearn_poly7")
    #plt.show()

    poly8 = PolynomialFeatures(degree=8, include_bias=False)
    poly8_features = poly8.fit_transform(x_values_lr)
    model.fit(poly8_features, y_values)
    y8_predict = model.predict(poly8_features)
    print(y8_predict)

    #plt.scatter(x_values, y_values, color='green')
    #plt.plot(x_values, y8_predict)
    plt.savefig("matplotlib_styling_tests_sklearn_poly8")
    #plt.show()

    poly9 = PolynomialFeatures(degree=9, include_bias=False)
    poly9_features = poly9.fit_transform(x_values_lr)
    model.fit(poly9_features, y_values)
    y9_predict = model.predict(poly9_features)
    print(y9_predict)

    #plt.scatter(x_values, y_values, color='green')
    #plt.plot(x_values, y9_predict)
    plt.savefig("matplotlib_styling_tests_sklearn_poly9")
    #plt.show()

    poly10 = PolynomialFeatures(degree=10, include_bias=False)
    poly10_features = poly10.fit_transform(x_values_lr)
    model.fit(poly10_features, y_values)
    y10_predict = model.predict(poly10_features)
    print(y10_predict)

    #plt.scatter(x_values, y_values, color='green')
    plt.plot(x_values, y10_predict)
    plt.savefig("matplotlib_styling_tests_sklearn_poly10")
    plt.show()
    """
    #END basic polynomialFeatures stuff
    #TODO? can I enforce line fit to be monotonically decreasing? if so how?

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