import stddraw
from stddraw import picture
from picture import Picture
import random
 
class EnemySettings:
    def __init__(self,x,y,hitbox,speed,typ,size):
            self.countx = x
            self.county = y
            self.hitBox = hitbox
            self.speed= speed
            self.typ = typ
            self.size = size
            

class Enemy:
    '''
    Handels individual enemy functions:
    proces enemy movements
    Test
    '''
    def __init__(self,x,y,typ,size,dir,speed,powerup,hitBox):
        self.x = x
        self.y = y
        self.typ = typ
        self.size = size
        self.dir = dir
        self.speed = speed
        self.powerup = powerup
        self.hitBox = hitBox

       
    #Draw type 0 enemy
    def drawBasicEnemy(self):
        #stddraw.setPenColor(stddraw.RED) #set pen color
        #stddraw.filledCircle(self.x,self.y,self.size) #Draw red Circle

        #graphics
        if self.hitBox == 1:
            #draw enemy with one life
            basic = Picture('Aliens.png')
        else:
            #draw enemy with 2 lives
            basic = Picture("Aliens.png")
            pass
        picture(basic, self.x, self.y)

    def drawBoss(self):
        boss = Picture('Boss0.png')
        picture(boss, self.x, self.y)
        self.drawBossHealth()

    def drawBossHealth(self):
        stddraw.setPenColor(stddraw.RED)
        stddraw.rectangle(-80,95,160,4)
        stddraw.setPenColor(stddraw.BLACK)
        #boss starting health
        w = 158 - (self.hitBox*16)
        if w < 0:w=0
        stddraw.rectangle(-79,96,w,2)

    #move single enemy sideways
    def moveEnemySideways(self):
        screenX = 100 #screen size x

        #move enemy left or right       
        self.x += self.dir*self.speed

        #check if enemy has reached side
        if self.x < -screenX + self.size or self.x > screenX-self.size:
            return True
        else:
            return False

    #move enemy down
    def moveEnemyDown(self): 
        #change direction
        self.dir *= -1
        #move down
        self.y -= self.size*2

    #check if enemy is below shooter
    def checkEnemyBelowShooter(self,settings,player):
        if self.y < player.y:
            #player looses-result = Fales
            settings.result = False
            return True #stop game
        else:
            return False #game continues
        
    #check if enemy touches player
    def checkEnemyTouchShooter(self,settings,player):
        #calculate distance between player and enemy
        distx = abs(self.x - player.x)
        disty = abs(self.y - player.y)
        dist = (distx**2 + disty**2)**0.5
        #test if enemy is touching player
        if dist < self.size + player.size:
            #player looses result = Fales
            settings.result = False
            return True #stop game
        else:
            return False #game continues
        
        

       


    



