from math import sin, cos, pi
from picture import Picture
from stddraw import picture, filledCircle, setPenColor, RED
pic = Picture('Ship1.png')
pics = [None]*74

class Ship:
    '''
    Pos - the position in the pics list that we are displaying
    angle - the angle of the ship that the bullet takes on when being fired
    '''
    def __init__(self, x, y, angle, fireRate, pos, hitBox, hpt, score):
        self._x = x
        self._y = y
        self._angle = angle
        self._fireRate = fireRate
        self._pos = pos
        self._hitBox = hitBox
        self._htp = hpt
        self._score = score
    #The create function makes all the different png's needed for the ship and stores it in a list. 
    #So when we rotate it just gets a photo that has already been rotated when we first started the program and that's
    #why it takes a few second to start the program because it does all this calculation before we start instead of during the game
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
            stAngle += pi/72
            count += 1
            
    #two functions so that we can thread them - you can see the threading in the 'game.py' file
    #this just makes the start up time double the speed it would be if we didnt thread them
    def create1():
        count = 37
        stAngle = 0
        while stAngle < pi/2:
            pic1 = Picture('invis.png')
            for j in range(pic.height()):
                    for i in range(pic.width()):
                        col = pic.get(i, j)
                        t = (i-64)*cos(stAngle)-(j-64)*sin(stAngle) + 64
                        l = (i-64)*sin(stAngle)+(j-64)*cos(stAngle) + 64
                        pic1._surface.set_at((int(t), int(l)), (col.getRed(), col.getBlue(), col.getGreen(), 255))
            pics[count] = pic1
            stAngle += pi/72
            count +=1
    
    def move(self, direction):
        self._x += direction*0.02
        picture(pics[self._pos], self._x, self._y)

    def rotate(self, rotation = 0):
        '''
        rotation determines if we are rotating clockwise or anticlockwise
        just calling the rotate method with no input will just display the ship at the current angle it is at
        '''
        if rotation == -1 and self._pos != 0:
            self._pos -= 1
            self._angle += pi/72
        elif rotation == 1 and self._pos !=len(pics)-1:
            self._pos += 1
            self._angle -= pi/72
        else:
            pass
        picture(pics[self._pos], self._x, self._y)
        if self._pos == 74:
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
    def getScore(self):
        return self._score
    def inscreaseScore(self):
        self._score += 1
    def resetScore(self):
        self._score = 0
    def get_htp(self):
        return self._htp
    def set_htp(self, val):
        self._htp = val
    def get_hitBox(self):
        return self._hitBox
    #Each ship gets there own fire rate that can be changed aswell as we collect power ups
    def getFireRate(self):
        return self._fireRate
    def setFireRate(self, fireRate):
        self._fireRate = fireRate

'''
This class handles the bullets and their movements
'''
class Bullet:
    def __init__(self, x, y, angle, owner, state):
        self._x = x
        self._y = y
        self._angle = angle
        self._state = state
        self._owner = owner

    def move(self):
        self._y += 0.06*sin(self._angle)
        self._x += 0.06*cos(self._angle)
        setPenColor(RED)
        filledCircle(self._x, self._y, 0.05)
    '''
    on initialization, _ makes a variable private so it can't be accessed outside of this file (self._x = x).
    so you have to make a method that will return the values that the obejct stores or sets the variables that the object stores.
    making variables private is good practice and our lecturer said that we must do it and will be marked down if we don't.
    '''
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getState(self):
        return self._state
    def setState(self, state):
        self._state = state
    def getOwner(self):
        return self._owner