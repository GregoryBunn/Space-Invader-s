import screens, stddraw

def main():
    stddraw.setXscale(-2, 2)
    stddraw.setYscale(-2, 2)
    while not stddraw.hasNextKeyTyped():
        screens.startScreen()

if __name__=='__main__': main()