import stddraw
import time
import player
import missile
import math
import enemy


def createPlayscreen(x,y):
    stddraw.clear(stddraw.GRAY)#form color
    #scale form
    stddraw.setXscale(-x,x)
    stddraw.setYscale(-y,y)


#Main game function(LOOP)
def gameloop(game_settings): 

    #create players list (for Dictionary)
    player_info = []
    screenY = game_settings["screen_x"]
    screenX = game_settings["screen_y"]

    #create player/players
    for i in range(game_settings["players"]):


        player_info = {

        #NB cant create more than one player
        "player_x" : 0, #player x coordinate
        "player_y" : int((screenY/10)*-8),#player y coordinate
        "player_dir_change" : 0, #player facing direction change 
        "playerDir": 0, #player facing Direction
        "playerMoveDir": 0, #Direction of player movement  
        "playerSpeed": 1.7, #speed of player
        "playerSize": 8, #size of player
        "score": 0, #current score of the player
        "time":0, #time since last missile
        "missileS": 10 #time between missiles
        } 


    #create missile list(for dictionary)
    missiles = []

    missiletype = 1 #Type of missile

    #create enemy list(for dictionary)
    enemys = []

    #create enemy settings
    Enemy_settings = {
            "countx" : 8,
            "county" : 3,
            "size" : 6,
            "ID" : 1,
            "Dir": 1,

            }

    enemy.createEnemy(enemys,Enemy_settings)



    #variable to indicate an active game
    play = True

    while play:

        #Create graphics
        stddraw.clear() #clear screen
        createPlayscreen(screenX,screenY) #create new screen
        enemy.hitmarks(enemys,Enemy_settings,missiles,player_info) #check if enemys have been hit
        enemy.moveEnemy(enemys,Enemy_settings) #Move enemys
        play = enemy.checkForEnd(enemys,game_settings,player_info)#check if game has ended
        enemy.drawEnemy(enemys) #draw enemys
        player.createPlayer(player_info) #draw players
        missile.createMissiles(missiles,missiletype,player_info["playerDir"]) #draw missiles
        player.drawScore(player_info,screenX,screenY) #draw score

        



        #Check for input
        if stddraw.hasNextKeyTyped():

            #Process input
            key = stddraw.nextKeyTyped()

            if key == "d":#move right
                player_info["playerMoveDir"] = 1


            elif key == "a":#move left
                player_info["playerMoveDir"] = -1

 
            elif key == "s":#stop moving
                player_info["playerMoveDir"] = 0

            elif key == "x":#exit
                play = False

            elif key == " ":#shoot

                #check if missile is allowed
                if missile.isAllowed(player_info):


                    #get direction of new missile
                    d = player_info["playerDir"]
                    #add missile
                    missiles.append({"x": player_info["player_x"]+(10*math.sin(d)),
                            "y": player_info["player_y"]+(10*math.cos(d)),
                            "dir": player_info["playerDir"],
                            })

                else: #if missile is not allowed
                    pass

            elif key == "e":#rotate right
                player_info["player_dir_change"] = 0.07

            elif key == "q":#rotate lefr
                player_info["player_dir_change"] = -0.07

            elif key == "w":#stop rotate
                player_info["player_dir_change"] = 0
                

        #get new missiles positions
        missiles = missile.moveM(missiles,screenX,screenY)


        #get new player position
        player_info["player_x"] = player.moveP(player_info,screenX)
    

        #get new aim direction
        player_info["playerDir"] = player.changeAimDir(player_info) 










        #show Graphics
        stddraw.show(50)

        #Increase time since last missile was fired
        player_info["time"]+=1