class EnemyList:

    def __init__(self):
        self.Enemylist = []#create list of enemys

    def add_Enemy(self,enemy_class:Enemy):
        #add enemy to list
        self.Enemylist.append(enemy_class)

    def remove_Enemy(self,enemy_class:Enemy):
        #remove enemy from list
        if enemy_class in self.Enemylist:
            self.Enemylist.remove(enemy_class)

    def Make_Basic_EnemyGrid(self,settings:EnemySettings):
        for y in range(settings.county):
            for x in range(settings.countx):
                typ = settings.typ
                
                xCor = -90+x*(15)
                yCor = 90 - y*(15)
                #adjustment for bos enemy
                if typ == 1:
                    xCor += 10
                    yCor -= 10
                size = settings.size#6
                dir = 1
                speed = settings.speed #1
                p = random.random()
                if p < 0.2:
                    PowerupType = 1
                elif p < 0.4:
                    PowerupType = 2
                elif p < 0.6:
                    PowerupType = 3
                else:
                    PowerupType = 0
                hitbox = settings.hitBox#1
                #Add Enemy to list
                self.add_Enemy(Enemy(xCor,yCor,typ,size,dir,speed,PowerupType,hitbox))

    def Move_Enemys(self):
        moveDown = False
        for enemy in self.Enemylist:
            
            if enemy.moveEnemySideways():
                moveDown = True
        if moveDown == True:
            for enemy in self.Enemylist:
                enemy.moveEnemyDown()

    #Draw enemys
    def Draw_Enemys(self):
        #itterate through list of enemys
        for enemy in self.Enemylist:
            
            if enemy.typ ==0:#if enemy is of type 0 enemy
                enemy.drawBasicEnemy()#draw enemy
            if enemy.typ == 1:
                enemy.drawBoss()
    

    #check if the game should end
    def Check_for_End(self,settings,players_list):

        #test if any players are left
        if len(players_list.Players) == 0:
            settings.result = False
            return False
        
        
            

        #if no enemys are left
        if len(self.Enemylist) == 0:
            #game is won
            settings.result = True

            return False #stop game
        
        
        #itterate through players
        for player in players_list.Players:

            if player.lives ==0:
                settings.result = False
                return False

            #itterate throung enemys
            for enemy in self.Enemylist:
                #check if enemy touches shooter
                if enemy.checkEnemyTouchShooter(settings,player):
                    return False #stop game
                #check if enemy is below shooter
                elif enemy.checkEnemyBelowShooter(settings,player):
                    return False #stop game
            
        

        return True#game should continue
    
    #powerup
    def Create_powerup(self,ec,powerups):
        x = self.Enemylist[ec].x
        y = self.Enemylist[ec].y
        powerupTyp = self.Enemylist[ec].powerup
        if self.Enemylist[ec].powerup == 0:
            #No powerup
            pass


        else:
            #add powerup
            powerups.add_powerup(Powerup(x,y,powerupTyp))
        
    #check if any of the enemy's have been hit
    def hitmarks(self,Missiles_list,playerlist,powerups,settings):

        nextM = True #boolean to increase missile count

        #itterate through all missiles and enemy locations
        mc = 0 #missile counter
        while mc < len(Missiles_list.missiles):
            nextM = True
            ec = 0 #enemy counter
            #check if missile is from a player
            if Missiles_list.missiles[mc].owner != 2:

                while (ec < len(self.Enemylist)):

                    #calculate distance between missile and enemy
                    distx = abs(Missiles_list.missiles[mc].x - self.Enemylist[ec].x)
                    disty = abs(Missiles_list.missiles[mc].y - self.Enemylist[ec].y)
                    dist = (distx**2 + disty**2)**0.5 

                    #need to add missile radius

                    #test if missile hit enemy
                    if dist < self.Enemylist[ec].size + Missiles_list.missiles[mc].size: # + if for missile size

                        #test enemy hitpoints
                        if self.Enemylist[ec].hitBox == 0:
                            #increase Total score
                            settings.score += 1
                            #increse player scores
                            if Missiles_list.missiles[mc].owner == 0:
                                playerlist.Players[0].score += 1
                            else:
                                playerlist.Players[1].score +=1

                            #create Powerup if enemy has one
                            self.Create_powerup(ec,powerups)#ec = enemy Number
  
                            #remove enemy
                            self.remove_Enemy(self.Enemylist[ec])

                        else:
                            self.Enemylist[ec].hitBox -= 1

                        #remove Missile
                        Missiles_list.remove_missile(Missiles_list.missiles[mc])
                            

                        #Don't have to increase mc (new missile in old position because of pop)
                        nextM = False 
                        break # exit while

                    else:
                        ec = ec + 1 #go to next enemy
            if nextM:
                mc = mc + 1 # go to next missile


class Powerup:
    def __init__(self,x,y,typ):
        self.x = x
        self.y = y
        self.typ = typ
    def move_down(self):
        POWERUP_SPEED = 1
        self.y -= POWERUP_SPEED
    def drawType(self):
        if self.typ == 1:
            stddraw.setPenColor(stddraw.PINK)
        elif self.typ == 2:
            stddraw.setPenColor(stddraw.BLUE)
        elif self.typ == 3:
            stddraw.setPenColor(stddraw.DARK_GREEN)

        stddraw.filledCircle(self.x,self.y,2)

    def checkPowerupBound(self):
        screenX = 100
        screenY = 100

        #Check if missile x is in the screen bounds
        if self.x > screenX-6 or self.x < -screenX+6:
            #remove missile
            return False
        
        #Check if missile y is in the screen bounds
        elif self.y > screenY-8 or self.y < -screenY+8:
            #remove missile
            return False
        
        #allow missile
        else:
            return True

class Powerup_List:
    def __init__(self):
        self.List_Powerups = []
    def add_powerup(self,powerup : Powerup):
        self.List_Powerups.append(powerup)

    def remove_powerup(self,powerup: Powerup):
        self.List_Powerups.remove(powerup)
    def move_draw_Powerups(self):
        for powerup in self.List_Powerups:
            powerup.move_down()
            if not powerup.checkPowerupBound():
                self.remove_powerup(powerup)
            powerup.drawType()