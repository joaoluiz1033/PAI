import matplotlib.pyplot as plt
import random
import pdb

from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from chess_control import Controller


class ParamsWidget(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)   
    
    def play(self):
        l_valid_moves = self.controler.give_valid_moves() 
        end_game = self.controler.give_game_state(l_valid_moves)       
        if not end_game:
            if self.controler.give_who_plays() == 'w':
                piece = input("Choose a piece: ")
                movement = input("Choose a movement: ")
                l_enemy_moves = self.controler.send_U_moves(\
                          piece,movement,l_possible_moves)
            else:
                l_enemy_moves = self.controler.send_IA_moves(\
                          l_possible_moves)
        else:
            self.controler.give_final_result
            
    def refresh(self):
        self.controler.give_map_board()


class MainWidget(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.setMinimumSize(640, 480)


class MainWindow(QMainWindow):
    
    def __init__(self, controler):
        super().__init__()
        self.setWindowTitle("Xadrez")
        self.mainwidget = MainWidget(self, controler)
        self.setCentralWidget(self.mainwidget)        
        



if __name__ == '__main__':
    app = QApplication([])
    controler = Controller()
    win = MainWindow(controler)
    controler.__init__()
    win.show()
    app.exec()