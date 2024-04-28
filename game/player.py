import stddraw
import math
from stddraw import picture
import music
import time







class Player:
    """
    Represents a player character in the game with attributes for movement, aiming, and scoring.

    Attributes:
        _x (float): The x-coordinate of the player.
        _y (float): The y-coordinate of the player.
        _aimChange (float): Amount of change in aiming direction per update.
        _aimDir (float): Current aiming direction in radians.
        _moveDir (float): Current moving direction; -1 for left, 1 for right.
        _moveSpeed (float): Speed of player movement.
        _size (int): Size of the player, affecting collision detection.
        _score (int): Current score of the player.
        _time (int): Timer since the last missile was fired.
        _missileTime (int): Required delay time between firing missiles.
        _lives (int): Number of lives the player has.
        _picList (list): List of images for different player states.
        _picture (Picture): Current picture representing the player.

    Methods:
        RotatePlayer(aimdir): Rotates the player to a new aim direction based on aimdir.
        drawPlayer(): Draws the player on the game screen.
        movePlayer(): Updates the player's position based on their move direction and speed.
        ChangeAim(): Changes the player's aiming direction within allowed bounds.
        drawScore(PlayerNum): Displays the player's score on the screen.
        drawLives(PlayerNum): Displays the number of lives left for the player.
        draw_missileTimer(playerNum): Draws a timer that indicates the readiness of the next missile.
        updateTime(): Increments the internal timer to manage missile firing readiness.
        isAllowed(): Checks if the player is allowed to fire a missile based on the timer.
    """
    
    def __init__(self,x : float,y : float,aimchange : float,aimDirection : float,moveDirection : float,moveSpeed : float,size : int,score : int,time : int,missileTime:int,lives:int,pictures):
        
        self._x = x #player x coordinate
        self._y = y #player y coordinate
        self._aimChange = aimchange #player facing direction change
        self._aimDir = aimDirection #player facing Direction
        self._moveDir = moveDirection #Direction of player movement
        self._moveSpeed = moveSpeed #speed of player
        self._size = size #size of player
        self._score = score #current score of the player
        self._time = time #time since last missile
        self._missileTime = missileTime #time between missiles
        self._lives = lives#player lives
        self._picList = pictures
        self._picture = self._picList[24]


    #Function that rotates player by choosing an image based on aim direction
    def RotatePlayer(self,aimdir):
        pos = int((aimdir/(math.pi/2))*24) + 24
        self._picture = self._picList[pos]
       




    def drawPlayer(self):
        #get some variables form self just for shorter code
        x = self._x
        y = self._y
        size = self._size
        aimDir = self._aimDir
        #Create player


        #rotate if needed
        if self._aimChange != 0:
            self.RotatePlayer(aimDir)
            
            #change angle
        #Draw player
        picture(self._picture, self._x, self._y)
        

        #draw aimLine
        #aim settings
        #stddraw.setPenColor(stddraw.GREEN)
        #stddraw.setPenRadius(1)
        #calculation of aim coordinates
        #aimX = x + size*(math.sin(aimDir))
        #aimY = y + size*(math.cos(aimDir))
        #create aim
        #stddraw.line(x,y,aimX,aimY)


        #Advanced graphics
        


    def  movePlayer(self):
        screenX = 100
        x = self._x
        speed = self._moveSpeed #speed = amount of pixels moved
        direc = self._moveDir#direc = -1(left) or 1 (right)
        #change x pos
        x = x + (direc * speed)

        #Check if x is in the screen bounds
        if x > screenX-8 or x < -screenX+8:
            x = (screenX-8) * direc

        #set new x pos
        self._x = x
        
    
    def ChangeAim(self):
        rate = 0.5#rate of angle change

        #change direction of aim
        playerD = self._aimDir
        direc = self._aimChange
        playerD = playerD +rate* direc

        #test if aim is within bounds
        if playerD < -(math.pi)/2:
            playerD = -(math.pi)/2
            self._aimChange = 0
        elif playerD > (math.pi)/2:
            playerD = (math.pi)/2
            self._aimChange = 0

        #set new aim
        self._aimDir = playerD
    
    #Draw score of player
    def drawScore(self,PlayerNum):
        stddraw.setFontSize(20)
        stddraw.setPenColor(stddraw.WHITE)
        if PlayerNum == 0:
            stddraw.text(-80 ,-85,"score: "+str(self._score))
        else:
            stddraw.text(80,-85,"score: "+str(self._score))

    #Draw lives of player
    def drawLives(self,PlayerNum):
        
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.text(-82+(PlayerNum*152), -95, "Lives: ")
        #checks player lives and draws images
        stddraw.setPenColor(stddraw.RED)
        for i in range(self._lives): stddraw.filledCircle((-68 + i*6.1)+(PlayerNum*152), -96, 3)
        
        


    def draw_missileTimer(self,playerNum):
        #Draw the time since the last missile was fired for a player
        stddraw.setPenColor(stddraw.DARK_GRAY)
        
        if playerNum == 0:
            stddraw.rectangle(-99 ,-80,5,25)
        else:
            stddraw.rectangle(94 ,-80,5,25) 
        
        #Timer red if missile not allowed
        if self._time <= self._missileTime:
            stddraw.setPenColor(stddraw.RED)
        #Timer green if missile is allowed
        elif self._time > self._missileTime and self._time < self._missileTime*2:
            stddraw.setPenColor(stddraw.GREEN)
        else:
            #Timer Blue if super missile is allowed
            stddraw.setPenColor(stddraw.BLUE)

        #Cap the height to double the allowed time
        if self._time > self._missileTime*2:
            h = self._missileTime*2
        else:
            h = self._time

        #scale h to max 25
        h = h/(self._missileTime*2) * 25

        if playerNum == 0:
            stddraw.filledRectangle(-98 ,-80,2,h)
        else:
            stddraw.filledRectangle(95 ,-80,2,h) 
       


    #update time since last missile
    def updateTime(self):
        self._time += 5

    #check if player is allowed to fire a missile
    def isAllowed(self):
        if self._time > self._missileTime:
            return True
        else:
            return False


            
