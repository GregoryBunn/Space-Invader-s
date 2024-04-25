import stddraw

def displayScore(p1, p2 = None):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(-1.8, -1.8, '%.0f' % (int(p1)))
    if p2 != None:
        stddraw.text(1.8, -1.8, '%.0f' % (int(p2)))

#display player lives
#needs to be modified to use imported pictures not drawn circles 
def displayLife(s0, s1):
    stddraw.setPenColor(stddraw.RED)
    stddraw.setPenRadius(0.003)
    lifeR = 0.1
    x1 = -1.8
    x2 = 1.8
    y = -1.5 

      
    if s1 == None:
        life1 = s0.get_htp()

        if (life1==3):
            for i in range(3): stddraw.filledCircle(x1, (y +0.25*i), lifeR) #draw full life picture x3
        elif (life1==2):
            for i in range(2): stddraw.filledCircle(x1, (y +0.25*i), lifeR) #draw full life picture x2
            #draw empty life picture x1
            stddraw.circle(x1, (y+2*0.25), lifeR)
        elif(life1==1):
            stddraw.filledCircle(x1, y, lifeR) #draw full life picture x1
            for i in range(2): stddraw.circle(x1, (y +0.25*(i+1)), lifeR) #draw empty life picture x2
        else: pass
    else: #zoe: displays 2 player ilves, but there's something weird with the one ship (?)
        life1 = s0.get_htp()
        life2 = s1.get_htp()

        if (life1==3):
            for i in range(3): stddraw.filledCircle(x1, (y +0.25*i), lifeR) #draw full life picture x3
        elif (life1==2):
            for i in range(2): stddraw.filledCircle(x1, (y +0.25*i), lifeR) #draw full life picture x2
            #draw empty life picture x1
            stddraw.circle(x1, (y+2*0.25), lifeR)
        elif(life1==1):
            stddraw.filledCircle(x1, y, lifeR) #draw full life picture x1
            for i in range(2): stddraw.circle(x1, (y +0.25*(i+1)), lifeR) #draw empty life picture x2
        else: pass
            
        if (life2==3):
            for i in range(3): stddraw.filledCircle(x2, (y +0.25*i), lifeR) #draw full life picture x3
        elif (life2==2):
            for i in range(2): stddraw.filledCircle(x2, (y +0.25*i), lifeR) #draw full life picture x2
            #draw empty life picture x1
            stddraw.circle(x2, (y+2*0.25), lifeR)
        elif(life2==1):
            stddraw.filledCircle(x2, y, lifeR) #draw full life picture x1
            for i in range(2): stddraw.circle(x2, (y +0.25*(i+1)), lifeR) #draw empty life picture x2
        else: pass
    