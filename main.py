"""
Sudden realisation that the data I'm using i.e. raw time vs. date since first WR might not be good for multiple reasons
1. Dates are poor predictive variables, due to various reasons:
a. New techniques and new paths are found in irregular intervals, I'd conjecture totally random (or very weak correlation at best, not that we can practically test this theory anyway)
b. Natural ebb and flow of how and when wr's are beaten, due to the above and the release of WRRs at, somewhat regular intervals?
c. Some levels, such as Traplaunch levels, are also essentially random in when times are set and beaten (see SotF for a prime example)
There are other, probably better reasons, but I think date is a poor predictor and so shouldn't be used in analysis (plus reconstructing 10+ years of history is difficult, and hence some dates are guesses/incomplete data)
The alternative I will use is much easier, indexing by id instead

The raw time is somewhat of an issue as well, given how WRs tend to be relatively, extremely unoptimised, and they monotonically increase in optimisation, either through brute force improvements or new techniques.
So why not plot the relative improvement instead? It will, hopefully, better represent what's going on, and focus on how the community has improved times, relative to its rather humble start.
That and it means that my graphs will all be monotonically increasing vs. decreasing, which is likely going to play with plotting algorithms better :)

My experimentations with functions and code will not go to waste, as they all needed to be rewritten into a coherent whole anyway :D
It will makes this file extrodinarily long with bloat though, and past me can only apologise, in advance, to future me.

Calculating relative improvement shouldn't be too difficult though, it will merely be:
(time2 - time1)/time1 -> note time1 > time2, so this will all need to be negated

For example, in Learning To Roll:
First WR: 3.999
Last WR: 2.226
(2.226-3.999)/3.999 = -0.443... a -44% increase, or a 44% percent `improvement` (cut) from the first to last time
I can simply calculate the negative increases, then double negative them
The improvement from the first wr to first wr though will need to be 0, what is -0 in python?

All scratch-pad/experimental code written before this realisation will be cut-and-pasted into dumping_ground.py
Further experimental code will be written, but I have the structure roughly in my head, will be worth nailing down proper though!
"""

#from turtle import color
import matplotlib.pyplot as plt
import numpy as np
#import itertools
from datetime import date
import csv
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.isotonic import IsotonicRegression
from scipy import interpolate

def main():
    print("its bare here now!!")


if __name__ == "__main__":
    main()