import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import interface_function as inter_fun

from chess_control import Controler


class ChessMovement(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self.movementUI()
        
    def movementUI(self):
        layout = QVBoxLayout()
        piece_label = QLabel("Piece")
        self.piece = QLineEdit()
        movement_label = QLabel("Movement")
        self.movement = QLineEdit()
        valid_moves_label = QLabel("Valid moves")
        self.valid_moves = QTextEdit()
        layout.addWidget(piece_label)
        layout.addWidget(self.piece)
        layout.addWidget(movement_label)        
        layout.addWidget(self.movement)
        layout.addWidget(valid_moves_label)
        layout.addWidget(self.valid_moves)
        self.setLayout(layout)


class ChessBoard(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        layout = self.board()  
        
        
    def board(self):        
        layout = QGridLayout()
        white = QPixmap(50, 50)
        white.fill(QColor(Qt.white))
        black = QPixmap(50, 50)
        black.fill(QColor(160,82,45))        
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    square = QLabel()
                    square.setPixmap(white)
                    layout.addWidget(square, i, j)
                else:
                    square = QLabel()
                    square.setPixmap(black)
                    layout.addWidget(square, i, j)
        self.setLayout(layout)
        return layout 
    
    def board_painter(self):
        pass
    

class ChessPieces(QWidget):
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self.pieces()
        
    def pieces(self):
        layout = QGridLayout()
        piece_map = self.controler.give_map()        
        for x in range(8):
            l = piece_map[7-x]
            j = 0
            for y in l:
                if y is not None:
                    piece = QLabel()
                    piece_type = inter_fun.add_piece(y.name)
                    piece.setPixmap(piece_type)
                    layout.addWidget(piece, x, j)
                j += 1
        self.setLayout(layout)
    
    
class chessUI(QWidget):

    def __init__(self, parent, controler):
        super().__init__(parent)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.chess_board = ChessBoard(self, controler)
        self.chess_movement = ChessMovement(self, controler)        
        hlayout.addWidget(self.chess_board,0)
        hlayout.addWidget(self.chess_movement,1)        
        vlayout.addLayout(hlayout,1)
        self.setLayout(vlayout)
    
class MainWindow(QMainWindow):

    def __init__(self, controler):
        super().__init__()
        self.setWindowTitle("Xadrez")
        self.setWindowIcon(QIcon('./images/wb.png'))
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage('Xadrez version 1.0')
        self.mainwidget = chessUI(self, controler)
        self.setCentralWidget(self.mainwidget)


def main():
    app = QApplication([])
    controler = Controler()
    win = MainWindow(controler)   
    controler.__init__()
    win.show()
    app.exec()
    
    
if __name__ == '__main__':
    main()