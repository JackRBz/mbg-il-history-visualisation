# Basic visualisation of the speedrunning history of Marble Blast Gold

This is a small amount of python code, used to take in csv data and produce various figures using matplotlib plotting, along with some lines/curves of best fit for the data. This was a) an excuse to play around with python, more specifically numpy and matplotlib, over the long Easter weekend of 2022 and b) A geniune curiosity to see how a games speedrunning history, for a game released back in 2003, would look like on a graph.

All data has been sourced from the community, more specifically this spreadsheet here: https://docs.google.com/spreadsheets/d/1Dj1HEUXkyALK8qCAuzAEetnvJhvJjWBxd1Nr5GR5CYc/edit#gid=0 

This data (with a few adjustments) can be found in the csv folder, where 1.csv represents the speedrun history data for the first MBG level, Learning to Roll.
Graphs can be found in the figs folder, with further subdivisions showing different lines/curves of best fit, as well as a few graphs plotting multiple levels all on the same graph.

Files such as dumping_ground.py are for personal future reference.

## FAQ: Past me to Future me

### I want to run this again, how do I do it?
  Need to install python (I used python 3.9 for this mini-project), set up an appropriate python environment (venv) and install packages.
  
  Python installations can be found on python.org.
  Python then can be set up in an IDE e.g. VSCode, and packages can then be installed post-environment setup.
  To set up in VSCode
  1. Select Python Interpreter (recent python installation)
  2. Run py -3 -m venv .venv in VSCode terminal
  3. install necessary packages: matplotlib, numpy, sklearn

### Why use WR Index vs. Relative Improvement as axes rather than <insert others here>?
  I initially used date vs. time as axes, and then replaced date with a 'days since 2004-08-04' (the release of Michael McFadden's Gold Time Guide, and the 'genesis' of MBG Speedrunning, so to speak), however I found these to be poor axes.
  Other axes I may not have thought of, so I cannot attest to their usefulness.
  To be honest, I copied what was used at the bottom of this article (https://www.lesswrong.com/posts/nhjaegqWxbBhiqMGS/analysis-of-world-records-in-speedrunning-linkpost -> which inspired me to do this whole mini-project in the first place!), after realising the futility of any axes I was using.

### Why not extend to other Marble Blast games/fanmods such as Marble Blast Ultra or Marble Blast Platinum? Or even other games entirely unrelated?
  Can absolutely be done, if I'm able to get data into a nice format. All the leaderboard history for MBPlatinum, or PlatinumQuest etc. do exist, however I'd need to work out/write a webscraper and produce a way, programmatically, to reduce all the times ever recorded on any given level to just the ones that were, at one point, WRs. It can be done, but I do not fancy doing this at the moment.
  
  As for other games, I'm not really sure why not, other than I have a significant personal connection to MBG and other Marble Blast games, and a lot of other games I play I'm not too wholly insterested in speedrunning, hence I am less inclined.
  
### What further work could be done for this small project?
  Explore other potential viable plots, or even just resizing plots (e.g. log plots)
  Look at expanding data sets to encompass more games (although without having an easy to use datasource to hand, this will entail much more work)
  Restructure code a little more to be more modular and reusable than just throwing everything into main.py.
