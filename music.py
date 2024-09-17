from PyQt5 import QtWidgets,QtCore,uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl
import os
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class Music(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/music.ui",self)
        self.player = QMediaPlayer()
        self.setWindowIcon(QIcon("icons/icon.png"))

        # self.btnVolumeUp.clicked.connect(self.volumeUp)
        # self.btnVolumeDown.clicked.connect(self.volumeDown)
        self.btnPlay.clicked.connect(self.play_audio)
        self.btnStop.clicked.connect(self.pause_audio)
        self.btnPlay.setIcon(QIcon("icons/play.ico"))
        self.btnStop.setIcon(QIcon("icons/pause.ico"))
        self.setWindowIcon(QIcon("icons/music.ico"))
        self.slider.valueChanged.connect(self.changed_slider)
        self.slider.setRange(0,100) # sliderin değer aralığının 0-100 arası olmasını sağlar
        self.slider.setValue(20)
        self.player.setVolume(20)

        self.pixmap = QPixmap("icons/volume.ico")
        self.lblVolume.setPixmap(self.pixmap)

    def changed_slider(self):   # slider değiştikçe playerin volumeünü sliderin değerine eşitler
       value = self.slider.value()
       self.player.setVolume(value)
       
    # def volumeUp(self):
    #     currentVolume = self.player.volume()
    #     self.player.setVolume(currentVolume + 5)

    # def volumeDown(self):
    #     currentVolume = self.player.volume()
    #     self.player.setVolume(currentVolume - 5)

    # def volumeMute(self):
    #     self.player.setMuted(not self.player.isMuted())

    def play_audio(self):
        full_file_path = os.path.join(os.getcwd(),"music/test.mp3")
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
        self.lblMusic.setText(full_file_path)
        
    def pause_audio(self):
        self.player.stop()