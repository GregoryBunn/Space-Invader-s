import stddraw, time, picture

pic = picture.Picture('Aliens.png')

class Alien:
    def __init__(self, x, y, r, state):
        self._x = x
        self._y = y
        self._r = r
        self._state = state

    def stay(self):
        stddraw.picture(pic, self._x, self._y)
    def move(self, d, spd):
        self._x += d*spd
        stddraw.picture(pic, self._x, self._y)
    def down(self):
        self._y -= self._r
        stddraw.picture(pic, self._x, self._y)
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def setX(self, val):
        self._x = val
    def getState(self):
        return self._state
    def setY(self, val):
        self._y = val
    def setState(self, state):
        self._state = state
