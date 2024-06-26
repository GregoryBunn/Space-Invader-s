from stddraw import picture
from picture import Picture
import stddraw
pic = Picture('Aliens.png')
boss = Picture('Boss0.png')
class Enemy:
    def __init__(self, x, y, hitBox, htp, state):
        self._x = x
        self._y = y
        self._state = state
        self._htp = htp
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
    def get_hitBox(self):
        return self._hitBox
    def setState(self, state):
        self._state = state

class Boss:
    def __init__(self, x, y, htp, hitBox, state):
        self._x = x
        self._y = y
        self._htp = htp
        self._hitBox = hitBox
        self._state = state

    def move(self, dir, spd, scale):
        self._x += spd*dir
        picture(boss, self._x, self._y)
        if self._x <= -scale+self._hitBox+0.2:
            return 1
        elif self._x >= scale-(self._hitBox+0.2):
            return 1
    
    def moveDown(self):
        self._y -= 0.4
        picture(boss, self._x, self._y)
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_hitBox(self):
        return self._hitBox
    def get_state(self):
        return self._state
    def set_state(self, state):
        self._state = state
    def get_htps(self):
        return self._htp
    def hit(self):
        self._htp -= 1
    #display boss health bar    
    def show_life(self):
        stddraw.setPenColor(stddraw.RED)
        px = self._htp/7 
        stddraw.line(-1.8, 1.8, px, 1.8)
    
class enBullet:
    def __init__(self, x, y, state):
        self._x = x
        self._y = y
        self._state = state
    def move(self):
        self._y -= 0.01
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.setPenRadius(0.01)
        stddraw.line(self._x, self._y, self._x, (self._y-0.1))
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def set_state(self, state):
        self._state = state
    def get_state(self):
        return self._state