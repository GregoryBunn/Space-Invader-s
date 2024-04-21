#the game?
import stddraw, title, objects, draw, move, project, level
def clear():
    stddraw.clear(stddraw.GRAY)

def reload():
    stddraw.show(3000)
    project.main()


def gamerun(SCREEN, SHOOTER):
    #initialising objects
    shooter = SHOOTER
    screen = SCREEN
    enemies = []
    enemySize = objects.enemy_level()
    missiles = []
    lDisplay = False #level-screen-displayed flag

    play = True
    while (play):        
        #levels
        if not(lDisplay):
            level.drawScreen(screen, shooter)
            lDisplay = True        
            level.enemyUpdate(shooter, enemySize, enemies, screen)
        

        #draw screen & objects 
        draw.gameScreen(screen)
        draw.shooter(shooter)
        draw.enemies(enemies)
        draw.score(shooter)
        draw.highscore()
        draw.lives(shooter)
        draw.level(shooter)
        draw.missiles(missiles)
           
        #check game statuses
        enemies, missiles = objects.checkEnemHit(enemies, missiles, shooter)
        play = objects.checkGameover(enemies, shooter, screen)
        lDisplay = level.checkLevel(enemies, shooter)

        #user inputs
        if(stddraw.hasNextKeyTyped()):
            user = stddraw.nextKeyTyped()
            if(user=="d"): shooter.sDir = 1  #shooter moves right
            elif(user=="s"): shooter.sDir = 0  #shooter stops
            elif(user=="a"): shooter.sDir = -1  #shooter moves left
            elif(user=="q"): shooter.aMov = -0.05  #aim moves left
            elif(user=="w"): shooter.aMov = 0  #aim stops
            elif(user=="e"): shooter.aMov = 0.05  #aim moves right
            elif(user=="x"): 
                play = False  #quit game 
                return shooter
            elif(user==" "): #shoot
                if(objects.checkTime(shooter)):
                    objects.addMiss(missiles, shooter)
                else: pass

        #update positions
        shooter.xPos = move.shooter(shooter)
        shooter.aDir = move.aim(shooter)
        move.enemy(enemies)
        missiles = move.missile(missiles)

           
        stddraw.show(10)
        shooter.time += 1 #update time since last missile

    return shooter
