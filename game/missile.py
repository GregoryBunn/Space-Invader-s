import stddraw
import math




class Missile:
    def __init__(self,x:float,y:float,dir:float,typ:int,owner:int,size:int):
        self.x = x #missile x
        self.y = y #missile y
        self.dir = dir #missile direction
        self.typ = typ #type of missile
        self.owner = owner #missile owner
        self.speed = 4 #missile speed
        self.size = size

    #draw Missile 
    def drawMissile(self):

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
        screenX = 100
        screenY = 100

        #Check if missile x is in the screen bounds
        if self.x > screenX-6 or self.x < -screenX+6:
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
    def __init__(self):
        self.missiles = []
    def add_missile(self,missile:Missile):
        self.missiles.append(missile)
    def remove_missile(self,missile:Missile):
        if missile in self.missiles:
            self.missiles.remove(missile)
    def move_drawMissiles(self):
        for missile in self.missiles[:]:
            missile.moveMissile()
            missile.drawMissile()
            if not missile.checkMissileBounds():
                self.missiles.remove(missile)

        





            

        






