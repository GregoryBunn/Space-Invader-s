import stddraw
import math




class Missile:
    #class done by Wikus
    """
    Represents a missile object in a game with properties for managing its state and behavior.

    Attributes:
        _x (float): The x-coordinate of the missile on the game screen.
        _y (float): The y-coordinate of the missile on the game screen.
        _dir (float): The direction of the missile's travel.
        _typ (int): The type of missile, which affects its appearance and possibly behavior.
        _owner (int): The identifier of the missile's owner, which could differentiate between player and enemy missiles.
        _speed (int): The speed at which the missile moves.
        _size (int): The size of the missile, affecting its appearance and collision area.

    Methods:
        drawMissile(): Draws the missile on the game screen using different colors and shapes based on the missile type.
    """
    def __init__(self,x:float,y:float,dir:float,typ:int,owner:int,size:int):
        """
        Initializes a new instance of the Missile class with specified attributes.

        Parameters:
            _x (float): The x-coordinate of the missile on the game screen.
            _y (float): The y-coordinate of the missile on the game screen.
            _dir (float): The direction of the missile's travel.
            _typ (int): The type of the missile.
            _owner (int): The identifier of the missile's owner.
            _size (int): The size of the missile.
        """
        self._x = x #missile x
        self._y = y #missile y
        self._dir = dir #missile direction
        self._typ = typ #type of missile
        self._owner = owner #missile owner
        self._speed = 4 #missile speed
        self._size = size

    #draw Missile Done by all parties Combined for version below
    def drawMissile(self):
        """
        Draws the missile on the game screen, with different characteristics based on the missile type.
        Type 0 missiles are drawn green, type 1 are red, and type 2 are blue.
        """

        if self._typ == 2:
            #set pen color
            stddraw.setPenColor(stddraw.BLUE)

            #draw missile
            stddraw.filledCircle(self._x,self._y,self._size)


        #creates missile of type 1S
        if self._typ == 1:
            #set pen color
            stddraw.setPenColor(stddraw.RED)

            #draw missile
            stddraw.filledCircle(self._x,self._y,self._size)
        #create missile of type 0
        if self._typ == 0:
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.setPenRadius(0.5)
            stddraw.line(self._x, self._y, self._x, (self._y-5))


    #move Missile Done by all parties Combined for version below
    def moveMissile(self):
        """
        Updates the missile's position based on its direction and speed, moving it across the game screen.
        """

        #move missile if missile is a counter attack missile
        if self._typ == 0:
            speed = 0.5
            self._y= self._y - speed*(self._speed*(1-abs(self._dir/(math.pi/2))))
        
        #move player missiles
        else:
            #change x pos
            self._x = self._x + (self._speed*(self._dir/(math.pi/2)))
            #change y pos
            self._y = self._y + (self._speed*(1-abs(self._dir/(math.pi/2))))



    def checkMissileBounds(self):
        """
        Checks whether the missile is still within the game screen boundaries.

        Returns:
            bool: True if the missile is within bounds, False otherwise.
        """
        screenX = 100
        screenY = 100

        #Check if missile x is in the screen bounds
        if self._x > screenX-6 or self._x < -screenX+6:
            #super missile bounce of wall
            if self._typ == 2 and abs(self._dir)< math.pi/2.1:
                #Change direction of missile
                self._dir = -self._dir
                return True
            else:

                #remove missile
                return False
        
        #Check if missile y is in the screen bounds
        elif self._y > screenY-8 or self._y < -screenY+8:
            #remove missile
            return False
        
        #allow missile
        else:
            return True
        
# Missile list Done by all parties Combined for version below
# class done by wikus
class MissileList:
    """
    Manages a collection of missiles in the game, handling operations such as adding, removing, and updating missiles.

    Attributes:
        _missiles (list of Missile): The list of missile objects currently active in the game.
    """
    def __init__(self):
        self._missiles = []
    def add_missile(self,missile:Missile):
        """
        Adds a new missile to the list of active missiles.

        Parameters:
            missile (Missile): The missile to be added to the list.
        """
        self._missiles.append(missile)
    def remove_missile(self,missile:Missile):
        """
        Removes a missile from the list of active missiles.

        Parameters:
            missile (Missile): The missile to be removed from the list.
        """
        if missile in self._missiles:
            self._missiles.remove(missile)
    def move_drawMissiles(self):
        """
        Updates the positions of all missiles in the list and draws them on the screen.
        This method also checks for missiles that are out of bounds and removes them.
        """
        for missile in self._missiles[:]:
            missile.drawMissile()
            missile.moveMissile()
            #Check if missile is in bound
            if not missile.checkMissileBounds():
                self._missiles.remove(missile)
            
        





            

        






