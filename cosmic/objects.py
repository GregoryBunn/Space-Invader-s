#objects? classes?
import stddraw, objects, math
#object classes
class shooter():
    xPos = 0  #x position
    yPos = -9.25  #y position
    rad = 0.75  #radius
    vx = 0.1  #speed
    sDir = 0  #shooter direction
    aDir = 0  #aim direction
    aMov = 0  #aim move direction
    score = 0  #user score
    time = 0 #time since last missile
    mTime = 10 #time(ms) between missiles
    lives = 1 #default: 3 lives
    level = 1 #player level counter, default: 1

class screen():
    x = 10
    y = 10
    win = False #default: lose

class enemy_level():    
    xNum = 1  #number of enemies across (default 1)
    yNum = 0  #number of enemies down (default 0)

class enemy():
    rad = 0.75  #radius
    eDir = 1 #direction
    s = 0.05 #speed
    life = 3 #hitpoint default 1
    def __init__(self, xPos, yPos):
        self.xPos = xPos  #imported x position
        self.yPos = yPos  #imported y position

class missile(): 
    rad = 0.1 #radius
    sp = 0.5 #speed
    def __init__(self, xPos, yPos, direc):
        self.xPos = xPos  #imported x position
        self.yPos = yPos  #imported y position
        self.direc = direc #imported direction

#extra object functions
def buildEnemies(e, eSize, wind):
    for y in range(eSize.yNum):
        for x in range(eSize.xNum): 
            e.append(objects.enemy((-9 + x*2), (7.25 - y*2)))
            
def addMiss(m, s): #missile, shooter
    x = s.xPos + s.rad*math.sin(s.aDir)
    y = s.yPos + s.rad*math.cos(s.aDir)
    d = s.aDir
    m.append(objects.missile(x, y, d))

def checkTime(S): #shooter
    if(S.time>S.mTime): #check if last missile time is greater than limit
        S.time = 0 #reset
        return True
    else: return False

def checkGameover(E,P,S):  #E=enemies, P=player, S=screen
    #check if enemy touches ground
    for i in range(len(E)):
        if abs(E[i].yPos) > (S.y - E[i].rad):
            S.win = False #player loses
            return False

    #check if enemy touches player
    for j in range(len(E)):
        y = abs(P.yPos - E[j].yPos)
        x = abs(P.xPos - E[j].xPos)
        d = math.sqrt((y**2 + x**2)) #distance between enemy and player
        if(d <= (P.rad + E[j].rad)):
            S.win = False #player loses
            return False

    return True

#(modified for hitpoints using enemy lives)
def checkEnemHit(E, M, P): #E=enemy, M=missile, P=player
    #list for enemy/missile indexes to remove
    remove_enemies = []
    remove_missiles = []

    #loop through enemies and track indexes
    for m, missile in enumerate(M):
        for e, enemy in enumerate(E):
            #distance between missile and enemy
            x = abs(missile.xPos - enemy.xPos)
            y = abs(missile.yPos - enemy.yPos)
            dis = math.sqrt((x**2 + y**2))

            #check if enemy is hit and reduce life and remove missile
            if (dis <= enemy.rad): 
                enemy.life -= 1
                remove_missiles.append(m)
                if (enemy.life==0): #if enemy has no life, remove
                    remove_enemies.append(e)
                    P.score += 2 #player score increase
                break

    #remove enemies and missiles
    #loops through sorted removal lists starting from the back
    for e_index in sorted(remove_enemies, reverse=True): del E[e_index]
    for m_index in sorted(remove_missiles, reverse=True): del M[m_index]

    #returns updated lists
    return E, M
