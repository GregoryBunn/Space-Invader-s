#title screen for project
import stddraw, objects, game
def title():
    stddraw.setFontSize(40)
    s = "SHOOTER GAME"
    stddraw.text(0, 5, s)

def instructions():
    stddraw.setFontSize(28)
    i = "Instuctions:"
    m = "[A] move left, [S] stop move, [D] move right"
    r = "[Q] rotate left, [W] stop rotate, [E] rotate right"
    s = "[Space] to shoot"
    h = "[H] for help"
    q = "[X] to end game"
    start = "Press [Space] to start"
    leave = "Press [q] to exit"
    stddraw.text(0, 2.5, i)
    stddraw.setFontSize(22)
    stddraw.text(0, 1, m)
    stddraw.text(0, 0, r)
    stddraw.text(0, -1, s)
    stddraw.text(0, -2, h)
    stddraw.text(0, -3, q)
    stddraw.setFontSize(34)
    stddraw.text(0, -6, start)
    stddraw.setFontSize(18)
    stddraw.text(0, -8, leave)

def highscore(player):
    #read highscore then compare with player
    f = open("highscore.txt", "r")
    h_score = int(f.read())
    f.close()
    if h_score<player.score: 
        #update highscore
        h_score = player.score 
        update = True
        #overwrite into txt file
        f = open("highscore.txt", "w")
        f.write(str(h_score))
        f.close()
    else: update = False

    return h_score, update


def gameover(wind,P):
    game.clear()
    s = "GAME OVER..."
    t = "game will restart soon..."
    if(wind.win):
        u = "You Win!"
    else: u = "You Lose!"
    stddraw.setFontSize(48)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(0, 5, u)
    stddraw.setFontSize(14)
    stddraw.text(0, -5, t)
    stddraw.setFontSize(28)
    stddraw.text(0, -1, "Score: "+str(P.score))

    #highscore
    High, newHigh = highscore(P)
    if newHigh: 
        stddraw.text(0, -2, "New Highscore!")
    else: stddraw.text(0, -2, "Highscore: "+str(High))

    game.reload()

def startSetup(wind):
    #screen setup    
    game.clear()
    stddraw.setXscale(-wind.x, wind.x)
    stddraw.setYscale(-wind.y, wind.y)
    stddraw.setPenColor(stddraw.WHITE)
    title()
    instructions()
    #screen loop
    active = True
    while active:
        #key to move on: [Space]
        if (stddraw.hasNextKeyTyped()):
            check = stddraw.nextKeyTyped() 
            if(check == " "):
                active = False
                #move to game screen
                game.clear()
            elif(check=="q"): 
                quit()
            else: pass
        stddraw.show(50)



def main():
    stddraw.clear(stddraw.GRAY)
    stddraw.setXscale(-10, 10)
    stddraw.setYscale(-10, 10)
    stddraw.setPenColor(stddraw.WHITE)
    title()
    instructions()
    stddraw.show(5000)  #wait 5 secs
    stddraw.clear(stddraw.GRAY)
    gameover()
    stddraw.show(3000)
    #main()

if __name__=='__main__':main()
