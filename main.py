import matplotlib.pyplot as plt
import numpy as np

def main():
    print("main func")
    x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
    plt.plot(x, np.sin(x))       # Plot the sine of each x point
    plt.show() 

print("not in main func")

## Writeup of the steps needed to create the necessary program

#Step 1: Getting the MBG IL data from the shared spreadsheet and into a plain csv file
#Note: Will likely scrape an interesting individual level (or a couple) and use as example, extend to all levels in due time
#Note2:- Listing the number of WR changes i.e. number of changes to pick a representative? ones
""" Note: (-3) indicates number of wr changeovers removed due to banned glitch
Dated: 15/04/2022
B1: 17, B2: 24, B3: 20, B4: 21, B5: 11 (-3), B6: 18, B7: 20 (-2), B8: 16, B9: 24, B10: 28, B11: 30, B12: 26, B13: 25, B14: 21, B15: 13, B16: 15, B17: 17, B18: 23, B19: 30, B20: 17, B21: 25, B22: 16, B23: 24, B24: 33
Average changes: 514/24 ~= 21.41666 -> Pick Winding Road?
I1: 32, I2: 17, I3: 40, I4: 33, I5: 22 (-1), I6: 15, I7: 17, I8: 29, I9: 30, I10: 13 (-3), I11: 21, I12: 53, I13: 16, I14: 24, I15: 28, I16: 20, I17: 22, I18: 16, I19: 28, I20: 13 (-1), I21: 18, I22: 15, I23: 14, I24: 21
Average changes: 557/24 ~= 23.208333 -> Pick I18?
A1: 20, A2: 23 (-1), A3: 19, A4: 18, A5: 13 (-2), A6: 27, A7: 11 (-1), A8: 20, A9: 20, A10: 22, A11: 17, A12: 20 (-1), A13: 15, A14: 24, A15: 25, A16: 24, A17: 22, A18: 15, A19: 27, A20: 19, A21: 11, A22: 20, A23: 20, A24: 13, A25: 22, A26: 17, A27: 23, A28: 29, A29: 13 (-2), A30: 15, A31: 15, A32: 25, A33: 17, A34: 21, A35: 12, A36: 25, A37: 21, A38: 24, A39: 27, A40: 19 (-1), A41: 21, A42: 30, A43: 22, A44: 10, A45: 31, A46: 20, A47: 15, A48: 28, A49: 14, A50: 31 (-1), A51: 17, A52: 22 (-2)
Average changes: 1051/52 ~= 20.211538... -> Pick A1? Thrill Ride
"""

#Step 1.5: Determine if any data cleanup is needed (been thinking about using dates vs. just plotting date since Michael McFadden's times)

#Step 2: Determine the best plotting function/graphing function for this data e.g. scatter function, step function
#Note: Are there other types of plotting functions that might be useful?

#Step 3: Determine a line/curve of best fit for these data points
#Note: A curve fitting must be decreasing linearly, at least, 

#Step ???: Work out important speedrunning events/discoveries, for example WRR's releasing, new startpad tricks discovered, TAS beginnings

if __name__ == "__main__":
    main()