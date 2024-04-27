import winsound
import stdaudio
import threading


'''
Shoot : Pixabay
080997_Bullet




Song: Pixabay
8-bit Air Fight : moodmode

Live lost: Pixabay
negative_beeps



'''


def playSong():
    musicTH = threading.Thread(target=song)
    musicTH.start()
    
def song():
    song = "song1.wav"
    winsound.PlaySound(song, winsound.SND_ASYNC)

def ShootSound():
    bullet = "blast"
    stdaudio.playFile(bullet)

def hitPlayer():
    Playerhit = "Life"
    stdaudio.playFile(Playerhit)

    
        
def bullet():
    bulletTH = threading.Thread(target=ShootSound)
    bulletTH.start()

    
def Player():
    PlayerTH = threading.Thread(target=hitPlayer)
    PlayerTH.start()
