import home
import gamerun

def main():
 
    
    #set Initial game settings
    game_settings = {
    "screen_x": 100,
    "screen_y": 100,
    "players": 1,
    "result" : False,

    } 

    #run homeloop
    home.runHomeScreen(game_settings)


    active = True

    while active:


    
        #Run gameloop
        gamerun.gameloop(game_settings)

        #Run End
        active = home.createEnd(game_settings)
    
        
    



if __name__ == "__main__":main()
