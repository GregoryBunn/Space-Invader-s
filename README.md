Run the 'gameRun.py' in 'CS 214 Final Code' to run the code. Just make sure you change your directory in terminal to 'CS 214 Final Code' otherwise it will say that it can't
find the png files in the current directory


Different methods for objects that may be confusing:
      
The get... and set... method: (getX() or setY()):
- variables are ment to be private in objects according to our prof, so thats why unders the dunder method init (__init__) when you set the variables
- with the '_' it makes them private. For example self._x = x. But now because they are provate, we can't access or change the variables information outside of the class. 
- Thats why we have the get and set method. get will return the value that it's getting and set will set the value you input to the atribute you set it to.

The ships have and angle, pos, state, x, and y atribute:
- x and y are pretty self explanitory
- the angle atribute is changed when rotating and is only there so that when you fire a bullet it is given the angle of the ship on the bullets initialization.
- the pos atribute is the position in the pics list in the file 'ship.py', the pics list is where we store all the different png's of the ship in different orrientations. All of these png's are done
- on start up of the program and thats why it takes a second or 2 to start. If we didn;t store them in a list before the game started it would have to do the maths for the orrientation of the ship every time and
- that would slow down the program considerably.
