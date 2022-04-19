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

#configure this at the bottom
def main(plotfunc):
    #Define needed variables up here for scoping/keeping-track reasons:
    times = []
    rel_improv = []
    #big 'ol list of all level names, for graph title purposes
    level_names = ["Learning to Roll", "Collect the Gems", "Jump Training", "Learn the Super Jump", "Platform Training", "Learn the Super Speed", "Elevator", "Air Movement", "Gyrocopter", "Time Trial", "Super Bounce", "Gravity Helix", "Shock Absorber", "There and Back Again", "Marble Materials Lab", "Bumper Training", "Breezeway", "Mine Field", "Trapdoors!", "Tornado Bowl", "Pitfalls", "Platform Party", "Winding Road", "Grand Finale",
    "Jump Jump Jump", "Monster Speedway Qualifying", "Skate Park", "Ramp Matrix", "Hoops", "Go for the Green", "Fork in the Road", "Tri Twist", "Marbletris", "Space Slide", "Skee Ball Bonus", "Marble Playground", "Hop Skip and a Jump", "Take the High Road", "Half-Pipe", "Gauntlet", "Moto-Marblecross", "Shock Drop", "Spork in the Road", "Great Divide", "The Wave", "Tornado Alley", "Monster Speedway", "Upward Spiral",
    "Thrill Ride", "Money Tree", "Fan Lift", "Leap of Faith", "Freeway Crossing", "Stepping Stones", "Obstacle Course", "Points of the Compass", "Three-Fold Maze", "Tube Treasure", "Slip 'n Slide", "Skyscraper", "Half Pipe Elite", "A-Maze-ing", "Block Party", "Trapdoor Madness", "Moebius Strip", "Great Divide Revisted", "Escher's Race", "To the Moon", "Around the World in 30 seconds", "Will o' the Wisp", "Twisting the night away", "Survival of the Fittest", 
    "Plumber's Portal", "Siege", "Ski Slopes", "Ramps Reloaded", "Tower Maze", "Free Fall", "Acrobat", "Whirl", "Mudslide", "Pipe Dreams", "Scaffold", "Airwalk", "Shimmy", "Path of Least Resistance", "Daedalus", "Ordeal", "Battlements", "Pinball Wizard", "Eye of the Storm", "Dive!", "Tightrope", "Natural Selection", "Tango", "Icarus", "Under Construction", "Pathways", "Darwin's Dilemna", "King of the Mountain"
    ]

    #CSV reading time
    for num in range(1,101): #range func is (inclusive, exclusive), so 1->100 is range(1,101) || Beginner: (1,25), Intermediate (25,49), Advanced (49,100)
        print("---BEGIN CSV TIME FETCHING---")
        with open(f"csvs/{num}.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #We also have runners and dates stored if wanted/needed
                times.append(row['Time'])

            #Convert items in list from strings to floats (only converting to numpy arrays later and then resetting them to plain ol' python lists)
            times = [float(i) for i in times]

        print("---END CSV TIME FETCHING----")
        print("---BEGIN RELATIVE IMPROVEMENT CALCULATION---")

        for num1 in range(0, len(times)):
            rel_change = (times[0] - times[num1])/(times[num1])
            rel_improv.append(rel_change)
        
        print(rel_improv)

        print("---END RELATIVE IMPROVEMENT CALCULATION---")
        print("---BEGIN CREATING PLOTS---")
    
        rel_improv = np.array(rel_improv)
        wr_index = np.arange(0, len(rel_improv))
        level_name = level_names[num - 1]

        if plotfunc != "all" and plotfunc != "composite":
            print("plotfunc != all or composite")
            plt.scatter(wr_index, rel_improv)

        if plotfunc == "polyfit":
            print("plotfunc == polyfit")
            #polyfit line of best fit
            a, b = np.polyfit(wr_index, rel_improv, 1)
            y_linefit = a*wr_index + b
            plt.plot(wr_index, y_linefit, label="1st deg")

            #polyfit 2nd degree curve of best fit
            a, b, c = np.polyfit(wr_index, rel_improv, 2)
            y_2ndcurve = a*pow(wr_index, 2) + b*wr_index + c
            plt.plot(wr_index, y_2ndcurve, label="2nd deg")

            #polyfit 3rd degree curve
            a, b, c, d = np.polyfit(wr_index, rel_improv, 3)
            y_3rdcurve = a*pow(wr_index, 3) + b*pow(wr_index, 2) + c*wr_index + d
            plt.plot(wr_index, y_3rdcurve, label="3rd deg")

            #polyfit 4th degree curve
            a, b, c, d, e = np.polyfit(wr_index, rel_improv, 4)
            y_4thcurve = a*pow(wr_index, 4) + b*pow(wr_index, 3) + c*pow(wr_index, 2) + d*wr_index + e
            plt.plot(wr_index, y_4thcurve, label="4th deg")

            plt.legend(title = "Using np.polyfit")
            plt.xlabel("WR Index")
            plt.ylabel("Relative Improvement")
            plt.title(f"WR History of {level_name}")
            plt.savefig(f"figs/{num}_polyfit.png")
            plt.clf()
        
        #For plotting multiple lines at once e.g. all plots for a specific difficulty
        if plotfunc == "composite":
            print("plotfunc == composite")
            plt.plot(wr_index, rel_improv)
            plt.xlabel("WR Index")
            plt.ylabel("Relative Improvement")

            # Kinda hacky but does work
            if num == 24:
                plt.title("WR History of Beginner MBG Levels")
                plt.savefig("figs/BeginnerILs.png")
                plt.clf()
            if num == 48:
                plt.title("WR History of Intermediate MBG Levels")
                plt.savefig("figs/IntermediateILs.png")
                plt.clf()
            if num == 100:
                plt.title("WR History of Advanced MBG Levels")
                plt.savefig("figs/AdvancedILs.png")
                plt.clf()
            
        #Somewhat repetitive, but saves all 100 level plots onto a single graph, verses splitting by difficulty
        if plotfunc == "all":
            print("plotfunc == all")
            plt.plot(wr_index, rel_improv)
            plt.xlabel("WR Index")
            plt.ylabel("Relative Improvement")
            plt.title("WR History of All MBG Levels")
            if num == 100:
                plt.savefig("figs/All100ILs.png")

        
        #reset values
        times = []
        rel_improv = []

#old testing function, probably deserves to be thrown into the dumping ground!
def relative_improvement_testfunc():
    print("test")
    times = [3.999,3.89,3.266,3.074,3.069,3.049,2.985,2.984,2.402,2.37,2.333,2.287,2.281,2.267,2.25,2.236,2.226]
    rel_improv = []

    for num in range(0, len(times)):
        rel_change = (times[0] - times[num])/(times[num])
        rel_improv.append(rel_change)
        
    print(len(times))
    print(len(rel_improv))
    print(rel_improv)

#configure the variables
"""
Current options:
polyfit: Creates scatter graph for each level, adds lines/curves of best fit (up to 4th degree) using np.polyfit method

composite: Creates a composite plot of all Beginner, Intermediate and Advanced levels on separate plots (i.e. 3 graphs)
all: Similar to composite, but all 100 levels are on one graph
"""
if __name__ == "__main__":
    main("composite")