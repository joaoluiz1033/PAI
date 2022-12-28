import sys
import pdb

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from chess_control import Controler

class Map_draw(QWidget):
    def __init__(self, parent,controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)
        self.textEdit = QTextEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        self.setLayout(layout)
        
    def draw(self):
        print(self.controler)
        
        
class Map_board(QWidget):
    
    def __init__(self, parent,controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)
        self.l_possible_moves = []
        self.button_map = QPushButton("Show Map")
        self.button_map.clicked.connect(self.print_map)                           
        self.piece = QLineEdit()
        self.piece_label = QLabel("Piece")
        self.movement = QLineEdit()
        self.movement_label = QLabel("Movement")
        self.button_move = QPushButton("Make a movement")                  
        self.button_move.clicked.connect(self.move_board)
        self.bshow_moves = QPushButton("Show Possible Moves")
        self.bshow_moves.clicked.connect(self.show_moves)    
        self.text_box = QTextEdit()
        self.text_box.setFontPointSize(9);
        layout = QVBoxLayout()  
        layout.addWidget(self.button_map) 
        layout.addWidget(self.bshow_moves)
        layout.addWidget(self.piece_label)
        layout.addWidget(self.piece)        
        layout.addWidget(self.movement_label)
        layout.addWidget(self.movement)        
        layout.addWidget(self.button_move) 
        layout.addWidget(self.text_box)
        self.setLayout(layout)        
    
    def print_map(self):
        s = self.controler.give_map_board()
        self.text_box.setPlainText(s)
        
    
    def move_board(self):
        self.controler.send_U_move(self.piece.text(), self.movement.text(), self.l_possible_moves)
        
    def show_moves(self):
        self.l_possible_moves = self.controler.give_valid_moves()  
        

class MainWidget(QWidget):
    
    def __init__(self, parent,controler):
        super().__init__(parent)        
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.map = Map_board(self,controler)        
        hlayout.addWidget(self.map, 0)
        vlayout.addLayout(hlayout, 0)
        self.setLayout(vlayout)
         
    
class MainWindow(QMainWindow):
    
    def __init__(self,controler):
        super().__init__()
        self.setWindowTitle("Xadrez")
        self.mainwidget = MainWidget(self,controler)
        self.setCentralWidget(self.mainwidget)

def main():
    app = QApplication([])
    controler = Controler()
    win = MainWindow(controler)    
    win.show()
    app.exec()
    
    
if __name__ == '__main__':
    main()