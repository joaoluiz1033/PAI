import matplotlib.pyplot as plt
import random
import pdb

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from chess_control import Control


class ChartsWidget(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)        
        layout = QVBoxLayout()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.draw()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

class LogWidget(QTextEdit):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)
        self.setFixedHeight(150)
        self.setReadOnly(True)
        self.append("LogWidget")        

    def refresh(self):
        message = self.controler.message        
        if message:
            self.append(message)


class ParamsWidget(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)        
        self.setFixedWidth(400)
        bd = controler.board
        controler.move_options()              
                
    def on_calendar_clicked(self, date):
        self.controler.select_date(date)


class MainWidget(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.setMinimumSize(640, 480)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.paramswidget = ParamsWidget(self, controler)        
        #self.logwidget = LogWidget(self, controler)
        hlayout.addWidget(self.paramswidget, 0)        
        vlayout.addLayout(hlayout, 1)
        #vlayout.addWidget(self.logwidget, 0)
        self.setLayout(vlayout)


class Mainwindow(QMainWindow):
    
    def __init__(self,control):
        super().__init__()
        self.setWindowTitle("Xadrez")
        self.mainwidget = MainWidget(self, control)
        self.setCentralWidget(self.mainwidget)


if __name__ == '__main__':
    app = QApplication([])
    controler = Control()
    win = Mainwindow(controler)
    controler.__init__()
    win.show()
    app.exec()