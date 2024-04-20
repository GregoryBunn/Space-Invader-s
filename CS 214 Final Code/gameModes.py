import screens, stddraw, enemies

def mainGame(scale):
    aliens = []
    numEnemies = 3
    spacing = scale*0.2
    y = scale - scale*0.1
    
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
    dir = 1
    temp = None
    changeDir = 0
    
    while True:
        stddraw.clear(stddraw.BLACK)
        if changeDir == 1:
            changeDir = 0
            for i in range(len(aliens)):
                aliens[i].moveDown()
            dir *= -1
        else:
            for i in range(len(aliens)):
                check = aliens[i].move(dir, 0.1, scale)
                if check == 1:
                    changeDir = 1
        stddraw.show(120)