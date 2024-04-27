import stddraw
from player import Player,PlayerList
import math
from missile import Missile,MissileList
from enemy import EnemySettings,EnemyList,Powerup,Powerup_List
import random, time


class GameLoop:
    def __init__(self,game_settings):
        self.screenX = game_settings.screen_x
        self.screenY = game_settings.screen_y
        self.game_settings = game_settings
        self.timer = 0
        self.level = game_settings.level

        #create player class
        self.PlayersList = PlayerList()

        #create missile class
        self.Missiles_list = MissileList()

        #create enemy class
        self.enemys = EnemyList() 

        if self.game_settings.level == 1:
            #create level 1 enemy settings
            self.Enemy_settingss = EnemySettings(5,3,1,1,0,6)
        elif self.game_settings.level ==2:
            #create level 2 enemy settings
            self.Enemy_settingss = EnemySettings(8,3,1,1,0,6)
        elif self.game_settings.level == 3:
            #create level 3 enemy settings
            self.Enemy_settingss = EnemySettings(1,1,1,1,1,12)
            


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
        self.play = self.enemys.Check_for_End(self.game_settings,self.PlayersList)

        #check if enemys have been hit
        self.enemys.hitmarks(self.Missiles_list,self.PlayersList,self.powerups)

        #move Powerups and draw them
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
        try:
            totTime = (frameEND - frameST)*1000
            #stddraw.text(1.8, 1.8, '%.0f' % (fps))
            if totTime > 24:
                stddraw.show(0)
            else:
                stddraw.show(24 - totTime)
        except Exception: 
            stddraw.show(24)

        
        

        #move Player & aim Player + update Time since last missile/player
        self.PlayersList.move_aim_timeUpdate()

    #Counter attack
    def counter_Attack(self):
        #check if enemys can shoot back
        if self.level != 0:
            #Counter attack intensity
            intensity = 5- self.level 
            if intensity < 1: intensity = 1 #Intensity between 1 and 4

            #check if enough time has passed since previous counter attack and if there is enemys
            if self.timer % (10*intensity)==0 and len(self.enemys.Enemylist)>0 :
                #get random enemy
                enemy = random.randint(0,len(self.enemys.Enemylist)-1)
                #get enemy location
                x = self.enemys.Enemylist[enemy].x
                y = self.enemys.Enemylist[enemy].y

                MissileSize = 5
                self.Missiles_list.add_missile(Missile(x,y,0,0,2,MissileSize))

    #Process input type 0
    def Process_inputType0(self):
        #Check for input
        if stddraw.hasNextKeyTyped():

            #Process input
            key = stddraw.nextKeyTyped()

            if key == "d":#move right
                self.PlayersList.Players[0].moveDir = 1
            elif key == "a":#move left
                self.PlayersList.Players[0].moveDir = -1


            elif key == "s":#stop moving
                self.PlayersList.Players[0].moveDir = 0

            elif key == "x":#exit
                self.play = False

            elif key == "e":#rotate right
                self.PlayersList.Players[0].aimChange = 0.07

            elif key == "q":#rotate lefr                
                self.PlayersList.Players[0].aimChange = -0.07

            elif key == "w":#stop rotate   
                self.PlayersList.Players[0].aimChange = 0

            elif key == " ":#shoot
                
                #check if missile is allowed
                if self.PlayersList.Players[0].isAllowed():


                    #get direction of new missile
                    d = self.PlayersList.Players[0].aimDir
            

                    #add missile
                    missiletype = 1#Type of missile
                    x = self.PlayersList.Players[0].x+(10*math.sin(d))
                    y = self.PlayersList.Players[0].y+(10*math.cos(d))
                    AimDir = self.PlayersList.Players[0].aimDir
                    MissileSize = 2.5
                    self.Missiles_list.add_missile(Missile(x,y,AimDir,missiletype,0,MissileSize))
                else:
                    pass

            #process second player input if there is one
            if self.game_settings.players == 2:


                if key == ";":#shoot
                    
                    #check if missile is allowed
                    if self.PlayersList.Players[1].isAllowed():


                        #get direction of new missile
                        d = self.PlayersList.Players[1].aimDir
                

                        #add missile
                        missiletype = 1#Type of missile
                        x = self.PlayersList.Players[1].x+(10*math.sin(d))
                        y = self.PlayersList.Players[1].y+(10*math.cos(d))
                        AimDir = self.PlayersList.Players[1].aimDir
                        MissileSize = 2.5
                        self.Missiles_list.add_missile(Missile(x,y,AimDir,missiletype,1,MissileSize))

                    
                        

                    else: #if missile is not allowed
                        pass

                elif key == "l":#move right
                        self.PlayersList.Players[1].moveDir = 1
                elif key == "j":#move left
                    self.PlayersList.Players[1].moveDir = -1


                elif key == "k":#stop moving
                    self.PlayersList.Players[1].moveDir = 0

                elif key == "o":#rotate right
                    self.PlayersList.Players[1].aimChange = 0.07

                elif key == "u":#rotate lefr                
                    self.PlayersList.Players[1].aimChange = -0.07

                elif key == "i":#stop rotate   
                    self.PlayersList.Players[1].aimChange = 0


    #Process input type 1                
    def Process_inputType1(self):

        #keyboard inputs
        keys = stddraw.getKeysPressed()
            
        
        if keys[stddraw.K_e]: 
            self.PlayersList.Players[0].aimChange = 0.07
        elif keys[stddraw.K_q]: 
            self.PlayersList.Players[0].aimChange = -0.07
        else:
             self.PlayersList.Players[0].aimChange = 0
 
        if keys[stddraw.K_w]:
            pass
            #set angle to straight
        if keys[stddraw.K_a]:
            self.PlayersList.Players[0].moveDir = -1
        elif keys[stddraw.K_d]:
            self.PlayersList.Players[0].moveDir = 1
        else: 
           
            self.PlayersList.Players[0].moveDir = 0
        if keys[stddraw.K_SPACE]:
            #check if missile is allowed
            if self.PlayersList.Players[0].isAllowed():


                #get direction of new missile
                d = self.PlayersList.Players[0].aimDir
        

                #add missile
                missiletype = 1#Type of missile
                x = self.PlayersList.Players[0].x+(10*math.sin(d))
                y = self.PlayersList.Players[0].y+(10*math.cos(d))
                AimDir = self.PlayersList.Players[0].aimDir
                MissileSize = 2.5
                self.Missiles_list.add_missile(Missile(x,y,AimDir,missiletype,0,MissileSize))
            else:
                pass
        #process second player input if there is one
        if self.game_settings.players == 2:
        
            #keyboard inputs
            keys = stddraw.getKeysPressed()
                
            
            if keys[stddraw.K_o]: 
                self.PlayersList.Players[1].aimChange = 0.07
            elif keys[stddraw.K_u]: 
                self.PlayersList.Players[1].aimChange = -0.07
            else:
                self.PlayersList.Players[1].aimChange = 0
    
            if keys[stddraw.K_i]:
                pass
                #set angle to straight
            if keys[stddraw.K_j]:
                self.PlayersList.Players[1].moveDir = -1
            elif keys[stddraw.K_l]:
                self.PlayersList.Players[1].moveDir = 1
            else: 
            
                self.PlayersList.Players[1].moveDir = 0
            if keys[stddraw.K_n]:
                #check if missile is allowed
                if self.PlayersList.Players[1].isAllowed():


                    #get direction of new missile
                    d = self.PlayersList.Players[1].aimDir
            

                    #add missile
                    missiletype = 1#Type of missile
                    x = self.PlayersList.Players[1].x+(10*math.sin(d))
                    y = self.PlayersList.Players[1].y+(10*math.cos(d))
                    AimDir = self.PlayersList.Players[1].aimDir
                    MissileSize = 2.5
                    self.Missiles_list.add_missile(Missile(x,y,AimDir,missiletype,1,MissileSize))
                else:
                    pass
            

    #run
    def run(self):
        while self.play:
            self.timer += 1
            self.Update_game()
            self.counter_Attack()


            if self.game_settings.inputType == 0:
                self.Process_inputType0()
            elif self.game_settings.inputType == 1:
                self.Process_inputType1()

    #create Players
    def create_players(self):
        for i in range(self.game_settings.players):
            if i == 0:
                p = self.game_settings.player1List
            else:
                p = self.game_settings.player2List
            self.PlayersList.add_player(Player(0+(i*10),-80,0,0,0,1.7,8,0,50,100,3,p))
        
    #create the play screen background
    def createPlayscreen(self):
        stddraw.clear(stddraw.BLACK)#form color
        #scale form
        stddraw.setXscale(-self.screenX,self.screenY)
        stddraw.setYscale(-self.screenY,self.screenY)