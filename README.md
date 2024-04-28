

To run the Project ensure you have all the standard libraries installed.
Run python project.py once you're in the game folder.

Additional elements added to the game:

- The game is structured in a modular fashion, using principles of object-oriented design implemented by Wikus.
- Music and sound were added to the game by Wikus. These sounds were downloaded from Pixabay (Creative Commons CC0 license). According to the Pixabay website, the sounds' author(s) do not require that they are mentioned when their sounds are used, but they are still mentioned.
- Additional graphics were also added to the game. The aliens were designed by Greg, who also designed the Ship graphic which was later upgraded by David Van Heerden, a designer willing to help us, free of charge, for an updated ship design.
- A player select screen was added at the start of the program for the user to choose the game mode - single or multiplayer.
- Special Ship rotation was added to the game by Wikus and Greg to make it possible for the ship to rotate its turret, even though it is an image, and rotate only the turret without the rest of the image rotating.
When playing sound and rotating an image it takes too long and makes the game lag. Greg used threading to do these tasks separately, thus preventing the game from lagging.
- When elements in the game change, the time needed to update the screen will change. Greg took this into account by measuring the time it takes to run the code in real-time and updating the framerate accordingly to ensure a steady frame rate.
- Zoe created a scoring system that takes the score of the individual players each round and also the total score of the combined player across the levels. She also used text files to enable a high score system that is able to store a previous high score and update the score if it is beaten.
- Different enemy types were implemented into the game, mainly a basic enemy and a boss type. The basic enemy can differ in hitpoints, changing its appearance slightly.
- Zoe also added multiple levels to the game by changing the amount of enemies, enemy types, enemy speed, and the enemy counter-attack speed per level.
- A level loading screen was added in-between levels to show the user that the previous level was beaten and that the next level is progressing. It loads automatically into the next level after a few seconds.
- Wikus added an additional shooter to the game where two players are able to play simultaneously. They play as a team to reach the highest score but can also play competitively against each other each round.
- Enemy counter-attack was also added to the game as a team effort. The counter-attack is an unpredictable event that gets more intense as the levels progress.
- Zoe added hitpoints to the game making it possible for the players to have multiple lives, as well as enemies that have more than one life depending on the enemy type and game level.
- Wikus and Greg added power-ups to the game, thus making it possible to increase the player speed, fire rate, and lives by getting a power-up.
- A special missile timer was added to the game by Wikus which enables a player to wait longer before firing and so shooting a super missile that has a bigger radius and that bounces off the side walls.
- Wikus added a health bar for the final Boss enemy making it feel more like a final battle and shows how close you are to winning.
- An Extra keyboard Feature was added: when 'W' is pressed the ship points vertically again to make it easy to reset the shooter angle