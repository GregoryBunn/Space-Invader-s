from stddraw import picture
from picture import Picture
pic = Picture('Aliens.png')
class Enemy:
    def __init__(self, x, y, hitBox, state):
        self._x = x
        self._y = y
        self._state = state
        self._hitBox = hitBox
    
    def move(self, dir, spd, scale):
        self._x += spd*dir
        picture(pic, self._x, self._y)
        if self._x <= -scale+self._hitBox:
            return 1
        elif self._x >= scale-self._hitBox:
            return 1
    def moveDown(self):
        self._y -=0.1
        picture(pic, self._x, self._y)

    def getState(self):
        return self._state
    def getY(self):
        return self._y
    def getX(self):
        return self._x
    def setState(self, state):
        self._state = state