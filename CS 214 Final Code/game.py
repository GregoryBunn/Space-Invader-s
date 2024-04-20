import gameModes, stddraw, threading
from ship import Ship

def main():
    scale = 2
    stddraw.setXscale(-scale, scale)
    stddraw.setYscale(-scale, scale)
    a = threading.Thread(target=Ship.create)
    b = threading.Thread(target=Ship.create1)
    a.start()
    b.start()
    a.join()
    b.join()
    while True:
        gameModes.mainGame(scale)
if __name__=='__main__': main()