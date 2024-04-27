
'''
Main project
sound: Pixabay
The Final Boss Battle : alperomeresin
8-bit Air Fight : moodmode
 
'''

from home import HomeScreen,EndScreen,PlayerSelect
from gamerun import GameLoop
import threading, stddraw, math, music
from stddraw import picture
from picture import Picture

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
        self.score = 0
        self.txt = "highscore.txt"
        self.highScore = self.getHighScore()

    def getHighScore(self):   
        f = open(self.txt, "r")
        score = f.read()
        f.close()
        if len(score) > 0:
            return int(score)
        else:
            return 0
    def setHighScore(self,score):
        self.highScore = score
        self.writeHighScore()
    def writeHighScore(self):
        f = open(self.txt,"w")
        f.write(str(self.highScore))
        f.close()

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

            

        
            if self.settings.result == True and self.settings.level ==3:
                self.settings.level += 1
                self.end_screen.run()
                self.settings.level = 1
            elif self.settings.result == True:
                self.settings.level += 1
                self.end_screen.run()
            elif self.settings.result == False:
                #self.settings.level = 1
                self.end_screen.run()
                self.settings.score = 0


            


            #Run End
   

def createPlayerPicture(num,lis,pic):
    pi = math.pi
    angle = -pi/2
    width = pic.width()
    heigth = pic.height()
    cx = width // 2
    cy = heigth // 2
    while angle < pi/2:
        rotatedpic = Picture(width, heigth)
        #rotatedpic = Picture('invis.png')
        cosMinusTheta = math.cos(-angle)
        sinMinusTheta = math.sin(-angle)
        for tx in range(width):
            for ty in range(heigth):
                if ty < heigth//2:#//2 unsures only the turret rotates
                    dX: int = tx - cx
                    dY: int = ty - cy             
                    sx = int(dX*cosMinusTheta - dY*sinMinusTheta + cx)
                    sy = int(dX*sinMinusTheta + dY*cosMinusTheta + cy)
                    col = stddraw.BLACK
                    if ((sx >= 0) and (sx < width) and (sy >= 0) and (sy < heigth)):
                        col = pic.get(sx, sy)

                        #Make sure nothing else then the turret is rotated
                        if (sx < 10) or (sx > 50):
                            col = stddraw.BLACK
                        
                else:
                    col = pic.get(tx,ty)

                
                rotatedpic.set(tx, ty, col)
        angle += pi/48 
        lis.append(rotatedpic)




def main():

    

    #Picture list
    picture_list1 = []
    picture_list2 = []
    #create thread for player pictures and start them
    player1TH = threading.Thread(target=createPlayerPicture, args=(0, picture_list1, Picture('Ship1A.png')))
    player2TH = threading.Thread(target=createPlayerPicture, args=(1, picture_list2, Picture('Ship2A.png')))

   
    music.playSong()
    player1TH.start()
    player2TH.start()
    
    #Create new instance of gamesettigns
    settings_game = GameSettings(screenXsize=512,screenYsize=512,players=1,inputType=1,level=1,p1=picture_list1,p2=picture_list2)

    #initialize game
    game = Game(settings_game)


    #run game
    game.run(player1TH,player2TH)
    
    
        
    



if __name__ == "__main__":main()
