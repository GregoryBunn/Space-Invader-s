import stddraw

def startScreen():
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(40)
    stddraw.text(0, 1.8, "COSMIC CONQUISTADORS")
    stddraw.setFontSize(35)
    stddraw.text(0, 0.8, "Instructions:")
    stddraw.setFontSize(20)
    stddraw.text(0, 0.3, "[A] move left, [D] move right")
    stddraw.text(0, 0, "[Q] rotate left, [E] rotate right")
    stddraw.text(0, -0.3, "[Space] to shoot")
    stddraw.text(0, -0.6, "[H] for help")
    stddraw.text(0, -0.9, "[X] to quit")
    stddraw.setFontSize(35)
    stddraw.text(0, -1.4, "Press any key to start")
    stddraw.show(0)

def loseScreen():
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(45)
    stddraw.text(0, 1.4, "You Lose :(")
    stddraw.setFontSize(35)
    stddraw.text(0, -1.4, "Press any key to restart")
    stddraw.show(0)

def winScreen():
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(45)
    stddraw.text(0, 1.4, "You WIN!")
    stddraw.setFontSize(18)
    stddraw.text(0, -1.4, "Press any key to go to the next level!")
    stddraw.show(0)

def playerSelect():
    #screen display
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(40)
    stddraw.text(0, 1.8, "COSMIC CONQUISTADORS")
    stddraw.setFontSize(20)
    stddraw.text(0, 0.8, "Press key to select Game Type:")
    stddraw.setFontSize(20)
    stddraw.text(0, 0.3, "[1] for 1 Player")
    stddraw.text(0, 0, "[2] for 2 Players")
    stddraw.setFontSize(16)
    stddraw.text(0, -1.4, "Press [Q] to close window")

    #screen while loop
    display = True
    while display:
        #check key input
        if stddraw.hasNextKeyTyped():
            check = stddraw.nextKeyTyped()
            if (check=="1") or (check=="2"): #set game player mode
                display = False #exit loop
            elif (check=="q"): #exit program
                quit()
            else: pass

        #show screen if nothing is pressed
        stddraw.show(0)