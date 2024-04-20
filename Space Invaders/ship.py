import stddraw, math, threading
from math import pi, sin, cos
from picture import Picture
r = 0.1
pics = [None]*38
pic = Picture('Ship1.png')
class Ship:
    def __init__(self, pos, x, y, angle):
        self._x = x
        self._y = y
        self._pos = pos
        self._angle = angle
    def create():
        count = 0
        stAngle = -pi/2
        while stAngle < 0:
            pic1 = Picture('invis.png')
            for j in range(pic.height()):
                    for i in range(pic.width()):
                        col = pic.get(i, j)
                        t = (i-64)*cos(stAngle)-(j-64)*sin(stAngle) + 64
                        l = (i-64)*sin(stAngle)+(j-64)*cos(stAngle) + 64
                        pic1._surface.set_at((int(t), int(l)), (col.getRed(), col.getBlue(), col.getGreen(), 255))
            pics[count] = pic1
            stAngle += pi/36
            count += 1
        print(stAngle)
    def create1():
        count = 19
        stAngle = 0
        while stAngle < pi/2:
            pic1 = Picture('invis.png')
            for j in range(pic.height()):
                    for i in range(pic.width()):
                        col = pic.get(i, j)
                        t = (i-64)*cos(stAngle)-(j-64)*sin(stAngle) + 64
                        l = (i-64)*sin(stAngle)+(j-64)*cos(stAngle) + 64
                        pic1.set(int(t), int(l), col)
            pics[count] = pic1
            stAngle +=pi/36
            count +=1 
    
    def move(self, direction):
        self._x += direction*0.02
        stddraw.picture(pics[self._pos], self._x, self._y)

    def rotate(self, rotation = 0):
        if rotation == -1 and self._pos != 0:
            self._pos -= 1
            self._angle += pi/36
        elif rotation == 1 and self._pos !=37:
            self._pos += 1
            self._angle -= pi/36
        else:
            pass
        stddraw.picture(pics[self._pos], self._x, self._y)
        if self._pos == 37:
            self._angle = 0
        elif self._pos == 0:
            self._angle = pi

    def getX(self):
        return self._x
    def setX(self, val):
        self._x = val
    def getAngle(self):
        return self._angle
    def setAngle(self, angle):
        self._angle = angle
    def getPos(self):
        return self._pos
    def setPos(self, pos):
        self._pos = pos
    def getY(self):
        return self._y
    

class Bullet:
    def __init__(self, x, y, angle, state):
        self._x = x
        self._y = y
        self._angle = angle
        self._state = state

    def move(self):
        self._y += 0.06*sin(self._angle)
        self._x += 0.06*cos(self._angle)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.filledCircle(self._x, self._y, 0.05)

    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getState(self):
        return self._state
    def setState(self, state):
        self._state = state
