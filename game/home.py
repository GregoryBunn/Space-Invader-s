import stddraw
import sys

"""
File that handles the diffrent static screens
classes include:
PlayerSelect
Homescreen
Endscreen

"""

#Code for the formatting was done by Greg and Zoe


class PlayerSelect:
    """
    Handles the player selection process on the first title screen of the game, 
    where the number of players are chosen.

    Attributes:
        settings (object): object that stores game settings.

    Methods:
        displayPlayerSelect(): Draws the graphical screen for playerselect.
        run(): Runs the screen and checks for any input.
    """
    def __init__(self,settings):
        """
        Initializes the PlayerSelect with the given settings.

        Args:
            settings: game settings.
        """
        self._settings = settings
    def displayPlayerSelect(self):

        """
        Create and draw the player select screen
        """
        #get screen size
        x = self._settings._screen_x
        y = self._settings._screen_y
        #set scale
        stddraw.setXscale(-x,x)
        stddraw.setYscale(-y,y)

        #set font
        stddraw.setFontFamily('OCR A Extended')

        #screen display
        stddraw.clear(stddraw.BLACK)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setFontSize(40)
        stddraw.text(0, 90, "COSMIC CONQUISTADORS")
        stddraw.setFontSize(20)
        stddraw.text(0, 40, "Press key to select Game Type:")
        stddraw.setFontSize(20)
        stddraw.text(0, 15, "[1] for 1 Player")
        stddraw.text(0, 0, "[2] for 2 Players")
        stddraw.setFontSize(16)
        stddraw.text(0, -70, "Press [Q] to close window")
        
    #run the select screen
    def run(self):
        """
        run the player select screen and check for any input
        """
        #create the select screen
        self.displayPlayerSelect()
        

        #Variable to activate game(exit home screen)
        start = False

        #Loop for homem screen
        while start == False:

            #check for a key input
            
            if stddraw.hasNextKeyTyped():

                #get key
                key = stddraw.nextKeyTyped()

                #enter play screen
                if key == "q":
                    #quit
                    sys.exit()

                elif key == "1":
                    #exit loop
                    start = True
                    #set players count
                    self._settings.players = 1
                elif key == "2":
                    #exit loop
                    start = True
                    #set player count
                    self._settings.players = 2

                #show screen if nothing is pressed
            stddraw.show(50)

        


class HomeScreen:
    """
    The main menu screen of the game

    Attributes:
        settings (object): object that stores game settings.

    Methods:
        display(): Renders the main menu screen.
        run(): Calls display and Manages the input logic for menu selection.
    """

    def __init__(self,settings):
        """
        Initializes the Homescreen with the given settings.

        Args:
            settings (object): game settings.
        """
        self._settings = settings

    #Create homescreen
    def displayHome(self):

        """
        Create the graphics depending on number of players and draws them
        """
        if self._settings.players==1:
            stddraw.clear(stddraw.BLACK)
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.setFontSize(40)
            stddraw.text(0, 90, "COSMIC CONQUISTADORS")
            stddraw.setFontSize(35)
            stddraw.text(0, 40, "Instructions:")
            stddraw.setFontSize(20)
            stddraw.text(0, 15, "[A] move left, [D] move right")
            stddraw.text(0, 0, "[Q] rotate left, [E] rotate right")
            stddraw.text(0, -15, "[Space] to shoot")
            stddraw.text(0, -30, "[X] to quit")
            stddraw.setFontSize(35)
            stddraw.text(0, -70, "Press any key to start")
        else:
            stddraw.clear(stddraw.BLACK)
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.setFontSize(40)
            stddraw.text(0, 90, "COSMIC CONQUISTADORS")
            stddraw.setFontSize(35)
            stddraw.text(0, 65, "Instructions:")
            stddraw.setFontSize(20)
            stddraw.text(0, 45, "Player1:")
            stddraw.setFontSize(18)
            stddraw.text(0, 35, "[A] move left, [D] move right")
            stddraw.text(0, 25, "[Q] rotate left, [E] rotate right")
            stddraw.text(0, 15, "[Space] to shoot")
            stddraw.setFontSize(20)
            stddraw.text(0, -10, "Player2:")
            stddraw.setFontSize(18)
            stddraw.text(0, -20, "[J] move left, [L] move right")
            stddraw.text(0, -30, "[U] rotate left, [O] rotate right")
            stddraw.text(0, -40, "[N] to shoot")
            stddraw.setFontSize(35)
            stddraw.text(0, -70, "Press any key to start")
            stddraw.setFontSize(16)
            stddraw.text(0, -90, "Press [X] to exit")

    #run the home screen
    def run(self):

        """
        Call the display function 
        Handels the input logic
        """

        #create the home screen
        self.displayHome()
        

        #Variable to activate game(exit home screen)
        start = False

        #Loop for homem screen
        while start == False:

            #check for a key input
            if stddraw.hasNextKeyTyped():

                #exit loop
                start = True

                #enter play screen
                if stddraw.nextKeyTyped() == "x":
                    #quit
                    sys.exit()

                #show screen if nothing is pressed
            stddraw.show(50)


