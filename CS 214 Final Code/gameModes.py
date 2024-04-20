import screens, stddraw, enemies, time
#Scale is just incase we all used different scale when programming but we can talk about what scale we want to use when we are all together
#I used scale of '2' when i coded mine so it would work inbetween -2 and 2
def mainGame(scale):
    #initializing all variables
    aliens = []
    numEnemies = 3
    spacing = scale*0.2
    y = scale - scale*0.1
    dir = 1
    temp = None
    changeDir = 0
    #______________________________________________________________________________________________#
    '''
    centers the enemies when starting the game, we can decide if we want to do this later on.
    It just looks nice when running but doesnt really matter at all, just adds extra lines of code.
    '''
    while not stddraw.hasNextKeyTyped():
        screens.startScreen()
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

    while True:
        stddraw.clear(stddraw.BLACK)
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
        #__________________________________________________________________________
        frameEND = time.time()
        '''
        The next code does the math inorder to have a consistent frame rate throughout the game
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