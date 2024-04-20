#drawings besides title
import stddraw, objects, game, math

def gameScreen(wind):
    game.clear()
    stddraw.setXscale(-wind.x, wind.x)
    stddraw.setYscale(-wind.y, wind.y)
    stddraw.setFontSize(18)

def shooter(s):
    #player
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledCircle(s.xPos, s.yPos, s.rad)

    #aim
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setPenRadius(0.075)
    aX = s.xPos + s.rad*(math.sin(s.aDir))
    aY = s.yPos + s.rad*(math.cos(s.aDir))
    stddraw.line(s.xPos, s.yPos, aX, aY)

def enemies(e):
    for i in range(len(e)): 
        if(e[i].life==3): stddraw.setPenColor(stddraw.GREEN)
        if(e[i].life==2): stddraw.setPenColor(stddraw.YELLOW)
        if(e[i].life==1): stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(e[i].xPos, e[i].yPos, e[i].rad)

def score(s):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(7, 9.5, "Score: "+str(s.score))

def highscore():
    #get highscore
    f = open("highscore.txt", "r")
    high_s = f.read()
    f.close()

    #draw highscore
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(-8, 9.5, "Highscore: "+str(high_s))

def level(player):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(-8.7, 8.5, "Level: "+str(player.level))

def missiles(m):
    stddraw.setPenColor(stddraw.BLACK)
    for i in range(len(m)): stddraw.filledCircle(m[i].xPos, m[i].yPos, m[i].rad)

def lives(player):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(6.8, 8.5, "Lives: ")
    #checks player lives and draws images
    stddraw.setPenColor(stddraw.RED)
    stddraw.setPenRadius(0.003)
    if player.lives ==3:
        for i in range(3): stddraw.filledCircle((7.9 + i*0.8), 8.5, 0.3)
    elif player.lives==2:
        for i in range(2): stddraw.filledCircle((7.9 + i*0.8), 8.5, 0.3)
        stddraw.circle((7.9 + 2*0.8), 8.5, 0.3)
    elif player.lives==1:
        stddraw.filledCircle((7.9), 8.5, 0.3)
        for i in range(2): stddraw.circle((7.9 + (i+1)*0.8), 8.5, 0.3)
        