class PlayerList:
    """
    Manages a collection of players in the game. Handles their drawing, movement, and interactions with game elements like missiles and powerups.

    Methods:
        add_player(player: Player): Adds a player to the list.
        remove_player(player: Player): Removes a player from the list.
        draw_ScorePlayers(): Draws all players along with their scores, missile timers, and lives.
        move_aim_timeUpdate(): Updates the movement, aim, and timers for all players.
        hitmarks_Players(Missiles_list): Checks and handles collisions between players and missiles.
        hitmarks_Powerups(powerupList): Checks and handles collisions between players and powerups, activating any powerups.
        activate_Powerup(typ, player): Activates a powerup effect based on the powerup type.
    """
    def __init__(self):
        self._Players = []
    def add_player(self,player:Player):
        self._Players.append(player)
    def remove_player(self,player:Player):
        self._Players.remove(player)
    def draw_ScorePlayers(self):
        c = 0 #num of player
        for player in self._Players:
            player.drawPlayer()
            player.drawScore(c)
            player.draw_missileTimer(c)
            player.drawLives(c)
            c+=1#increase player num

    #Itterate throuhg player and update their positions aim and time
    def move_aim_timeUpdate(self):
        for player in self._Players:
            player.movePlayer()
            player.ChangeAim()
            player.updateTime()

    def hitmarks_Players(self,Missiles_list):
        nextM = True #boolean to increase missile count

        #itterate through all missiles and player locations
        mc = 0 #missile counter
        while mc < len(Missiles_list._missiles):
            nextM = True

            #check if missile is from a enemy
            if Missiles_list._missiles[mc]._owner == 2:
                #Itterate through players reversed so that i can remove player if lives are done
                for player in reversed(self._Players):
                    #calculate distance between missile and player
                    distx = abs(Missiles_list._missiles[mc]._x - player._x)
                    disty = abs(Missiles_list._missiles[mc]._y - player._y)
                    dist = (distx**2 + disty**2)**0.5 
                    
                    #test if missile hit player
                    if dist < player._size + Missiles_list._missiles[mc]._size: # + for missile size
                        #remove Missile
                        Missiles_list.remove_missile(Missiles_list._missiles[mc])

                        #code to decreade player health
                        player._lives -= 1

                        
                        music.Player()
                        

                        #Don't have to increase mc (new missile in old position because of pop)
                        nextM = False 
                        break # exit for
            if nextM:
                mc = mc + 1 # go to next missile 

    def hitmarks_Powerups(self,powerupList):
        #nextP = True #boolean to increase missile count

        #itterate through all missiles and player locations
        pc = 0 #powerup counter
        while pc < len(powerupList._List_Powerups):
            nextP = True #boolean to increase powerup counter
            #Itterate through players
            for player in self._Players:
                #calculate distance between powerup and player
                distx = abs(powerupList._List_Powerups[pc]._x - player._x)
                disty = abs(powerupList._List_Powerups[pc]._y - player._y)
                dist = (distx**2 + disty**2)**0.5 
                
                #test if powerup hit player
                if dist < player._size + 2: #+2 if for powerup size

                    #powerup type 
                    typ = powerupList._List_Powerups[pc]._typ
                    #Do code to active powerup
                    self.activate_Powerup(typ,player)

                    #remove Powerup
                    powerupList.remove_powerup(powerupList._List_Powerups[pc])

                    


                    
                    

                    #Don't have to increase pc (new powerup in old position because of pop)
                    nextP = False 
                    break # exit for
            if nextP:
                pc = pc + 1 # go to next powerup 

    def activate_Powerup(self,typ,player):

        if typ == 1:#Activate type 1 missile
            #Only allow if allow if time less than 45
            if player._missileTime < 45: 
                player._missileTime = 45
            else:
                player._missileTime -= 10

        if typ == 2:#type 2 missile
            # only allow if live are less then 3
            if player._lives < 3:
                player._lives += 1

        if typ == 3:#Type 3 missile
            #only allow if move speed is not to high
            if player._moveSpeed < 3.5:
                player._moveSpeed += 0.5