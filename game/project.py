
'''
Main project

'''

from home import HomeScreen,EndScreen,PlayerSelect
from gamerun import GameLoop
import threading
import time
import stddraw
from stddraw import picture
from picture import Picture
from color import Color 
import math



#game settings
class GameSettings:
    #has three parameters
    def __init__(self,screenXsize,screenYsize,players,inputType,level : int,p1,p2):
        #initialize parameters
        self.screen_x = 100
        self.screen_y = 100
        self.players = players
        self.result = False
        self.inputType = inputType
        self.x = screenXsize
        self.y = screenYsize
        self.level = level
        self.player1List = p1
        self.player2List = p2

class Game:
    #initialized with settings
    def __init__(self,settings):
        #game settings
        self.settings = settings

        #self playerchoose screen initialized GREG
        self.Select_Screen = PlayerSelect(self.settings)

        #Game homescreen initialized
        self.home_screen = HomeScreen(self.settings)

        #Game Endscreen initialized
        self.end_screen = EndScreen(self.settings)
    
    #starts game
    def run(self,p1,p2):

        #createPlayerChoose screen GREG
        self.Select_Screen.run()

        #create homscreen
        self.home_screen.run()

        #indicates active game
        active = True

        #Wait for the player threads to complete
        p1.join()
        p2.join()

        #games main loop(continues rounds)
        while active:

    
            #Run gameloop
            #gamerun.gameloop(self.settings)
            game = GameLoop(self.settings)
            game.run()



            #Run End
            active = self.end_screen.run()
   

def createPlayerPicture(num,lis,pic):
    pi = math.pi
    angle = -pi/2
    width = pic.width()
    heigth = pic.height()
    cx = width // 2
    cy = heigth // 2
    while angle < pi/2:
        rotatedpic = Picture(width, heigth)
        cosMinusTheta = math.cos(-angle)
        sinMinusTheta = math.sin(-angle)
        for tx in range(width):
            for ty in range(heigth):
                dX: int = tx - cx
                dY: int = ty - cy             
                sx = int(dX*cosMinusTheta - dY*sinMinusTheta + cx)
                sy = int(dX*sinMinusTheta + dY*cosMinusTheta + cy)
                col: Color = stddraw.BLACK
                if ((sx >= 0) and (sx < width) and (sy >= 0) and (sy < heigth)):
                    col = pic.get(sx, sy)
                rotatedpic.set(tx, ty, col)
        angle += pi/48 
        lis.append(rotatedpic)
        #picture(rotatedpic, 0.5, 0.5)
        #stddraw.show(20)


def main():

    

    #Picture list
    picture_list1 = []
    picture_list2 = []
    #create thread for player pictures and start them
    player1TH = threading.Thread(target=createPlayerPicture, args=(0, picture_list1, Picture('Ship1.png')))
    player2TH = threading.Thread(target=createPlayerPicture, args=(1, picture_list2, Picture('Ship1.png')))
    player1TH.start()
    player2TH.start()
    
    #Create new instance of gamesettigns
    settings_game = GameSettings(screenXsize=512,screenYsize=512,players=1,inputType=1,level=1,p1=picture_list1,p2=picture_list2)

    #initialize game
    game = Game(settings=settings_game)


    #run game
    game.run(player1TH,player2TH)
    
    
        
    



if __name__ == "__main__":main()
