from threading import Timer
from PyQt5 import QtWidgets, QtCore,uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
import sys
from music import Music
from utils import TimerThread
from todo import Todo
from success_tracking import Success_Tracking
class MainWindow(QtWidgets.QMainWindow):
    signal_to_sett = pyqtSignal()
    signal_to_music = pyqtSignal()
    signal_to_todo = pyqtSignal()
    signal_to_tracker = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ks-main.ui",self)
        self.btnStart.clicked.connect(self.start_timer)
        self.btnPause.clicked.connect(self.pause_timer)
        self.btnReset.clicked.connect(self.reset_timer)
        self.btnTracker.clicked.connect(self.to_tracker)
        self.btnMusic.clicked.connect(self.to_music)
        self.btnTodo.clicked.connect(self.to_todo)
        self.setWindowIcon(QIcon("icons/icon.png"))
        self.thread = TimerThread()
        self.music = Music()
        
    '''
    # def set_pomodoro(self):
    #     self.thread.pomodoro = int(self.spinPomodoro.value())
    #     self.kalanPomodoro.setText(f"Kalan Pomodoro: {self.thread.pomodoro}")

    # def set_timer(self):

    #     # self.thread.mins = int(self.lineTime.text())
    #     self.label.setText("{:2d}:{:2d}".format(self.thread.mins,self.thread.seconds))
    '''

    def start_timer(self):                     # Süreyi ayarlayıp sayacı başlatır
        if self.rdWork.isChecked():
            self.thread.mins = 24
        elif self.rdShortBreak.isChecked():
            self.thread.mins = 4
        elif self.rdLongBreak.isChecked():
            self.thread.mins = 14
        self.thread.start()
        self.thread.signal.connect(self.change_timer)

    def to_music(self):
        self.signal_to_music.emit()
    
    def to_todo(self):
        self.signal_to_todo.emit()

    def to_tracker(self):
        self.signal_to_tracker.emit()

    def change_timer(self,val):     # thread instanceının emit ettiği signaldeki değer değiştikçe self.lalbel a yazdırır
        self.label.setText(str(val))

    def pause_timer(self):       # thread örneğinin pause_thread metodunu çağırır
        self.thread.pause_thread() 

    def reset_timer(self):      # thread örneğinin reset_thread metodunu çağırır labela threadin mins ve seconds değişkenlerinin değerlerini yazar
       self.thread.reset_thread()
       self.label.setText(str("{:2d}:{:2d}".format(self.thread.mins,self.thread.seconds)))

    


class Controller:
    def show_main(self):
        self.main = MainWindow()
        self.main.show()
        self.main.signal_to_music.connect(self.show_music)
        self.main.signal_to_todo.connect(self.show_todo)
        self.main.signal_to_tracker.connect(self.show_tracker)
    def show_music(self):
        self.main.music.show()
    
    def show_todo(self):
        self.todo = Todo()
        self.todo.show()

    def show_tracker(self):
        self.tracker = Success_Tracking()
        self.tracker.show()

app = QtWidgets.QApplication(sys.argv)
ctr = Controller()
ctr.show_main()
sys.exit(app.exec())