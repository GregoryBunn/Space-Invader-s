import gameModes, stddraw, threading, screens
from ship import Ship
from math import pi

def main():
    scale = 2
    wave = 0
    numEn = 0
    wl = None
    htp = 3
    spd = 0
    lvl = 1
     
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
        screens.startScreen(players)
    
    #If you choose 1 player then the s1 - the second player - is none
    #If you chose 2 player then s1 is made an object and will therefore not be 'None' so all the if statements will work for the second player
    if players == 2:
        s1 = Ship(0.4, -1.8, pi/2, 0, 37, 0.1, htp, 0)
        s0 = Ship(-0.4, -1.8, pi/2, 0, 37, 0.1, htp, 0)
    elif players == 1:
        s0 = Ship(0, -1.8, pi/2, 0, 37, 0.1, htp, 0)
        s1 = None

    while True:
        if wl == 0:
            numEn = 0
            spd = 0
            s0.set_htp(2)
            s0.reset_Score()
            if s1 != None:
                s1.set_htp(2)
                s1.reset_Score()
        elif wl == 'exit': return
            
        if wave < 3:
                
                #if you win a game, the game returns 1. so if outcome is 1 it will change everything acordingly 
                #the same if you lose, outcome will be 0 and this will handle everything accordingly
                #If you click 'x' then you quite the game and outcome will be 'exit' which will just return and then take you out of the game
                outcome = gameModes.mainGame(scale, numEn, spd, s0, s1, lvl)
                print(outcome)
                if outcome == 1:
                    spd += 0.01
                    numEn += 1
                    wave += 1
                    lvl += 1
                elif outcome == 0:
                    s0.set_htp(2)
                    s0.reset_Score()
                    if s1 != None:
                        s1.set_htp(2)
                        s1.reset_Score()
                    numEn = 0
                    spd = 0
                    wave = 0
                elif outcome == 'exit': return
        else:
            #wl is the outcome for the boss level. if its 1, you win
            #if it's 0 then you lose and the game resets
            wl = gameModes.boss(scale, 13, s0, s1, lvl)
            wave = 0


if __name__=='__main__': main()