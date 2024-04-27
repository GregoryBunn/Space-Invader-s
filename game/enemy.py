import stddraw
from stddraw import picture
from picture import Picture
import random
 
class EnemySettings:
    def __init__(self,x,y,hitbox,speed,typ,size):
            self._countx = x
            self._county = y
            self._hitBox = hitbox
            self._speed= speed
            self._typ = typ
            self._size = size
            

class Enemy:
    '''
    Handels individual enemy functions:
    proces enemy movements
    Test
    '''
    def __init__(self,x,y,typ,size,dir,speed,powerup,hitBox):
        self._x = x
        self._y = y
        self._typ = typ
        self._size = size
        self._dir = dir
        self._speed = speed
        self._powerup = powerup
        self._hitBox = hitBox

       
    #Draw type 0 enemy
    def drawBasicEnemy(self):
        #stddraw.setPenColor(stddraw.RED) #set pen color
        #stddraw.filledCircle(self.x,self.y,self.size) #Draw red Circle

        #graphics
        if self._hitBox == 1:
            #draw enemy with one life
            basic = Picture('Alien2.png')
        else:
            #draw enemy with 0 lives
            basic = Picture("Alien1.png")
            pass
        picture(basic, self._x, self._y)

    def drawBoss(self):
        boss = Picture('Boss0.png')
        picture(boss, self._x, self._y)
        self.drawBossHealth()

    def drawBossHealth(self):
        stddraw.setPenColor(stddraw.RED)
        stddraw.rectangle(-80,95,160,4)
        stddraw.setPenColor(stddraw.BLACK)
        #boss starting health
        w = 158 - (self._hitBox*16)
        if w < 0:w=0
        stddraw.rectangle(-79,96,w,2)

    #move single enemy sideways
    def moveEnemySideways(self):
        screenX = 100 #screen size x

        #move enemy left or right       
        self._x += self._dir*self._speed

        #check if enemy has reached side
        if self._x < -screenX + self._size or self._x > screenX-self._size:
            return True
        else:
            return False

    #move enemy down
    def moveEnemyDown(self): 
        #change direction
        self._dir *= -1
        #move down
        self._y -= self._size*2

    #check if enemy is below shooter
    def checkEnemyBelowShooter(self,settings,player):
        if self._y < player._y:
            #player looses-result = Fales
            settings.result = False
            return True #stop game
        else:
            return False #game continues
        
    #check if enemy touches player
    def checkEnemyTouchShooter(self,settings,player):
        #calculate distance between player and enemy
        distx = abs(self._x - player._x)
        disty = abs(self._y - player._y)
        dist = (distx**2 + disty**2)**0.5
        #test if enemy is touching player
        if dist < self._size + player._size:
            #player looses result = Fales
            settings.result = False
            return True #stop game
        else:
            return False #game continues
        
        

       


    



class EnemyList:

    def __init__(self):
        self._Enemylist = []#create list of enemys

    def add_Enemy(self,enemy_class:Enemy):
        #add enemy to list
        self._Enemylist.append(enemy_class)

    def remove_Enemy(self,enemy_class:Enemy):
        #remove enemy from list
        if enemy_class in self._Enemylist:
            self._Enemylist.remove(enemy_class)

    def Make_Basic_EnemyGrid(self,settings:EnemySettings):
        for y in range(settings._county):
            for x in range(settings._countx):
                typ = settings._typ
                
                xCor = -90+x*(15)
                yCor = 90 - y*(15)
                #adjustment for bos enemy
                if typ == 1:
                    xCor += 10
                    yCor -= 10
                size = settings._size#6
                dir = 1
                speed = settings._speed #1
                p = random.random()
                if p < 0.2:
                    PowerupType = 1
                elif p < 0.4:
                    PowerupType = 2
                elif p < 0.6:
                    PowerupType = 3
                else:
                    PowerupType = 0
                hitbox = settings._hitBox#1
                #Add Enemy to list
                self.add_Enemy(Enemy(xCor,yCor,typ,size,dir,speed,PowerupType,hitbox))

    def Move_Enemys(self):
        moveDown = False
        for enemy in self._Enemylist:
            if enemy.moveEnemySideways():
                moveDown = True
        if moveDown == True:
            for enemy in self._Enemylist:
                enemy.moveEnemyDown()

    #Draw enemys
    def Draw_Enemys(self):
        #itterate through list of enemys
        for enemy in self._Enemylist:
            
            if enemy._typ ==0:#if enemy is of type 0 enemy
                enemy.drawBasicEnemy()#draw enemy
            if enemy._typ == 1:
                enemy.drawBoss()
    

    #check if the game should end
    def Check_for_End(self,settings,players_list):

        #test if any players are left
        if len(players_list._Players) == 0:
            settings.result = False
            return False
        
        
            

        #if no enemys are left
        if len(self._Enemylist) == 0:
            #game is won
            settings.result = True

            return False #stop game
        
        
        #itterate through players
        for player in players_list._Players:

            if player._lives ==0:
                settings.result = False
                return False

            #itterate throung enemys
            for enemy in self._Enemylist:
                #check if enemy touches shooter
                if enemy.checkEnemyTouchShooter(settings,player):
                    return False #stop game
                #check if enemy is below shooter
                elif enemy.checkEnemyBelowShooter(settings,player):
                    return False #stop game
            
        

        return True#game should continue
    
    #powerup
    def Create_powerup(self,ec,powerups):
        x = self._Enemylist[ec]._x
        y = self._Enemylist[ec]._y
        powerupTyp = self._Enemylist[ec]._powerup
        if self._Enemylist[ec]._powerup == 0:
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

                while (ec < len(self._Enemylist)):

                    #calculate distance between missile and enemy
                    distx = abs(Missiles_list.missiles[mc].x - self._Enemylist[ec]._x)
                    disty = abs(Missiles_list.missiles[mc].y - self._Enemylist[ec]._y)
                    dist = (distx**2 + disty**2)**0.5 

                    #need to add missile radius

                    #test if missile hit enemy
                    if dist < self._Enemylist[ec]._size + Missiles_list.missiles[mc].size: # + if for missile size

                        #test enemy hitpoints
                        if self._Enemylist[ec]._hitBox == 0:
                            #increase Total score
                            settings.score += 1
                            #increse player scores
                            if Missiles_list.missiles[mc].owner == 0:
                                playerlist._Players[0]._score += 1
                
                            else:
                                playerlist._Players[1]._score +=1
                        

                            #create Powerup if enemy has one
                            self.Create_powerup(ec,powerups)#ec = enemy Number
  
                            #remove enemy
                            self.remove_Enemy(self._Enemylist[ec])

                        else:
                            self._Enemylist[ec]._hitBox -= 1

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
        self._x = x
        self._y = y
        self._typ = typ
    def move_down(self):
        POWERUP_SPEED = 1
        self._y -= POWERUP_SPEED
    def drawType(self):
        if self._typ == 1:
            stddraw.setPenColor(stddraw.PINK)
        elif self._typ == 2:
            stddraw.setPenColor(stddraw.BLUE)
        elif self._typ == 3:
            stddraw.setPenColor(stddraw.DARK_GREEN)

        stddraw.filledCircle(self._x,self._y,2)

    def checkPowerupBound(self):
        screenX = 100
        screenY = 100

        #Check if missile x is in the screen bounds
        if self._x > screenX-6 or self._x < -screenX+6:
            #remove missile
            return False
        
        #Check if missile y is in the screen bounds
        elif self._y > screenY-8 or self._y < -screenY+8:
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