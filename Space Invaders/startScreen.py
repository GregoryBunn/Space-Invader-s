import stddraw, ship, threading

def startScreen():                              #Start screen setup
    stddraw.clear(stddraw.GRAY)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(45)
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
    a = threading.Thread(target=ship.Ship.create)
    b = threading.Thread(target=ship.Ship.create1)
    a.start()
    b.start()
    a.join()
    b.join()

    while stddraw.hasNextKeyTyped():
        stddraw.nextKeyTyped()
    print(stddraw.hasNextKeyTyped())
    while not stddraw.hasNextKeyTyped():    #wait for a keyboard to change to the game screen
        stddraw.show(0)