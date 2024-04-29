import stddraw
import math

def isAllowed(player):
    if player["time"] > player["missileS"]:
        player["time"] = 0
        return True
    else:
        return False



def createMissiles(missiles,typ,aimDir):

    #create list for missile x and y positions
    x = [miss["x"] for miss in missiles]
    y = [miss["y"] for miss in missiles]
    if typ == 1:
        #creates missile of type 1
        stddraw.setPenColor(stddraw.BLACK)

        #go through list of missile coordinates and make missiles
        for i in range(len(x)):
            stddraw.filledCircle(x[i],y[i],1)


#def moveM(x,y,screenX,screenY,direc):
def moveM(missiles,screenX,screenY):

    #speed of missiles
    speed = 4

    #num op missiles
    count = len(missiles)
    i = 0
    #itterate through all missiles
    while i < count and count != 0:
        pos = i

        #create list for direction of all the missiles
        direc = [miss["dir"] for miss in missiles]
        
        #change x pos
        missiles[pos]["x"] = missiles[pos]["x"] + (speed*(direc[pos]/(math.pi/2)))

        #change y pos
        missiles[pos]["y"] = missiles[pos]["y"] + (speed*(1-abs(direc[pos]/(math.pi/2))))


        #Check if missile x is in the screen bounds
        if missiles[pos]["x"] > screenX-6 or missiles[pos]["x"] < -screenX+6:
            #remove missile
            missiles.pop(pos)

            #adjust list after removing missile
            count = count-1

        #Check if missile y is in the screen bounds
        elif missiles[pos]["y"] > screenY-8 or missiles[pos]["y"] < -screenY+8:
            #remove missile
            missiles.pop(pos)
            #adjust list after removing missile
            count = count-1
        else:
            #Go to next missile    
            i += 1



    #return new x,y of missiles
    return missiles

