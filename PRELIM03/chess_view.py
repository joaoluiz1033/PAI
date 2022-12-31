import sys
import pdb

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import interface_function as inter_fun

from chess_control import Controler


class ChessMovement(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)        
        self.controler = controler
        self.controler.addClient(self)
        self.valid_movements = []
        self.enemy_moves = []
        self.movementUI()
        
        
    def movementUI(self):
        layout = QVBoxLayout()
        piece_label = QLabel("Piece")
        self.piece = QLineEdit()
        movement_label = QLabel("Movement")
        self.movement = QLineEdit()
        valid_moves_label = QLabel("Valid moves")
        self.valid_moves = QTextEdit()
        move_button = QPushButton("Move")
        move_button.clicked.connect(self.User_move)
        self.bshow_moves = QPushButton("Show Possible Moves")
        self.bshow_moves.clicked.connect(self.show_moves)
        layout.addWidget(piece_label)
        layout.addWidget(self.piece)
        layout.addWidget(movement_label)        
        layout.addWidget(self.movement)
        layout.addWidget(move_button)
        layout.addWidget(valid_moves_label)
        layout.addWidget(self.valid_moves)
        layout.addWidget(self.bshow_moves)
        self.setLayout(layout)        
        
        
    def User_move(self):
        piece = self.piece.text()
        movement = self.movement.text()
        self.enemy_moves = self.controler.send_U_move(piece,\
                              movement, self.valid_movements)
            
    def refresh(self):
        king = self.controler.give_who_plays()
        if self.controler.give_game_state(self.valid_movements):
            pass
        else:
            self.controler.give_final_result(self.enemy_moves,king)
    
    def show_moves(self):
        self.valid_movements = self.controler.give_valid_moves()
        self.valid_moves.setPlainText(\
                          inter_fun.moves_to_string(self.valid_movements))

class ChessBoard(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)        
        self.controler = controler 
        self.controler.addClient(self)
        self.layout = QGridLayout()  
        self.board()        
        self.board_pieces = ChessPieces(self,controler,self.layout)        
        
    def board(self): 
        white = QPixmap(50, 50)
        white.fill(QColor(Qt.white))
        black = QPixmap(50, 50)
        black.fill(QColor(160,82,45))        
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    square = QLabel()
                    square.setPixmap(white)
                    self.layout.addWidget(square, i, j)
                else:
                    square = QLabel()             
                    square.setPixmap(black)                    
                    self.layout.addWidget(square, i, j)
        self.setLayout(self.layout)
         
    def refresh(self):
        self.board()
        self.board_pieces = ChessPieces(self,self.controler,self.layout)
 
        
class ChessPieces(QWidget):
    
    def __init__(self, parent, controler,layout):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)
        self.layout = layout
        self.pieces()
        
    def pieces(self):        
        piece_map = self.controler.give_map()
        for x in range(8):
            l = piece_map[7-x]
            j = 0
            for y in l:
                if y is not None:
                    piece = QLabel()                  
                    piece_type = inter_fun.add_piece(y.name)                                      
                    piece.setPixmap(piece_type.scaled(50, 50))                  
                    self.layout.addWidget(piece, x, j)
                j += 1
        
    def refresh(self):
        self.pieces()
    
    
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


class chessMenu(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler 
        game_type = QComboBox()
        game_type.addItems(["Player vs Player", "Player vs IA", "IA vs IA"])
        game_type_label = QLabel("Type of game")
        IA_level = QComboBox()
        IA_level.addItems(["Random","Not that stupid","Ok","Hard AF"])
        IA_level_label = QLabel("IA level (if any)")
        start_button = QPushButton("Begin match")
        start_button.clicked.connect(self.start_game)
        game_server = QComboBox()
        game_server.addItems(["Offline","Online"])
        game_server_label = QLabel("Server")
        layout = QVBoxLayout()
        layout.addWidget(game_type_label)
        layout.addWidget(game_type)
        layout.addWidget(IA_level_label)
        layout.addWidget(IA_level)
        layout.addWidget(game_server_label)
        layout.addWidget(game_server)
        layout.addWidget(start_button)        
        self.setLayout(layout)        
    
    def start_game(self):   
        self.mainwidget = chessUI(self,controler)
        self.setCentralWidget(self.mainwidget)
        return True
        

class chessIni(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.menu = chessMenu(self,controler)
        hlayout.addWidget(self.menu,0)
        vlayout.addLayout(hlayout,1)
        self.setLayout(vlayout)
        
    
class MainWindow(QMainWindow):

    def __init__(self, controler):
        super().__init__()
        self.setWindowTitle("Xadrez")
        self.setWindowIcon(QIcon('./images/wb.png'))
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        self.controler = controler
        status_bar.showMessage('Xadrez version 1.0')         
        game_type = QComboBox()
        game_type.addItems(["Player vs Player", "Player vs IA", "IA vs IA"])
        game_type_label = QLabel("Type of game")
        IA_level = QComboBox()
        IA_level.addItems(["Random","Not that stupid","Ok","Hard AF"])
        IA_level_label = QLabel("IA level (if any)")
        start_button = QPushButton("Begin match")
        start_button.clicked.connect(self.start_game)
        game_server = QComboBox()
        game_server.addItems(["Offline","Online"])
        game_server_label = QLabel("Server")
        layout = QVBoxLayout()
        layout.addWidget(game_type_label)
        layout.addWidget(game_type)
        layout.addWidget(IA_level_label)
        layout.addWidget(IA_level)
        layout.addWidget(game_server_label)
        layout.addWidget(game_server)
        layout.addWidget(start_button)
        self.setWindowFlags(
        Qt.Window |
        Qt.CustomizeWindowHint |
        Qt.WindowTitleHint |
        Qt.WindowCloseButtonHint |
        Qt.WindowStaysOnTopHint |
        Qt.WindowMinimizeButtonHint
        )
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        
    def start_game(self):   
        self.mainwidget = chessUI(self,self.controler)
        self.setCentralWidget(self.mainwidget)
        self.setGeometry(300, 100, 700, 500)
        return True

def main():
    app = QApplication([])
    controler = Controler()
    win = MainWindow(controler)  
    win.show()
    app.exec()
    
    
if __name__ == '__main__':
    main()