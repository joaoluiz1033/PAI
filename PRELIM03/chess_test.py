import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from chess_control import Controler


class Map():
    
    def __init__(self):
        pass

class Map_board(QWidget):
    
    def __init__(self, parent,controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)        
        self.setFixedWidth(300)
        layout = QVBoxLayout()
        
    def print_map(self):
        self.controler()
        
        
class MainWidget(QWidget):
    
    def __init__(self, parent,controler):
        super().__init__(parent)
        self.setMinimumSize(640, 480)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.map = Map_board(self,controler)
        hlayout.addWidget(self.map, 0)
        vlayout.addLayout(hlayout, 1)
        self.setLayout(vlayout)
           
    
class MainWindow(QMainWindow):
    
    def __init__(self,controler):
        super().__init__()
        self.setWindowTitle("Xadrez")
        self.mainwidget = MainWidget(self,controler)

def main():
    app = QApplication([])
    controler = Controler()
    win = MainWindow(controler)    
    win.show()
    app.exec()
    
    
if __name__ == '__main__':
    main()