#end screen class
class EndScreen:
    """
    Displays the end game screen based on the result of the game..

    Attributes:
        settings (object): game settings.

    Methods:
        display(): Creates the end game screen.
        run(): Manages the end game input, determining if the game should restart or close.
    """
    def __init__(self,settings):
        """
        Initializes the Endscreen with the given settings.

        Args:
            _settings (object): game settings.
        """
        self._settings = settings
    
    #create screen
    def display(self):
        """
        Create and display the endscreen
        """
        stddraw.clear(stddraw.BLACK) #Create Black form        
        stddraw.setPenColor(stddraw.WHITE) #set font color

        Finallevel = 6
        if self._settings._level == Finallevel:
            #Show the screen for when the game has been won
            stddraw.setFontSize(40) #set font size
            stddraw.text(0,30,"You Win!!!")
            stddraw.setFontSize(20)
            stddraw.text(0,0,"Total Score: " + str(self._settings._score))
            
            if self._settings._score > self._settings._highScore:
                stddraw.setFontSize(25)
                stddraw.text(0,-40,"You set the high score!!" )
                self._settings.setHighScore(self._settings._score)
            else:

                stddraw.setFontSize(20)
                stddraw.text(0,-35,"HighScore: " + str(self._settings._highScore))
            #set new high score
            stddraw.setFontSize(15)
            stddraw.text(0,-50,"Game will restart shortly")
            stddraw.text(0,-60,"Press [x] to exit game")
        else:
            #check if player won or lose
            if self._settings._result:
                #Progress to next level
                stddraw.setFontSize(40) #set font size
                stddraw.text(0,0,"Next Level")
                stddraw.setFontSize(15) #set font size
                stddraw.text(0,-50,"Next level starting soon...")
                stddraw.text(0,-60,"Press [x] to exit game")
                
            else:
                #restart game
                stddraw.setFontSize(35)
                stddraw.text(0,0,"Better luck next time")
                stddraw.setFontSize(25)
                stddraw.text(0,-20,"Total Score: " + str(self._settings._score))
                
               

                stddraw.setFontSize(15) #set font size
                stddraw.text(0,-30,"HighScore: " + str(self._settings._highScore))
                if self._settings._score > self._settings._highScore:
                    #set new highscore
                    stddraw.text(0,-35,"You set the high score!!" )
                    self._settings.setHighScore(self._settings._score)
                stddraw.text(0,-50,"New game starting soon...")
                stddraw.text(0,-60,"Press [x] to exit game")

    #run Endscreen
    def run(self):
        """
        run the endscreen by calling display and handle any input
        """
        #clear key list if there is one
        while stddraw.hasNextKeyTyped():
            stddraw.nextKeyTyped()

        #create screen
        self.display()
        #Variable to exit end screen
        start = False
        timer = 50
        time = 0
        #Loop for end screen
        while start == False:
            #check if enough time has passed after end
            if time == timer*100:
                time = 0
                return True#start new game

            #check for a key input
            if stddraw.hasNextKeyTyped():
                #exit loop
                start = True

                #play again
                if stddraw.nextKeyTyped() != "x":
                    return True #(game run is called again)

                    
                    
                #quit game if x is pressed
                else:
                    return False

                #show screen if nothing is pressed

            time = time + timer #increase time passed
            stddraw.show(timer) #show screen


