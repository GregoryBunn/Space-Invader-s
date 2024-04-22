import stddraw

def startScreen():
    stddraw.clear(stddraw.GRAY)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(40)
    stddraw.text(0, 1.8, "COMSIC CONQUISTADORS")
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
    stddraw.clear(stddraw.GRAY)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(45)
    stddraw.text(0, 1.4, "You Lose :(")
    stddraw.setFontSize(35)
    stddraw.text(0, -1.4, "Press any key to restart")
    stddraw.show(0)

def winScreen():
    stddraw.clear(stddraw.GRAY)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(45)
    stddraw.text(0, 1.4, "You WIN!")
    stddraw.setFontSize(18)
    stddraw.text(0, -1.4, "Press any key to go to the next level!")
    stddraw.show(0)