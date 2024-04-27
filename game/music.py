import winsound
import stdaudio
import threading


'''
hit: 080997_Bullet
Pixabay

blaster: BLASTER 2
Pixabay

sound: Pixabay
The Final Boss Battle : alperomeresin
8-bit Air Fight : moodmode

'''


def playSong():
    musicTH = threading.Thread(target=song)
    musicTH.start()
    
def song():
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
