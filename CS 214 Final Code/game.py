import gameModes, stddraw, threading, screens, enemies
from ship import Ship

def main():
    scale = 2
    outcome = 0
    wl = None
    htp = 2
    spd = 0
    score = 0
    stddraw.setXscale(-scale, scale)
    stddraw.setYscale(-scale, scale)
    a = threading.Thread(target=Ship.create)
    b = threading.Thread(target=Ship.create1)
    a.start()
    b.start()
    a.join()
    b.join()
    while not stddraw.hasNextKeyTyped():
        screens.startScreen()
    keys = stddraw.getKeysPressed()
    if keys[stddraw.K_2]:
        players = 2
    else:
        players = 1
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
            wl = gameModes.boss(scale, 2)
            outcome = 0


if __name__=='__main__': main()