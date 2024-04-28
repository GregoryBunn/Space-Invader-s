Run the 'gameRun.py' in 'CS 214 Final Code' to run the code. Just make sure you change your directory in terminal to 'CS 214 Final Code' otherwise it will say that it can't
find the png files in the current directory

      
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

The owner atribute for bullets:
- That is just so that we can see which player shot the bullet in 2 player
- it's to make score traking a lot easier. you will see if you kill an alien now it will print to terminal which player shot the bullet that killed the alien.

Additional elements added to the game
- The game is structured in a modular fashion, using principles of object oriented design implemented by Wikus
- Music and sound was added to the game by Wikus. These sounds were downloaded from pixabay (Creative Commons CC0 license) According to the pixabay website the sounds authers do not require that they are mentioned when their sounds are used,  but we still mentioned them
- Additional graphics were also added to the game. The aliens were designed by Greg, he also designed the Ship grapic which was later upgraded by David Van Heerden a Designer willing to help us ,free of charge for a updated ship design
- Special Ship rotation was added to the game by Wikus and Greg to make it possible for the ship to rotate its turret even though it is an image and rotate only the turrent without the rest of the image rotating
- When playing sound and rotating an image it takes to long and makes the game lag. Greg used threading to do these tasks sepperatly and therefor stop the game from lagging
- When elements in the game change the time needed to update the screen will change. Greg took this into account by measuring the time it takes to run the code real time and update the framerate accordingly to unsure a steady frame rate
- Zoe created a scoring system that takes the score of the individual players each round and also the total score of the combined player across the levels. She also used text files to unable a high score system that is able to store a previous high score and update the score if it is beaten
- Zoe also added multiple level to the game by changing the amount of enemys, enemytypes, enemyspeed and the enemy counter attack speed
- Wikus added an additional shooter to the game where two players are able to play sumaltaniosly. They play as a team to reach a the highest score but can also play competitavly against each other each round
- Enemy counter attack was also added to the game as a team effort. The counter attack is an unpredictable event that gets more intense as the levels progress
- Zoe added enemy hitpoints to the game making it possible for the  players to have multiple lives and also enemys that have more than one live depending on the enemy type
- Wikus and Greg added powerups to the game making it possible to increase the player speed, fire rate and lives by getting a powerup
- A special missile timer was added to the game by Wikus which enables a player to wait longer before firing and so shooting a super missile that has a bigger radius and that bounces of the side walls
- Wikus added a health bar for the final Boss enemy making it feel more like a final battle



