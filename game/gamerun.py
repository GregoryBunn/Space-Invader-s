import stddraw
from player import Player,PlayerList
import math
from missile import Missile,MissileList
from enemy import EnemySettings,EnemyList,Powerup_List
import random, time
import music
import sys

#Game loop and the gamerun file handles most of the game logic and was coded by all parties the class implemetation was doen by Wikus
class GameLoop:
    """
    Manages the main game loop, integrating all game components such as players, missiles, and enemies. 
    It handles game states and transitions between different levels based on the provided game settings.

    Attributes:
        _screenX (int): Width of the game screen.
        _screenY (int): Height of the game screen.
        _game_settings (GameSettings): Configuration for game settings including screen size and level.
        _timer (int): A counter used for timing events within the game.
        _level (int): Current game level.
        _PlayersList (PlayerList): Manages all player-related activities.
        _Missiles_list (MissileList): Manages all missile-related activities.
        _enemys (EnemyList): Manages all enemy-related activities.
    """
    def __init__(self,game_settings):
        self._screenX = game_settings._screen_x
        self._screenY = game_settings._screen_y
        self._game_settings = game_settings
        self._timer = 0
        self._level = game_settings._level


        #create player class
        self.PlayersList = PlayerList()

        #create missile class
        self.Missiles_list = MissileList()

        #create enemy class
        self.enemys = EnemyList() 

        if self._game_settings._level == 1:
            #create level 1 enemy settings
            self.Enemy_settingss = EnemySettings(6,2,0,1,0,6)
        elif self._game_settings._level == 2:
            #create level 2 enemy settings
            self.Enemy_settingss = EnemySettings(5,3,0,1,0,6)
        elif self._game_settings._level == 3:
            #create level 3 enemy settings
            self.Enemy_settingss = EnemySettings(4,3,1,1,0,6)
        elif self._game_settings._level == 4:
            #create level 4 enemy settings
            self.Enemy_settingss = EnemySettings(6,3,1,1,0,6)
        elif self._game_settings._level == 5:
            #create level 5 enemy settings
            self.Enemy_settingss = EnemySettings(1,1,10,1.5,1,12)
            


        #Variable to indicate an active game
        self.play = True


        #Initialize players
        self.create_players()
        #make a basic enemy grid
        self.enemys.Make_Basic_EnemyGrid(self.Enemy_settingss)

        #make list of powerups on screen
        self.powerups = Powerup_List()

    #Update game variables and draw screen
    def Update_game(self):
        """
        Updates all game elements based on the current game state, including player positions, missile trajectories, and enemy actions.
        """
        frameST = time.time()
        #Create graphics
        stddraw.clear() #clear screen
        self.createPlayscreen() #create new screen

        #draw players and their score
        self.PlayersList.draw_ScorePlayers()



        #Move enemys
        self.enemys.Move_Enemys()

        #draw enemys   
        self.enemys.Draw_Enemys()
            
        #check if game has ended 
        self.play = self.enemys.Check_for_End(self._game_settings,self.PlayersList)

        #check if enemys have been hit
        self.enemys.hitmarks(self.Missiles_list,self.PlayersList,self.powerups,self._game_settings)

        #move Powerups and draw them=
        self.powerups.move_draw_Powerups()

        #check if player hit powerup
        self.PlayersList.hitmarks_Powerups(self.powerups)

        #check if players have been hit
        self.PlayersList.hitmarks_Players(self.Missiles_list)

        

        #draw and move missiles
        self.Missiles_list.move_drawMissiles()
        
        #Get the time it took the run the update code
        frameEND = time.time()
        #print(f'proccess time: {frameEND-frameST}')


        #show Graphics
        '''
        The next few lines of code does the math inorder to have a consistent frame rate throughout the game
        '''
        #Code added by Greg
        #______________________________________________________________________________________________________
        try:
            fps = 1/(frameEND - frameST)
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.text(90, 90, '%.0f' % (fps))
            if fps < 30:
                stddraw.show(0)
            else:
                stddraw.show(1000/30 - (frameEND-frameST)*1000)
        except Exception: 
            stddraw.show(1000/30)
        #_______________________________________________________________________________________________________
        

        #move Player & aim Player + update Time since last missile/player
        self.PlayersList.move_aim_timeUpdate()

    #Counter attack
    def counter_Attack(self):
        """
        Handles enemy counter-attacks, determining when and how enemies respond to player actions.
        """
        #check if enemys can shoot back
        if self._level != 0:
            #Counter attack intensity
            intensity = 5- self._level 
            if intensity < 1: intensity = 1 #Intensity between 1 and 4

            #check if enough time has passed since previous counter attack and if there is enemys
            if self._timer % (10*intensity)==0 and len(self.enemys._Enemylist)>0 :
                #get random enemy
                enemy = random.randint(0,len(self.enemys._Enemylist)-1)
                #get enemy location
                x = self.enemys._Enemylist[enemy]._x
                y = self.enemys._Enemylist[enemy]._y

                MissileSize = 5
                self.Missiles_list.add_missile(Missile(x,y,0,0,2,MissileSize))

    #Process input type 0
    def Process_inputType0(self):
        """
        Processes player inputs of type 0, typically involving direct control mechanisms such as keyboard or joystick inputs.
        """
        #Check for input
        if stddraw.hasNextKeyTyped():

            #Process input
            key = stddraw.nextKeyTyped()

            if key == "d":#move right
                self.PlayersList._Players[0]._moveDir = 1
            elif key == "a":#move left
                self.PlayersList._Players[0]._moveDir = -1


            elif key == "s":#stop moving
                self.PlayersList._Players[0]._moveDir = 0

            elif key == "x":#exit
                self._play = False

            elif key == "e":#rotate right
                self.PlayersList._Players[0]._aimChange = 0.07

            elif key == "q":#rotate lefr                
                self.PlayersList._Players[0]._aimChange = -0.07

            elif key == "w":#stop rotate   
                self.PlayersList._Players[0]._aimChange = 0
            elif key == "x":#exit
                sys.exit()

            elif key == " ":#shoot
                self.fireMissile(0)

            #process second player input if there is one
            if self._game_settings._players == 2:


                if key == ";":#shoot
                    
                    self.fireMissile(1)


                elif key == "l":#move right
                        self.PlayersList._Players[1]._moveDir = 1
                elif key == "j":#move left
                    self.PlayersList._Players[1]._moveDir = -1


                elif key == "k":#stop moving
                    self.PlayersList._Players[1]._moveDir = 0

                elif key == "o":#rotate right
                    self.PlayersList._Players[1]._aimChange = 0.07

                elif key == "u":#rotate lefr                
                    self.PlayersList._Players[1]._aimChange = -0.07

                elif key == "i":#stop rotate   
                    self.PlayersList._Players[1]._aimChange = 0
                


    #Process input type 1  
    #This input type was done by Greg              
    def Process_inputType1(self):
        """
        Processes player inputs of type 1, typically involving more complex control mechanisms or AI-driven inputs.
        """

        #keyboard inputs
        keys = stddraw.getKeysPressed()
            
        
        if keys[stddraw.K_e]: #rotate left
            self.PlayersList._Players[0]._aimChange = 0.07
        elif keys[stddraw.K_q]: #rotate rigth
            self.PlayersList._Players[0]._aimChange = -0.07
        else: #stop rotate
             self.PlayersList._Players[0]._aimChange = 0
 
        if keys[stddraw.K_w]:
            pass
            #set angle to straight
        if keys[stddraw.K_a]:#move left
            self.PlayersList._Players[0]._moveDir = -1
        elif keys[stddraw.K_d]:#move right
            self.PlayersList._Players[0]._moveDir = 1
        elif keys[stddraw.K_x]:#exit
            sys.exit()
        else:   
            self.PlayersList._Players[0]._moveDir = 0#stop movement
        if keys[stddraw.K_SPACE]:
            self.fireMissile(0)#fire missile


        #process second player input if there is one
        if self._game_settings.players == 2:
        
            #keyboard inputs
            keys = stddraw.getKeysPressed()
                
            
            if keys[stddraw.K_o]: #rotate left
                self.PlayersList._Players[1]._aimChange = 0.07
            elif keys[stddraw.K_u]: #rotate right
                self.PlayersList._Players[1]._aimChange = -0.07
            else:
                self.PlayersList._Players[1]._aimChange = 0#stop rotate
    
            if keys[stddraw.K_i]:
                pass
                #set angle to straight
            if keys[stddraw.K_j]:#move left
                self.PlayersList._Players[1]._moveDir = -1
            elif keys[stddraw.K_l]:#move right
                self.PlayersList._Players[1]._moveDir = 1
            else: #stop moving
                self.PlayersList._Players[1]._moveDir = 0

            if keys[stddraw.K_n]:#fire missile
                self.fireMissile(1)


            

    #run
    def run(self):
        """
        Starts and maintains the game loop until the end of the game, handling transitions between game states and processing all game actions.
        """
        while self.play:
            self._timer += 1#update time that has passed
            self.Update_game() #Update all the game characteristics
            self.counter_Attack() #call the enemy counter attack function

            #handle input depending in  input type
            if self._game_settings._inputType == 0:
                self.Process_inputType0()
            elif self._game_settings._inputType == 1:
                self.Process_inputType1()

    #create Players
    def create_players(self):
        """
        Initializes players in the game, setting up their starting positions and configurations based on the game settings.
        """
        for i in range(self._game_settings.players):
            # p is the amount of players
            if i == 0:
                p = self._game_settings._player1List
            else:
                p = self._game_settings._player2List
            self.PlayersList.add_player(Player(0+(i*10),-80,0,0,0,1.7,8,0,50,100,3,p))#Create players
        
    #create the play screen background
    def createPlayscreen(self):
        """
        Sets up the visual components of the play screen at the start of the game or when the game level changes.
        """
        stddraw.clear(stddraw.BLACK)#form color
        #scale form
        stddraw.setXscale(-self._screenX,self._screenY)
        stddraw.setYscale(-self._screenY,self._screenY)
        stddraw.setFontSize(15)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.text(0,-95,"Total score: "+str(self._game_settings._score))

    def fireMissile(self,p):
        """
        Controls the firing of missiles by players, determining the timing and positioning of missile launches.
        """
        #check if missile is allowed
        if self.PlayersList._Players[p].isAllowed():
        #if 1 ==1:

            #get direction of new missile
            d = self.PlayersList._Players[p]._aimDir
    

            #add missile
            music.bullet()#play missile sound
            #test for super missile
            if self.PlayersList._Players[p]._time >= self.PlayersList._Players[p]._missileTime*2:
                missiletype = 2#Super missile
                MissileSize = 5
            else:
                missiletype = 1#Basic missile 
                MissileSize = 2.5
            #Get  missile starting coordinates
            x = self.PlayersList._Players[p]._x+(10*math.sin(d))
            y = self.PlayersList._Players[p]._y+(10*math.cos(d))+abs(66//2-66//2.2)#the abs is to adjust for the image rotation
            AimDir = self.PlayersList._Players[p]._aimDir
            #create missile
            self.Missiles_list.add_missile(Missile(x,y,AimDir,missiletype,p,MissileSize))
            #make missile timer 0
            self.PlayersList._Players[p]._time = 0

        
