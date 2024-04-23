import screens, stddraw, enemies, time, threading, score, random, gameFuncs
from ship import Ship, Bullet
from math import pi, sqrt
#Scale is just incase we all used different scale when programming but we can talk about what scale we want to use when we are all together
#I used scale of '2' when i coded mine so it would work inbetween -2 and 2
def mainGame(scale, players, en, spd, sc, htp):
    #initializing all variables
    aliens = []
    bullets = []
    enBullets = []
    numEnemies = 3
    if en != 0:
        numEnemies += en
    spacing = scale*0.2
    y = scale - scale*0.1
    dir = 1
    changeDir = 0
    shootingEnemy = 0
    test = 0
    fireRate = 20
    rand = None
    gameState = True
    exit = 0
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
            name = enemies.Enemy(x, y, scale*0.075, 1, True)
            aliens.append(name)
            counter += 1
            x += spacing
        y -= spacing
    #Make a ship
    #You'll see that this function 'mainGame' takes in players aswell and that is because on the start screen if you press the number 2 key
    #it will be 2 player, making a second ship. this happens in the 'game.py' file
    if players == 2:
        s1 = Ship(0.4, -1.8, pi/2, 0, 37, 0.1, htp, sc)
        s0 = Ship(-0.4, -1.8, pi/2, 0, 37, 0.1, htp, sc)
    elif players == 1:
        s0 = Ship(0, -1.8, pi/2, 0, 37, 0.1, htp, sc)

    while gameState:
        stddraw.clear(stddraw.BLACK)

        #Shows the win screen
        if len(aliens) == 0:
            sc = s0.getScore()
            health = s0.get_htp()
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
            return 1, sc, health
        frameST = time.time()

        rand = random.randint(0, 200)
        if rand == 50:
            shootingEnemy = int(random.random()*(len(aliens)-1))
            bul = test
            bul = enemies.enBullet(aliens[shootingEnemy].getX(),aliens[shootingEnemy].getY(), True)
            enBullets.append(bul)
            test += 1
        for i in range(len(enBullets)):
            enBullets[i].move()
            

        #Handles all of the enemies movements
        if changeDir == 1:
            changeDir = 0
            for i in range(len(aliens)):
                aliens[i].moveDown()
            dir *= -1
        else:
            for i in range(len(aliens)):
                check = aliens[i].move(dir, 0.01+spd, scale)
                if check == 1:
                    changeDir = 1




        #keyboard inputs
        keys = stddraw.getKeysPressed()
        exit = gameFuncs.keyBoardProccess(keys, s0, scale, bullets, fireRate)
        
        if exit == 1:
            return 2, 0, 0

        #The movement for the second player on if a second player is chosen, otherwise it does nothing
        if players == 2:
           gameFuncs.keyBoardProccessP2(keys, s1, scale, bullets, fireRate)

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
                if distance <= (scale*aliens[j].get_hitBox()+0.05):
                    if bullets[i].getOwner() == '1':
                        s0.inscreaseScore()
                    elif bullets[i].getOwner() == '2':
                        s1.inscreaseScore()
                    bullets[i].setState(False)
                    aliens[j].setState(False)
                   # flag = True
                i += 1
            j += 1
        i = 0


        while i < len(enBullets):
            distance = sqrt((enBullets[i].get_x() - s0.getX())**2 + (enBullets[i].get_y() - s0.getY())**2)
            if distance <= s0.get_hitBox() + 0.05:
                s0.set_htp(s0.get_htp() - 1)
                enBullets[i].set_state(False)
            i += 1
        i = 0
        while i <len(enBullets):
            if enBullets[i].get_state() == False:
                del enBullets[i]
            else:
                i += 1

        if s0.get_htp() == 0:
            del s0
            screens.loseScreen()
            time.sleep(1)
            while stddraw.hasNextKeyTyped(): stddraw.nextKeyTyped()
            while not stddraw.hasNextKeyTyped(): screens.loseScreen()
            return 0, 0, 0
            
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
        
        for i in range(len(aliens)):
            if aliens[i].getY() <= s0.getY() + aliens[i].get_hitBox():
                del s0
                screens.loseScreen()
                time.sleep(1)
                while stddraw.hasNextKeyTyped(): stddraw.nextKeyTyped()
                while not stddraw.hasNextKeyTyped(): screens.loseScreen()
                return 0, 0, 0
        
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


def boss(scale, htps):
    bullets = []
    changeDir = 0
    dir = 1
    timer = 0
    gameState = True
    lose = False
    fireRate = 50
    s0 = Ship(0, -1.8, pi/2, 0, 37, 0.01, 1, 0)
    boss = enemies.Boss(0, scale - scale*0.2, htps, 0.18, True)
    while gameState:
        stddraw.clear(stddraw.BLACK)
        if lose == True:
            screens.loseScreen()
            time.sleep(1)
            while stddraw.hasNextKeyTyped(): stddraw.nextKeyTyped()
            while not stddraw.hasNextKeyTyped(): screens.loseScreen()
            return 0
        if changeDir == 1:
            changeDir = 0
            boss.moveDown()
            dir *= -1
        else:
            check = boss.move(dir, 0.02, scale)
            if check == 1:
                changeDir = 1
        
        rand = random.randint(0, 200)
        if rand == 50 and timer <= 0:
            dir *= -1
            timer = 200
        timer -= 1


        keys = stddraw.getKeysPressed()
        exit = gameFuncs.keyBoardProccess(keys, s0, scale, bullets, fireRate)
        if exit == 1:
            return 2, 0, 0


        i = 0
        while i != len(bullets):
            bullets[i].move()
            if bullets[i].getX() > 2 or bullets[i].getX() < -2 or bullets[i].getY() > 2 or bullets[i].getY() < -2:
                del bullets[i]
            else:
                i += 1
        
        i = 0
        while i < len(bullets):
            distance = sqrt((boss.get_x() - bullets[i].getX())**2 + (boss.get_y() - bullets[i].getY())**2)
            if distance <= (scale*boss.get_hitBox()+0.05):
                s0.inscreaseScore()
                bullets[i].setState(False)
                boss.hit()
                if boss.get_htps() == 0:
                    boss.set_state(False)
            i += 1
        
        if boss.get_state() == False:
            del boss
            health = s0.get_htp()
            del s0
            screens.winScreen()
            time.sleep(1)
            while stddraw.hasNextKeyTyped(): stddraw.nextKeyTyped()
            while not stddraw.hasNextKeyTyped(): screens.winScreen()
            return 1, 0, health
        i = 0
        while i < len(bullets):
            if bullets[i].getState() == False:
                del bullets[i]
            else:
                i += 1
        
        if boss.get_y() < s0.getY() + 0.1:
            lose = True
        
        stddraw.show(1000/90)