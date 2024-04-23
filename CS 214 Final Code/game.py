import gameModes, stddraw, threading, screens, enemies
from ship import Ship

def main():
    scale = 2
    outcome = 0
    wl = None
    htp = 2
    spd = 0
    score = 0
     
    #game setup?
    stddraw.setXscale(-scale, scale)
    stddraw.setYscale(-scale, scale)
    stddraw.setFontFamily('OCR A Extended')
    a = threading.Thread(target=Ship.create)
    b = threading.Thread(target=Ship.create1)
    a.start()
    b.start()
    a.join()
    b.join()

    #starting screen(s) displayed
    screens.playerSelect()
    keys = stddraw.getKeysPressed()
    if keys[stddraw.K_2]:
        players = 2
    elif keys[stddraw.K_1]:
        players = 1
    while not stddraw.hasNextKeyTyped():
        screens.startScreen()

    while True:
        if wl == 0:
            spd = 0
            wl = None
            score = 0
            htp = 2
        if outcome < 3:
                temp, score, htp = gameModes.mainGame(scale, players, outcome, spd, score, htp)
                if temp == 1:
                    spd += 0.01
                    outcome += 1
                elif temp == 0:
                    htp = 2
                    outcome = 0
                    spd = 0
                    score = 0
        else:
            wl = gameModes.boss(scale, 15)
            outcome = 0


if __name__=='__main__': main()