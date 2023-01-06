import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *


class WinForm(QWidget):
    
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('QTimer example')
        self.listFile=QListWidget()
        self.label=QLabel('Label')
        layout=QGridLayout()
        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)
        self.time = QTime(0, 10, 0)
        layout.addWidget(self.label,0,0,1,2)
        self.startTimer()
        self.setLayout(layout)

    def showTime(self):        
        self.time = self.time.addSecs(-1)
        timeDisplay=self.time.toString('mm:ss')
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        
    def endTimer(self):
        self.timer.stop()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())