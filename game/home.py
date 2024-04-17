import stddraw
import sys
#from gamerun import GameLoop


class HomeScreen:

    def __init__(self,settings):
        #class initialized with settings
        self.settings = settings

    #Create homescreen
    def displayHome(self):
        #get screen size
        x = self.settings.screen_x
        y = self.settings.screen_y
        stddraw.clear(stddraw.GRAY) #Create gray form
        #set scale
        stddraw.setXscale(-x,x)
        stddraw.setYscale(-y,y)
        stddraw.setFontFamily('Arial') #set font
        stddraw.setFontSize(40) #set font size
        stddraw.setPenColor(stddraw.WHITE) #set font color

        #add needed text
        stddraw.text(0,int(y/10)*8,"COSMIC CONQUISTADORS")
        stddraw.setFontSize(30)
        stddraw.text(0,int(y/10)*5,"Instructions:")
        stddraw.setFontSize(22)
        stddraw.text(0,int(y/10)*3,"[A] move left, [S] stop move, [D] move right")
        stddraw.text(0,int(y/10)*1.5,"[Q] rotate left,[W] stop rotate,[E] rotate right")
        stddraw.text(0,int(y/10)*0,"[Space] to shoot")
        stddraw.text(0,int(y/10)*-1.5,"[H] for help")
        stddraw.text(0,int(y/10)*-3,"[X] to quit")
        stddraw.setFontSize(30)
        stddraw.text(0,int(y/10)*-6,"Press any key to start")

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




