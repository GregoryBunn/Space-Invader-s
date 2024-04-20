import stddraw, math, time, random, startScreen, ship, alien, audioTest, threading, stars, gameModes

#Start Canvas Setup
stddraw.setCanvasSize(660, 660)
stddraw.setXscale(-2.0, 2.0)
stddraw.setYscale(-2.0, 2.0) 
startScreen.startScreen()    
#________________________________________________________________________#

#Variables for tracking gameplay
def main():
    difficulty = 1
    while True:
        difficulty += gameModes.default(difficulty)
if __name__=="__main__": main()
