import stddraw
import math


class Player:
    def __init__(self,x : float,y : float,aimchange : float,aimDirection : float,moveDirection : float,moveSpeed : float,size : int,score : int,time : int,missileTime:int,lives:int):
        
        self.x = x #player x coordinate
        self.y = y #player y coordinate
        self.aimChange = aimchange #player facing direction change
        self.aimDir = aimDirection #player facing Direction
        self.moveDir = moveDirection #Direction of player movement
        self.moveSpeed = moveSpeed #speed of player
        self.size = size #size of player
        self.score = score #current score of the player
        self.time = time #time since last missile
        self.missileTime = missileTime #time between missiles
        self.lives = lives#player lives

    def drawPlayer(self):
        #get some variables form self just for shorter code
        x = self.x
        y = self.y
        size = self.size
        aimDir = self.aimDir

        #Create circle
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.filledCircle(x,y,size)

        #aim settings
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.setPenRadius(1)

        #calculation of aim coordinates
        aimX = x + size*(math.sin(aimDir))
        aimY = y + size*(math.cos(aimDir))

        #create aim
        stddraw.line(x,y,aimX,aimY)

    def  movePlayer(self):
        screenX = 100
        x = self.x
        speed = self.moveSpeed #speed = amount of pixels moved
        direc = self.moveDir#direc = -1(left) or 1 (right)
        #change x pos
        x = x + (direc * speed)

        #Check if x is in the screen bounds
        if x > screenX-8 or x < -screenX+8:
            x = (screenX-8) * direc

        #set new x pos
        self.x = x
        
    
    def ChangeAim(self):
        rate = 0.5#rate of angle change

        #change direction of aim
        playerD = self.aimDir
        direc = self.aimChange
        playerD = playerD +rate* direc

        #test is aim is within bounds
        if playerD < -(math.pi)/2:
            playerD = -(math.pi)/2
            self.aimChange = 0
        elif playerD > (math.pi)/2:
            playerD = (math.pi)/2
            self.aimChange = 0

        #set new aim
        self.aimDir = playerD
    
    def drawScore(self,PlayerNum):
        stddraw.setFontSize(20)
        stddraw.setPenColor(stddraw.WHITE)
        if PlayerNum == 0:
            stddraw.text(-80 ,-90,"score: "+str(self.score))
        else:
            stddraw.text(80,-90,"score: "+str(self.score))

    def draw_missileTimer(self,playerNum):
        stddraw.setPenColor(stddraw.BLACK)
        
        if playerNum == 0:
            stddraw.rectangle(-99 ,-80,5,25)
        else:
            stddraw.rectangle(94 ,-80,5,25) 
        
        if self.time <= self.missileTime:
            stddraw.setPenColor(stddraw.RED)
        elif self.time > self.missileTime and self.time < self.missileTime*2:
            stddraw.setPenColor(stddraw.GREEN)
        else:
            stddraw.setPenColor(stddraw.BLUE)

        if self.time > self.missileTime*2:
            h = self.missileTime*2
        else:
            h = self.time

        #scale h to max 25

        h = h/(self.missileTime*2) * 25

        if playerNum == 0:
            stddraw.filledRectangle(-98 ,-80,2,h)
        else:
            stddraw.filledRectangle(95 ,-80,2,h) 
       


    #update time since last missile
    def updateTime(self):
        self.time += 5

    #check if player is allowed to fire a missile
    def isAllowed(self):
        if self.time > self.missileTime:
            self.time = 0
            return True
        else:
            return False


            
class PlayerList:
    def __init__(self):
        self.Players = []
    def add_player(self,player:Player):
        self.Players.append(player)
    def remove_player(self,player:Player):
        self.Players.remove(player)
    def draw_ScorePlayers(self):
        c = 0 #num of player
        for player in self.Players:
            player.drawPlayer()
            player.drawScore(c)
            player.draw_missileTimer(c)

            
            c+=1#increase player num

    def move_aim_timeUpdate(self):
        for player in self.Players:
            player.movePlayer()
            player.ChangeAim()
            player.updateTime()

    def hitmarks_Players(self,Missiles_list):
        nextM = True #boolean to increase missile count

        #itterate through all missiles and player locations
        mc = 0 #missile counter
        while mc < len(Missiles_list.missiles):
            nextM = True

            #check if missile is from a enemy
            if Missiles_list.missiles[mc].owner == 2:
                #Itterate through players reversed so that i can remove player if lives are done
                for player in reversed(self.Players):
                    #calculate distance between missile and player
                    distx = abs(Missiles_list.missiles[mc].x - player.x)
                    disty = abs(Missiles_list.missiles[mc].y - player.y)
                    dist = (distx**2 + disty**2)**0.5 
                    
                    #test if missile hit player
                    if dist < player.size + 1: #+1 if for missile size
                        #remove Missile
                        Missiles_list.remove_missile(Missiles_list.missiles[mc])

                        #code to decreade player health
                        player.lives -= 1

                        
                        

                        #Don't have to increase mc (new missile in old position because of pop)
                        nextM = False 
                        break # exit for
            if nextM:
                mc = mc + 1 # go to next missile 

    def hitmarks_Powerups(self,powerupList):
        #nextP = True #boolean to increase missile count

        #itterate through all missiles and player locations
        pc = 0 #powerup counter
        while pc < len(powerupList.List_Powerups):
            nextP = True #boolean to increase powerup counter
            #Itterate through players
            for player in self.Players:
                #calculate distance between powerup and player
                distx = abs(powerupList.List_Powerups[pc].x - player.x)
                disty = abs(powerupList.List_Powerups[pc].y - player.y)
                dist = (distx**2 + disty**2)**0.5 
                
                #test if powerup hit player
                if dist < player.size + 2: #+2 if for powerup size

                    #powerup type 
                    typ = powerupList.List_Powerups[pc].typ
                    #Do code to active powerup
                    self.activate_Powerup(typ,player)

                    #remove Powerup
                    powerupList.remove_powerup(powerupList.List_Powerups[pc])

                    


                    
                    

                    #Don't have to increase pc (new powerup in old position because of pop)
                    nextP = False 
                    break # exit for
            if nextP:
                pc = pc + 1 # go to next powerup 

    def activate_Powerup(self,typ,player):
        if typ == 1:
            if player.missileTime < 6:
                player.missileTime = 1
            else:
                player.missileTime -= 5
        



    
