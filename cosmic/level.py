#level details
import objects, stddraw, game

def drawScreen(SCREEN, PLAYER):
    game.clear()
    stddraw.setXscale(-SCREEN.x, SCREEN.x)
    stddraw.setYscale(-SCREEN.y, SCREEN.y)

    stddraw.clear(stddraw.GRAY)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(38)
    stddraw.text(0, 0, "Level: "+str(PLAYER.level))
    stddraw.show(1000)
    #return False

def enemyUpdate(player, enemySize, enemyList, window):
    lev = player.level
    if(lev==1): #default/start enemy details
        enemySize.xNum = 2
        enemySize.yNum = 2
        objects.buildEnemies(enemyList, enemySize, window) #build enemy list
        for enemy in enemyList: enemy.life = 1 #set hitpoints to 1
    elif(lev==2): 
        enemySize.xNum = 5
        enemySize.yNum = 3
        objects.buildEnemies(enemyList, enemySize, window) #build enemy list

        #change enemy life size
        for enemy in enemyList: enemy.life = 2 #set hitpoints to 2
    else: #default/start enemy details
        enemySize.xNum = 5
        enemySize.yNum = 3
        objects.buildEnemies(enemyList, enemySize, window) #build enemy list

    #return enemyList #return new list

def checkLevel(E, player): #E = enemyList
    #check if no enemies
    if len(E)==0:
        player.level += 1 #increase level
        return False
    else: return True