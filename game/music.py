import winsound
import stdaudio
import threading


'''
hit: 080997_Bullet
Pixabay

blaster: BLASTER 2
Pixabay

'''


def playSong():
    song = "song1.wav"
    winsound.PlaySound(song, winsound.SND_ASYNC)
def ShootSound():
    bullet = "bullet1"
    stdaudio.playFile(bullet)
def hitEnemy():
    Enemyhit = "EnemyHit.wav"
def hitPlayer():
    Playerhit = ""

    
        
def bullet():
    bulletTH = threading.Thread(target=ShootSound)
    bulletTH.start()
    #ShootSound()

    

    
def Enemy():
    pass
    
def Player():
    pass
