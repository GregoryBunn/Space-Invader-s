import stddraw
import math




class Missile:
    """
    Represents a missile object in a game with properties for managing its state and behavior.

    Attributes:
        x (float): The x-coordinate of the missile on the game screen.
        y (float): The y-coordinate of the missile on the game screen.
        dir (float): The direction of the missile's travel.
        typ (int): The type of missile, which affects its appearance and possibly behavior.
        owner (int): The identifier of the missile's owner, which could differentiate between player and enemy missiles.
        speed (int): The speed at which the missile moves.
        size (int): The size of the missile, affecting its appearance and collision area.

    Methods:
        drawMissile(): Draws the missile on the game screen using different colors and shapes based on the missile type.
    """
    def __init__(self,x:float,y:float,dir:float,typ:int,owner:int,size:int):
        """
        Initializes a new instance of the Missile class with specified attributes.

        Parameters:
            x (float): The x-coordinate of the missile on the game screen.
            y (float): The y-coordinate of the missile on the game screen.
            dir (float): The direction of the missile's travel.
            typ (int): The type of the missile.
            owner (int): The identifier of the missile's owner.
            size (int): The size of the missile.
        """
        self.x = x #missile x
        self.y = y #missile y
        self.dir = dir #missile direction
        self.typ = typ #type of missile
        self.owner = owner #missile owner
        self.speed = 4 #missile speed
        self.size = size

    #draw Missile 
    def drawMissile(self):
        """
        Draws the missile on the game screen, with different characteristics based on the missile type.
        Type 0 missiles are drawn green, type 1 are red, and type 2 are blue.
        """

        if self.typ == 2:
            #set pen color
            stddraw.setPenColor(stddraw.BLUE)

            #draw missile
            stddraw.filledCircle(self.x,self.y,self.size)


        #creates missile of type 1S
        if self.typ == 1:
            #set pen color
            stddraw.setPenColor(stddraw.RED)

            #draw missile
            stddraw.filledCircle(self.x,self.y,self.size)
        #create missile of type 0
        if self.typ == 0:
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.setPenRadius(0.5)
            stddraw.line(self.x, self.y, self.x, (self.y-5)) 
    
    def moveMissile(self):
        """
        Updates the missile's position based on its direction and speed, moving it across the game screen.
        """

        #move missile if missile is a counter attack missile
        if self.typ == 0:
            speed = 0.5
            self.y= self.y - speed*(self.speed*(1-abs(self.dir/(math.pi/2))))
        
        #move player missiles
        else:
            #change x pos
            self.x = self.x + (self.speed*(self.dir/(math.pi/2)))
            #change y pos
            self.y = self.y + (self.speed*(1-abs(self.dir/(math.pi/2))))



    def checkMissileBounds(self):
        """
        Checks whether the missile is still within the game screen boundaries.

        Returns:
            bool: True if the missile is within bounds, False otherwise.
        """
        screenX = 100
        screenY = 100

        #Check if missile x is in the screen bounds
        if self.x > screenX-6 or self.x < -screenX+6:
            #super missile bounce of wall
            if self.typ == 2 and abs(self.dir)< math.pi/2.1:
                self.dir = -self.dir
                return True
            else:

                #remove missile
                return False
        
        #Check if missile y is in the screen bounds
        elif self.y > screenY-8 or self.y < -screenY+8:
            #remove missile
            return False
        
        #allow missile
        else:
            return True
        
class MissileList:
    """
    Manages a collection of missiles in the game, handling operations such as adding, removing, and updating missiles.

    Attributes:
        missiles (list of Missile): The list of missile objects currently active in the game.
    """
    def __init__(self):
        self.missiles = []
    def add_missile(self,missile:Missile):
        """
        Adds a new missile to the list of active missiles.

        Parameters:
            missile (Missile): The missile to be added to the list.
        """
        self.missiles.append(missile)
    def remove_missile(self,missile:Missile):
        """
        Removes a missile from the list of active missiles.

        Parameters:
            missile (Missile): The missile to be removed from the list.
        """
        if missile in self.missiles:
            self.missiles.remove(missile)
    def move_drawMissiles(self):
        """
        Updates the positions of all missiles in the list and draws them on the screen.
        This method also checks for missiles that are out of bounds and removes them.
        """
        for missile in self.missiles[:]:
            missile.drawMissile()
            missile.moveMissile()
            if not missile.checkMissileBounds():
                self.missiles.remove(missile)
            
        





            

        






