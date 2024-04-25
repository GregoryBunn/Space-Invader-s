import winsound
import time

class Music_class:
    def __init__(self):
        self.song = "song1.wav"
        self.Play = True
        self.bullet = ""
        self.Enemyhit = ""
        self.Playerhit = ""

    def playSong(self):
        while self.Play:
            winsound.PlaySound("song1.wav", winsound.SND_ASYNC)
            time.sleep(0.1)
    def stopSong(self):
        self.Play = False
    def PlaySong(self):
        self.Play = False
        
