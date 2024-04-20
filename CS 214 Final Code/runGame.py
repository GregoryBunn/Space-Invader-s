import screens, stddraw

def main():
    stddraw.setXscale(-2, 2)
    stddraw.setYscale(-2, 2)
    while True:
        screens.startScreen()
        stddraw.show(1000)

if __name__=='__main__': main()