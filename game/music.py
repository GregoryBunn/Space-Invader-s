import winsound
import threading

'''
hit: 080997_Bullet
Pixabay

blaster BLASTER 2
Pixabay

'''


def playSong():
    song = "song1.wav"
    winsound.PlaySound(song, winsound.SND_ASYNC)
def ShootSound():
    bullet = "bullet.wav"
    winsound.PlaySound(bullet, winsound.SND_ASYNC)
def hitEnemy():
    Enemyhit = "EnemyHit"
    winsound.PlaySound(Enemyhit, winsound.SND_ASYNC)
def hitPlayer():
    Playerhit = ""
    pass
    
        
def bullet():
    bulletTH = threading.Thread(target=ShootSound(),args=(None))
    bulletTH.start()
def Enemy():
    EnemyTH = threading.Thread(target=hitEnemy(),args=(None))
    EnemyTH.start()
def Player():
    PlayerTH = threading.Thread(target=hitPlayer(),args=(None))
    PlayerTH.start()