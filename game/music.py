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
    #Tread for background music
    musicTH = threading.Thread(target=song)
    musicTH.start()
    
def song():
    #background song
    song = "song1.wav"
    winsound.PlaySound(song, winsound.SND_ASYNC)

def ShootSound():
    #Shooting sound
    bullet = "blast"
    stdaudio.playFile(bullet)

def hitPlayer():
    #live lose sound
    Playerhit = "Life"
    stdaudio.playFile(Playerhit)

    
        
def bullet():
    #bullet thread
    bulletTH = threading.Thread(target=ShootSound)
    bulletTH.start()

    
def Player():
    #player live lose thread
    PlayerTH = threading.Thread(target=hitPlayer)
    PlayerTH.start()
