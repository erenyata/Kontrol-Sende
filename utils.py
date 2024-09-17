from PyQt5.QtCore import QThread,pyqtSignal
import time

class TimerThread(QThread):
    signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        self.seconds = 59
        self.mins = 24
        
    
    def run(self):                    
            while self.seconds > 0:
                time.sleep(1)
                self.seconds -= 1
                if self.seconds == 0:
                    if self.mins >  0:
                        self.mins -= 1 
                        self.seconds = 59
                self.signal.emit(str("{:2d}:{:2d}".format(self.mins,self.seconds)))

    def pause_thread(self): # threadi zorla durdurur
        self.terminate()

    def reset_thread(self): # threadi zorla durdurur seconds ve mins değişkenlerini sıfırlar böylece sayaç sıfırlanmış olur
        self.terminate()
        self.seconds = 59
        self.mins = 24
        