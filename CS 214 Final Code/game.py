import gameModes, stddraw, threading, screens, enemies
from ship import Ship

def main():
    scale = 2
    outcome = 0
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
        if outcome < 3:
            outcome += gameModes.mainGame(scale, players)
        else:
            gameModes.boss(scale, 15)
            outcome = 0


if __name__=='__main__': main()