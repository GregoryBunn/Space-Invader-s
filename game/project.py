
'''
Main project

'''

from home import HomeScreen,EndScreen
from gamerun import GameLoop



#game settings
class GameSettings:
    #has three parameters
    def __init__(self,screenXsize,screenYsize,players,inputType,level : int):
        #initialize parameters
        self.screen_x = 100
        self.screen_y = 100
        self.players = players
        self.result = False
        self.inputType = inputType
        self.x = screenXsize
        self.y = screenYsize
        self.level = level

class Game:
    #initialized with settings
    def __init__(self,settings):
        #game settings
        self.settings = settings

        #Game homescreen initialized
        self.home_screen = HomeScreen(self.settings)

        #Game Endscreen initialized
        self.end_screen = EndScreen(self.settings)
    
    #starts game
    def run(self):

        #create homscreen
        self.home_screen.run()

        #indicates active game
        active = True

        #games main loop(continues rounds)
        while active:


    
            #Run gameloop
            #gamerun.gameloop(self.settings)
            game = GameLoop(self.settings)
            game.run()



            #Run End
            active = self.end_screen.run()





    

def main():

    #Create new instance of gamesettigns
    settings_game = GameSettings(screenXsize=512,screenYsize=512,players=2,inputType=0,level=1)

    #initialize game
    game = Game(settings=settings_game)

    #run game
    game.run()
    
    
        
    



if __name__ == "__main__":main()
