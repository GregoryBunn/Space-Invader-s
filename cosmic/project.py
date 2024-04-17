#runs the main project
import objects, game, title

def main():
    #initialise game screen and player
    screen = objects.screen()
    player = objects.shooter()
    
    #run title screen
    title.startSetup(screen)
    
    play = True
    while(play):
        #run game
        player = game.gamerun(screen, player)

        #run gameover
        title.gameover(screen, player)

if __name__=="__main__":main()
