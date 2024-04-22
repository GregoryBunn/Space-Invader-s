import screens, stddraw, enemies, time, threading, score
from ship import Ship, Bullet
from math import pi, sqrt
#Scale is just incase we all used different scale when programming but we can talk about what scale we want to use when we are all together
#I used scale of '2' when i coded mine so it would work inbetween -2 and 2
def mainGame(scale, players):
    #initializing all variables
    aliens = []
    bullets = []
    numEnemies = 3
    spacing = scale*0.2
    y = scale - scale*0.1
    dir = 1
    changeDir = 0
    fireRate = 10
    limit = 0
    gameState = True
    #______________________________________________________________________________________________#
    '''
    centers the enemies when starting the game, we can decide if we want to do this later on.
    It just looks nice when running but doesnt really matter at all, just adds extra lines of code.
    '''
    if numEnemies%2 == 0:
        xInit = (-spacing/2)-((numEnemies/2) - 1)*spacing
    else:                                   
        xInit = spacing*-int(numEnemies/2)
    counter = 0
    for j in range(numEnemies):
        x = xInit
        for i in range(numEnemies):
            name = counter
            name = enemies.Enemy(x, y, scale*0.075, True)
            aliens.append(name)
            counter += 1
            x += spacing
        y -= spacing
    #Make a ship
    #You'll see that this function 'mainGame' takes in players aswell and that is because on the start screen if you press the number 2 key
    #it will be 2 player, making a second ship. this happens in the 'game.py' file
    if players == 2:
        s1 = Ship(0.4, -1.8, pi/2, 0, 37, 0)
        s0 = Ship(-0.4, -1.8, pi/2, 0, 37, 0)
    elif players == 1:
        s0 = Ship(0, -1.8, pi/2, 0, 37, 0)

    while gameState:
        stddraw.clear(stddraw.BLACK)

        #Shows the win screen
        if len(aliens) == 0:
            del s0
            for i in range(len(bullets)):
                del bullets[0]
            while stddraw.hasNextKeyTyped():
                stddraw.nextKeyTyped()
            screens.winScreen()
            time.sleep(1)
            while not stddraw.hasNextKeyTyped():
                screens.winScreen()
            #return 1 so that in the 'game.py' file, we can see if they have won a game and then make it more difficult later on
            #So for now it doesn't do much but is there for code to use later on.
            return 1
        frameST = time.time()




        #Handles all of the enemies movements
        if changeDir == 1:
            changeDir = 0
            for i in range(len(aliens)):
                aliens[i].moveDown()
            dir *= -1
        else:
            for i in range(len(aliens)):
                check = aliens[i].move(dir, 0.01, scale)
                if check == 1:
                    changeDir = 1




        #keyboard inputs
        keys = stddraw.getKeysPressed()
        if keys[stddraw.K_e]:
            s0.rotate(1)
        elif keys[stddraw.K_q]:
            s0.rotate(-1)
        elif keys[stddraw.K_w]:
            s0.setAngle(pi/2)
            s0.setPos(37)
        if keys[stddraw.K_a]:
            if s0.getX() > (-scale+0.2):
                s0.move(-1)
            else:
                s0.rotate()
        elif keys[stddraw.K_d]:
            if s0.getX() < (scale-0.2):
                s0.move(1)
            else:
                s0.rotate()
        else:
            s0.rotate()
        
        #The movement for the second player on if a second player is chosen, otherwise it does nothing
        if players == 2:
            if keys[stddraw.K_o]:
                s1.rotate(1)
            elif keys[stddraw.K_u]:
                s1.rotate(-1)
            elif keys[stddraw.K_i]:
                s1.setAngle(pi/2)
                s1.setPos(37)
            if keys[stddraw.K_j]:
                if s1.getX() > (-scale+0.2):
                    s1.move(-1)
                else:
                    s1.rotate()
            elif keys[stddraw.K_l]:
                if s1.getX() < (scale-0.2):
                    s1.move(1)
                else:
                    s1.rotate()
            else:
                s1.rotate()






        #shooting for the first player
        if keys[stddraw.K_SPACE] and s0.getFireRate() <= 0:
            bullet = Bullet(s0.getX(), s0.getY(), s0.getAngle(), '1',  True)
            bullets.append(bullet)
            s0.setFireRate(fireRate)
        else: s0.setFireRate(s0.getFireRate()-1)

        #Shooting for the second player
        if players == 2:
            if keys[stddraw.K_n] and s1.getFireRate() <= 0:
                bullet = Bullet(s1.getX(), s1.getY(), s1.getAngle(), '2',  True)
                bullets.append(bullet)
                s1.setFireRate(fireRate)
            else: s1.setFireRate(s1.getFireRate()-1)






        #interaction between the enemies and bullets. 
        i = 0
        while i != len(bullets):
            bullets[i].move()
            if bullets[i].getX() > 2 or bullets[i].getX() < -2 or bullets[i].getY() > 2 or bullets[i].getY() < -2:
                del bullets[i]
            else:
                i += 1
        
        j = 0
        while j < len(aliens):
            i = 0
            while i < len(bullets):
                distance = sqrt((aliens[j].getX() - bullets[i].getX())**2 + (aliens[j].getY() - bullets[i].getY())**2)
                if distance <= (scale*0.075+0.05):
                    if bullets[i].getOwner() == '1':
                        s0.inscreaseScore()
                    elif bullets[i].getOwner() == '2':
                        s1.inscreaseScore()
                    bullets[i].setState(False)
                    aliens[j].setState(False)
                    flag = True
                i += 1
            j += 1

        i = 0
        while i < len(aliens):
            if aliens[i].getState() == False:
                del aliens[i]
            else: i+= 1
        i = 0
        while i < len(bullets):
            if bullets[i].getState() == False:
                del bullets[i]
            else:
                i += 1
        if players == 1:
            score.displayScore(s0.getScore())
        elif players == 2:
            score.displayScore(s0.getScore(), s1.getScore())
        frameEND = time.time()
        '''
        The next few lines of code does the math inorder to have a consistent frame rate throughout the game
        '''
        try:
            fps = 1/(frameEND - frameST )
            stddraw.text(1.8, 1.8, '%.0f' % (fps))
            if fps < 90:
                stddraw.show(0)
            else:
                stddraw.show(1000/90 - (frameEND-frameST)*1000)
        except Exception: 
            stddraw.show(1000/90)