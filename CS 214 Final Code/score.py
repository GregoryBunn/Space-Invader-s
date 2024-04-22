import stddraw

def displayScore(p1, p2 = None):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(-1.8, -1.8, '%.0f' % (int(p1)))
    if p2 != None:
        stddraw.text(1.8, -1.8, '%.0f' % (int(p2)))