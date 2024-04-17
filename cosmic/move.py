#moving objects 
import objects, math

def shooter(Sinfo):
    wind = objects.screen()

    Sinfo.xPos = Sinfo.xPos + (Sinfo.sDir)*(Sinfo.vx)

    #checking bounds & stopping
    if abs(Sinfo.xPos) > (wind.x - Sinfo.rad):
        Sinfo.sDir = 0

    return Sinfo.xPos

def aim(Ainfo):
    angleR = 0.5 #movement speed
    Ainfo.aDir = Ainfo.aDir + Ainfo.aMov*angleR

    #checking bounds
    if (Ainfo.aDir < -(math.pi /2)): Ainfo.aDir = -(math.pi /2)
    elif (Ainfo.aDir > (math.pi /2)): Ainfo.aDir = (math.pi /2)

    return Ainfo.aDir

def missile(mList):
    wind = objects.screen()
    #loop through missile list
    i = 0
    m = len(mList)
    while i<m and m!=0:
        #change x and y
        mList[i].xPos = mList[i].xPos + mList[i].sp*(mList[i].direc/(math.pi/2))
        mList[i].yPos = mList[i].yPos + mList[i].sp*(1-abs(mList[i].direc/(math.pi/2)))

        
        #remove missile if outofbounds
        #xbounds
        if(abs(mList[i].xPos)> (wind.x+mList[i].rad)):
            del mList[i]
            m -= 1 
        #ybounds
        elif(abs(mList[i].yPos) > (wind.y+mList[i].rad)):
            del mList[i]
            m -= 1
        else: i += 1 #next missile
    
    return mList


def enemy(eList):
    #function usables
    wind = objects.screen()

    for enemy in eList:
        #moves enemies to right
        enemy.xPos += enemy.eDir*enemy.s

        #checks bounds > moves opp. dir. & down
        if abs(enemy.xPos) > (wind.x - enemy.rad):
            for all_enemies in eList:
                all_enemies.eDir *= -1
                all_enemies.yPos -= 1

            break

