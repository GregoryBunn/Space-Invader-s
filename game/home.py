import stddraw
import sys
#from gamerun import GameLoop


class PlayerSelect:
    def __init__(self,settings):
        self.settings = settings
    def displayPlayerSelect(self):
        #get screen size
        x = self.settings.screen_x
        y = self.settings.screen_y
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
                    self.settings.players = 1
                elif key == "2":
                    #exit loop
                    start = True
                    #set player count
                    self.settings.players = 2

                #show screen if nothing is pressed
            stddraw.show(50)

        


class HomeScreen:

    def __init__(self,settings):
        #class initialized with settings
        self.settings = settings

    #Create homescreen
    def displayHome(self):
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
        stddraw.text(0, -30, "[H] for help")
        stddraw.text(0, -45, "[X] to quit")
        stddraw.setFontSize(35)
        stddraw.text(0, -70, "Press any key to start")

    #run the home screen
    def run(self):
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
                if stddraw.nextKeyTyped() == "q":
                    #quit
                    sys.exit()

                #show screen if nothing is pressed
            stddraw.show(50)


#end screen class
class EndScreen:
    def __init__(self,settings):
        #class initialized with settings
        self.settings = settings
    
    #create screen
    def display(self):
        stddraw.clear(stddraw.GRAY) #Create gray form
        stddraw.setFontFamily('Arial') #set font
        stddraw.setFontSize(40) #set font size
        stddraw.setPenColor(stddraw.WHITE) #set font color


        #check if player won or lose
        if self.settings.result:
            stddraw.text(0,0,"You win")
            
        else:
            stddraw.text(0,0,"Better luck next time")

    #run Endscreen
    def run(self):

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
                    sys.exit()

                #show screen if nothing is pressed

            time = time + timer #increase time passed
            stddraw.show(timer) #show screen




