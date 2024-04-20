import stddraw, math, time, random, startScreen, ship, alien, audio, threading, stars

def main():

    #Variable declarations start
    minX = 0
    maxX = 0
    minY = 0
    flag = False
    check = False
    check1 = False
    escape = False
    start = True
    numEnemies = 5
    spacing = 0.4
    radius = 0.15
    bullets = []
    enemies = []
    star = []
    fireRate = 0
    placeHold = None
    #Variable declarations end

    #Game set up start
    stddraw.setCanvasSize(660, 660)
    stddraw.setXscale(-2.0, 2.0)
    stddraw.setYscale(-2.0, 2.0) 
    startScreen.startScreen()    
    #Game set up end

    for i in range(40):
        sign = random.randint(1, 2)
        sign2 = random.randint(1, 2)
        if sign2 == 2:
            sign2 = -1
        if sign == 2:
            sign = -1
        xPos = random.random()*2*sign
        yPos = random.random()*2*sign2
        speed = random.random()
        while speed < 0.2 or speed > 0.4:
            speed = random.random()
        name = i
        name = stars.Star(xPos, yPos, speed)
        star.append(name)

    #Start Game
    while not escape:
        beg = time.time()
        if start == True:
            start = False
            if numEnemies%2 == 0:                   #set the correct starting position if there is an even number of enemies
               xInit = (-spacing/2)-((numEnemies/2) - 1)*spacing
            else:                                   #set the correct starting position if there is an odd number of enemies
                xInit = spacing*-int(numEnemies/2)

            counter = 0 #counter for the key name in the dictionary set to 0
            y = 1.8
            for j in range(numEnemies):
                x = xInit
                for i in range(numEnemies):
                    name = counter 
                    name = alien.Alien(x, y, radius, True)
                    enemies.append(name)
                    x += spacing
                    counter += 1
                y -= spacing
            s = ship.Ship(18, 0, -1.8, math.pi/2)

        if len(enemies) == 0:
            stddraw.clear(stddraw.MAGENTA)
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.setFontSize(35)
            stddraw.text(0, 0, "You Win!")
            stddraw.setFontSize(20)
            stddraw.text(0, -1, "Press any key to restart")
            stddraw.show(1000)
            for i in range(len(bullets)):
                del bullets[0]
            while stddraw.hasNextKeyTyped():
                stddraw.nextKeyTyped()
            while not stddraw.hasNextKeyTyped():
                stddraw.clear(stddraw.MAGENTA)
                stddraw.setPenColor(stddraw.WHITE)
                stddraw.setFontSize(35)
                stddraw.text(0, 0, "You Win!")
                stddraw.setFontSize(20)
                stddraw.text(0, -1, "Press any key to restart")
                stddraw.show(0)
            start = True

        if  math.sqrt((minY - s.getY())**2) <= (0.1 + 0.15):
            stddraw.clear(stddraw.DARK_RED)
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.setFontSize(35)
            stddraw.text(0, 0, "You Lose!")
            stddraw.setFontSize(20)
            stddraw.text(0, -1, "Press any key to restart")
            stddraw.show(1000)
            for c in range(len(bullets)):
                del bullets[0]
            for l in range(len(enemies)):
                del enemies[0]
            while stddraw.hasNextKeyTyped():
                stddraw.nextKeyTyped()
            while not stddraw.hasNextKeyTyped():
                stddraw.clear(stddraw.DARK_RED)
                stddraw.setPenColor(stddraw.WHITE)
                stddraw.setFontSize(35)
                stddraw.text(0, 0, "You Lose!")
                stddraw.setFontSize(20)
                stddraw.text(0, -1, "Press any key to restart")
                stddraw.show(0)
            minY = 0
            start = True

        stddraw.clear(stddraw.BLACK)

        for i in range(len(star)):
            if star[i].y <= -2:
                sign = random.randint(1, 2)
                if sign == 2:
                    sign = -1
                star[i].x = random.random()*sign*2
                star[i].y = random.random()+2
            else:
                stars.Star.move(star[i])


        if flag == True:
            threading.Thread(target=audio.enemyDead).start()
            flag = False
        
       
        if minX > (-2+radius) and maxX == 0:
            if check == False:
                check = True
                for g in range(len(enemies)):
                    enemies[g].down()
                    if enemies[g].getY() < minY:
                        minY = enemies[g].getY()
            else:
                for g in range(len(enemies)):
                    enemies[g].move(-3, 0.01)
                    if enemies[g].getX() < minX:
                        minX = enemies[g].getX() 
        elif maxX < (2-radius):
            if check1 == False:
                check1 = True
                for g in range(len(enemies)):
                    enemies[g].down()
                    if enemies[g].getY() < minY:
                        minY = enemies[g].getY()
            else:
                for g in range(len(enemies)):
                    enemies[g].move(3, 0.01)
                    if enemies[g].getX() > maxX:
                        maxX = enemies[g].getX()
        else:
            check  = False
            check1 = False
            minX = 0
            maxX = 0

        keys = stddraw.getKeysPressed()
        if keys[stddraw.K_x]:
            escape = True
        if keys[stddraw.K_h]:
            startScreen.startScreen()
        if keys[stddraw.K_a]:
            if s.getX() > (-2+0.1):
                s.move(-1)
            else:
                s.rotate()
        elif keys[stddraw.K_d]:
            if s.getX() < (2-0.1):
                s.move(1)
            else:
                s.rotate()
        else:
            s.rotate
        if keys[stddraw.K_w]:
            s.setAngle(math.pi/2)
            s.setPos(18)
            s.rotate()
        else:
            s.rotate()
        if keys[stddraw.K_q]:
            s.rotate(-1)
        elif keys[stddraw.K_e]:
            s.rotate(1)
        if keys[stddraw.K_SPACE] and fireRate == 0:
            placeHold = ship.Bullet(s.getX(), s.getY(), s.getAngle(), True)
            bullets.append(placeHold)
            fireRate = 40
        if fireRate != 0:
            fireRate -= 1
        i = 0
        while i < len(bullets):
            ship.Bullet.move(bullets[i])
            if bullets[i].getX() > 2 or bullets[i].getX() < -2 or bullets[i].getY() > 2 or bullets[i].getY() < -2:
                del bullets[i]
            else:
                i += 1


        j = 0
        while j < len(enemies):
            i = 0
            while i < len(bullets):
                distance = math.sqrt((enemies[j].getX() - bullets[i].getX())**2 + (enemies[j].getY() - bullets[i].getY())**2)
                if distance <= (radius+0.05):
                    bullets[i].setState(False)
                    enemies[j].setState(False)
                    flag = True
                i += 1
            j += 1

        i = 0
        while i < len(enemies):
            if enemies[i].getState() == False:
                del enemies[i]
            else: i+= 1
        i = 0
        while i < len(bullets):
            if bullets[i].getState() == False:
                del bullets[i]
            else:
                i += 1
        end = time.time()
        '''
        Handles the frame rate so that the game has a constant speed throughout
        and does not speed up or slow down depending on proccess time
        '''
        print(f'Process time: {end - beg}')
        try:
            fps = 1/(end - beg)
            stddraw.text(1.8, 1.8, '%.0f' % (fps))
            if fps < 90:
                stddraw.show(0)
            else:
                stddraw.show(1000/90 - (end-beg)*1000)
        except Exception: 
            stddraw.show(1000/90)
 

if __name__ == "__main__": main()
