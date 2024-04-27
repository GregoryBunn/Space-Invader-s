
'''
Main project

Classes:
GameSettings: Game settings functions
Game: Handels the multiple levels and runs the game

Methods:
    Main(): Runs the  game
    createPlayerPicture(): Create different angles of the shooter before the game starts
 
'''

from home import HomeScreen,EndScreen,PlayerSelect
from gamerun import GameLoop
import threading, stddraw, math, music
from stddraw import picture
from picture import Picture

#game settings
class GameSettings:
    #has three parameters
    """
    Manages the game settings including screen size, player settings, input types, and level details.

    Attributes:
        screen_x (int): Width of the game screen.
        screen_y (int): Height of the game screen.
        players (int): Number of players in the game.
        inputType (str): Type of input used by the players.
        x (int): Custom setting for screen width adjustment.
        y (int): Custom setting for screen height adjustment.
        level (int): Current game level.
        player1List (list): Configuration for player 1.
        player2List (list): Configuration for player 2.
        score (int): Current score of the game.
        txt (str): File path for storing high scores.
        highScore (int): Highest score achieved in the game.

    Methods:
        getHighScore: Retrieves the highest score from the highscore file.
        setHighScore: Updates the highest score if the current score exceeds the high score.
        writeHighScore: Writes the new high score to the file.
    """


    def __init__(self,screenXsize,screenYsize,players,inputType,level : int,p1,p2):
        #initialize parameters
        self._screen_x = 100
        self._screen_y = 100
        self._players = players
        self._result = False
        self._inputType = inputType
        self._x = screenXsize
        self._y = screenYsize
        self._level = level
        self._player1List = p1
        self._player2List = p2
        self._score = 0
        self._txt = "highscore.txt"
        self._highScore = self.getHighScore()

    def getHighScore(self): 
        """
        Retrieves the highest score from a stored file.

        Returns:
            int: The highest score recorded.
        """  
        f = open(self._txt, "r")
        score = f.read()
        f.close()
        if len(score) > 0:
            return int(score)
        else:
            return 0
    def setHighScore(self,score):
        """
        Updates the high score if the given score is higher than the current high score.

        Parameters:
            score (int): The new score to compare against the high score.

        Returns:
            bool: True if the high score was updated, False otherwise.
        """
        self._highScore = score
        self.writeHighScore()
    def writeHighScore(self):
        """
        Writes the high score to a file.

        Parameters:
            score (int): The score to write as the new high score.
        """
        f = open(self._txt,"w")
        f.write(str(self._highScore))
        f.close()

class Game:
    """
    Manages the overall game processes including initializing levels, handling player actions, and controlling game states.

    Methods:
        run(): Starts the main game loop and handles transitions between different screens and states.
        createPlayerPicture(): Prepares visual representations of the player from different angles.
    """
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
        """
        Runs the main game loop, processing player inputs, updating game state, and rendering the game screen.
        """

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

            

        
            if self.settings._result == True and self.settings._level ==3:
                self.settings._level += 1
                self.end_screen.run()
                self.settings._level = 1
            elif self.settings._result == True:
                self.settings._level += 1
                self.end_screen.run()
            elif self.settings._result == False:
                self.settings._level = 1
                self.end_screen.run()
                self.settings._score = 0


            


            #Run End
   

def createPlayerPicture(num,lis,pic):
    """
    Creates and returns images of the player from multiple angles for use in the game.
    """
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
    """
    The main entry point of the application. Initializes the game and starts the game loop.
    """

    

    #Picture list
    picture_list1 = []
    picture_list2 = []
    #create thread for player pictures and start them
    player1TH = threading.Thread(target=createPlayerPicture, args=(0, picture_list1, Picture('Ship1A.png')))
    player2TH = threading.Thread(target=createPlayerPicture, args=(1, picture_list2, Picture('Ship2A.png')))

   
    music.playSong()
    player1TH.start()
    player2TH.start()
    
    #Create new instance of gamesettings
    settings_game = GameSettings(screenXsize=512,screenYsize=512,players=1,inputType=1,level=1,p1=picture_list1,p2=picture_list2)

    #initialize game
    game = Game(settings_game)


    #run game
    game.run(player1TH,player2TH)
    
    
        
    



if __name__ == "__main__":main()
