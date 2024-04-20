import stddraw, random
class Star:
    def __init__(self, x, y, spd):
        self.x = x
        self.y = y
        self.spd = spd
    def move(n):
        n.y -= 0.004*n.spd
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.filledCircle(n.x, n.y, 0.008)

def main():
    stddraw.setXscale(-2, 2)
    stddraw.setYscale(-2, 2)
    stars = []
    for i in range(40):
        sign = random.randint(1, 2)
        sign2 = random.randint(1, 2)
        if sign2 == 2:
            sign2 = -1
        if sign == 2:
            sign = -1
        xPos = random.random()*2*sign
        yPos = random.random()*2*sign2
        speed = random.random()
        while speed < 0.2 or speed > 0.4:
            speed = random.random()
        name = i
        name = Star(xPos, yPos, speed)
        stars.append(name)
    while True:
        stddraw.clear(stddraw.BLACK)
        for i in range(len(stars)):
            if stars[i].y <= -2:
                sign = random.randint(1, 2)
                if sign == 2:
                    sign = -1
                stars[i].x = random.random()*sign*2
                stars[i].y = random.random()+2
            else:
                Star.move(stars[i])
        stddraw.show(1)

if __name__ =='__main__': main()
