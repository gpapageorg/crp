import vlc

class Player():

    def __init__(self, url):
        self.p = vlc.MediaPlayer(url)
    
    def play(self):
        self.p.play()

    def pause(self):
        self.p.pause()
    def setVolume(self,vol):
        self.p.audio_set_volume(vol)