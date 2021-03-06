import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.isotonic import IsotonicRegression

#configure this at the bottom of the file!
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
            rel_change = round(rel_change, 3)
            rel_improv.append(rel_change)
        
        print(rel_improv)

        print("---END RELATIVE IMPROVEMENT CALCULATION---")
        print("---BEGIN CREATING PLOTS---")
    
        rel_improv = np.array(rel_improv)
        wr_index = np.arange(0, len(rel_improv))
        wr_index_fix = wr_index.reshape(-1, 1)
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
            plt.savefig(f"figs/polyfit/{num}_polyfit.png")
            plt.clf()

        if plotfunc == "sklearn":
            print("plotfunc == sklearn")
            #Starting linear regression model
            model = LinearRegression()
            model.fit(wr_index_fix, rel_improv)
            lr_best_fit = model.predict(wr_index_fix)
            print(f'The parameters of the line: {model.coef_}')
            plt.plot(wr_index, lr_best_fit, label="Linear Regression")

            #Starting Polynomial Features modelling, 2 to 4
            poly2 = PolynomialFeatures(degree=2, include_bias=False)
            poly2_features = poly2.fit_transform(wr_index_fix)
            model.fit(poly2_features, rel_improv) 
            y2_predict = model.predict(poly2_features)
            plt.plot(wr_index, y2_predict, label="2nd Degree")

            poly3 = PolynomialFeatures(degree=3, include_bias=False)
            poly3_features = poly3.fit_transform(wr_index_fix)
            model.fit(poly3_features, rel_improv)
            y3_predict = model.predict(poly3_features)
            plt.plot(wr_index, y3_predict, label="3rd Degree")

            poly4 = PolynomialFeatures(degree=4, include_bias=False)
            poly4_features = poly4.fit_transform(wr_index_fix)
            model.fit(poly4_features, rel_improv)
            y4_predict = model.predict(poly4_features)
            plt.plot(wr_index, y4_predict, label="4th Degree")

            plt.legend(title = "Using sklearn")
            plt.xlabel("WR Index")
            plt.ylabel("Relative Improvement")
            plt.title(f"WR History of {level_name}")
            plt.savefig(f"figs/sklearn/{num}_sklearn.png")
            plt.clf()

        if plotfunc == "sklearn_isotonic":
            print("plotfunc == sklearn_isotonic")
            model = IsotonicRegression()
            ir_best_fit = model.fit_transform(wr_index_fix, rel_improv)
            print(ir_best_fit)

            plt.plot(wr_index, ir_best_fit, label="Isotonic Reg")
            plt.xlabel("WR Index")
            plt.ylabel("Relative Improvement")
            plt.title(f"WR History of {level_name}")
            plt.savefig(f"figs/sklearn_ir/{num}_sklearn_ir.png")
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

#configure the variables
"""
Current options:
polyfit: Creates scatter graph for each level, adds lines/curves of best fit (up to 4th degree) using np.polyfit method
sklearn: Similar to polyfit, only using LinearRegression and Polynomial Features for lines
sklearn_isotonic: Similar to sklearn, only using IsotonicRegression instead

composite: Creates a composite plot of all Beginner, Intermediate and Advanced levels on separate plots (i.e. 3 graphs)
all: Similar to composite, but all 100 levels are on one graph
"""
if __name__ == "__main__":
    main("sklearn_isotonic")