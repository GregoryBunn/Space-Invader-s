import gameModes, stddraw

def main():
    scale = 2
    stddraw.setXscale(-scale, scale)
    stddraw.setYscale(-scale, scale)
    while True:
        gameModes.mainGame(scale)

if __name__=='__main__': main()