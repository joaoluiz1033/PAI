import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import interface_function as inter_fun
import chess_ql as ql

from chess_control import Controler

def debug_trace():
    from PyQt5.QtCore import pyqtRemoveInputHook
    from pdb import set_trace
    pyqtRemoveInputHook()
    set_trace()

class ChessMovement(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)        
        self.controler = controler
        self.controler.addClient(self)
        self.valid_movements = []
        self.enemy_moves = []
        self.turn = 1
        self.movementUI()       
        
    def movementUI(self):
        layout = QVBoxLayout()
        piece_label = QLabel("Piece")
        self.piece = QLineEdit()
        movement_label = QLabel("Movement")
        self.movement = QLineEdit()
        valid_moves_label = QLabel("Valid moves")
        self.valid_moves = QTextEdit()        
        if self.controler.game_type == 1:
            move_button = QPushButton("Move")
            move_button.clicked.connect(self.playerVSIA)            
        elif self.controler.game_type == 2:
            move_button = QPushButton("Move")
            move_button.clicked.connect(self.userMove)
        elif self.controler.game_type == 3:
            move_button = QPushButton("Simulate")
            move_button.clicked.connect(self.IAIA2)            
        self.bshow_moves = QPushButton("Show moves (delete this button)")        
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
        if self.controler.user == 'b':
            self.IA_move()
            self.controler.refreshAll()
        else:
            self.show_moves()
        
    def playerVSIA(self):                
        piece = self.piece.text()
        movement = self.movement.text()
        self.enemy_moves = self.controler.send_U_move(piece,\
                              movement, self.valid_movements)
        #self.controler.send_who_plays()
        go = self.refresh()
        if go:            
            self.IA_move()  
            self.controler.refreshAll()
        else:
            self.controler.refreshAll()
                
    def IA_move(self):
        self.show_moves_IA()
        self.enemy_moves = self.controler.send_IA_move\
            (self.valid_movements, self.enemy_moves)
    
    def userMove(self):
        piece = self.piece.text()
        movement = self.movement.text()
        self.enemy_moves = self.controler.send_U_move(piece,\
                              movement, self.valid_movements)
        #self.controler.send_who_plays()
        go = self.controler.refreshAll()
            
    def IAIA(self): 
        i = 0
        go = True
        while go and i < 10: 
            go = self.refresh()
            if go:
                self.IA_move()            
                self.controler.refreshAll()
            else:
                self.controler.refreshAll()
            i += 1
            
    def IAIA2(self):                  
        go = self.refresh()
        if go:
            self.IA_move()            
            self.controler.refreshAll()
        else:
            self.controler.refreshAll()            
        
    def refresh(self):
        king = self.controler.give_who_plays()  
        self.show_moves()
        if not self.controler.give_game_state(self.valid_movements):                
            return True
        else:            
            self.controler.give_final_result(self.enemy_moves,king)
            return False
    
    def show_moves(self):
        self.valid_movements = self.controler.give_valid_moves()
        self.valid_moves.setPlainText(\
                      inter_fun.moves_to_string(self.valid_movements))  
    
    def show_moves_IA(self):
        self.valid_movements = self.controler.give_valid_moves()
        
        

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
        #self.board_pieces = ChessPieces(self,self.controler,self.layout)
 
        
class ChessPieces(QWidget):
    
    def __init__(self, parent, controler,layout):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)
        self.layout = layout
        self.pieces()
        
    def pieces(self):        
        piece_map = self.controler.give_map() 
        if self.controler.user == 'w':        
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
        else:
            for x in range(8):
                l = piece_map[x]
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


class MainWindow(QMainWindow):

    def __init__(self, controler):
        super().__init__()
        self.setWindowTitle("Xadrez")
        self.setWindowIcon(QIcon('./images/bk.png'))
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        self.controler = controler
        status_bar.showMessage('Xadrez version 2.0')         
        self.game_type = QComboBox()
        self.game_type.addItems(["Player vs IA","Player vs Player",\
                                 "IA vs IA"])
        game_type_label = QLabel("Type of game")        
        self.start_button = QPushButton("Next")
        self.start_button.clicked.connect(lambda: self.next_option(\
                                  self.game_type.currentText()))
        self.layout = QVBoxLayout()
        self.layout.addWidget(game_type_label)
        self.layout.addWidget(self.game_type)
        self.layout.addWidget(self.start_button)
        self.setWindowFlags(
        Qt.Window |
        Qt.CustomizeWindowHint |
        Qt.WindowTitleHint |
        Qt.WindowCloseButtonHint |
        Qt.WindowStaysOnTopHint |
        Qt.WindowMinimizeButtonHint
        )
        w = QWidget()
        w.setLayout(self.layout)
        self.setCentralWidget(w)
        
    def start_game(self):   
        self.mainwidget = chessUI(self,self.controler)
        self.setCentralWidget(self.mainwidget)
        self.setGeometry(300, 100, 700, 500)
        return True
    
    def next_option(self, game_type):
        if game_type == 'Player vs IA':
            self.controler.game_type = 1
            self.player_vs_IA()
        elif game_type == "Player vs Player":
            self.controler.game_type = 2
            self.player_vs_player()
        else:
            self.controler.game_type = 3
            self.IA_vs_IA()
            
    def player_vs_IA(self):
        self.IA_level = QComboBox()
        self.IA_level.addItems(["Random","Easy","Ok","Hard"])
        IA_level_label = QLabel("IA level")
        self.IA_level.currentTextChanged.connect(\
                                             self.IA_vs_player_level)
        self.User_team = QComboBox()
        self.User_team.addItems(["White","Black"])
        User_team_label = QLabel("User's team")
        self.User_team.currentTextChanged.connect(\
                                              self.IA_vs_player_team)
        self.layout.addWidget(IA_level_label)
        self.layout.addWidget(self.IA_level)
        self.layout.addWidget(User_team_label)
        self.layout.addWidget(self.User_team)
        self.start_button.setParent(None)
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)        
        
    def IA_vs_player_level(self):
        level = self.IA_level.currentText()        
        if level == "Random":
            self.controler.IA_level = 1
        elif level == "Easy":
            self.controler.IA_level = 2 
        elif level == "Ok":
            self.controler.IA_level = 3
        elif level == 'Hard':
            self.controler.IA_level = 4
    
    def IA_vs_player_team(self):
        user = self.User_team.currentText()
        if user == "White":
            self.controler.user = 'w'
        else:
            self.controler.user = "b"        
    
    def player_vs_player(self):
        self.type_of_server = QComboBox()
        self.type_of_server.addItems(["Local","Dedicated server"])
        type_of_server_label = QLabel("Local/Server")
        self.type_of_server.currentTextChanged.connect(\
                                             self.player_server)
        self.layout.addWidget( type_of_server_label)
        self.layout.addWidget(self. type_of_server)        
        self.start_button.setParent(None)
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)
        
    def player_server(self):
        server = self.type_of_server.currentText()
        if user == "Local":
            self.controler.server = 1
        else:
            self.controler.server = 2
    
    def IA_vs_IA(self):
        self.IA1_level = QComboBox()
        self.IA1_level.addItems(["Random","Easy","Ok","Hard"])
        IA1_level_label = QLabel("IA level for white")
        self.IA1_level.currentTextChanged.connect(\
                                             self.IA_vs_IA_level1)
        self.IA2_level = QComboBox()
        self.IA2_level.addItems(["Random","Easy","Ok","Hard"])
        IA2_level_label = QLabel("IA level for black")
        self.IA2_level.currentTextChanged.connect(\
                                             self.IA_vs_IA_level2)        
        self.layout.addWidget(IA1_level_label)
        self.layout.addWidget(self.IA1_level)
        self.layout.addWidget(IA2_level_label)
        self.layout.addWidget(self.IA2_level)
        self.start_button.setParent(None)
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)
    
    def IA_vs_IA_level1(self):
        level1 = self.IA1_level.currentText()        
        if level1 == "Random":
            self.controler.IA_level = 1
        elif level1 == "Easy":
            self.controler.IA_level = 2 
        elif level1 == "Ok":
            self.controler.IA_level = 3
        elif level1 == 'Hard':
            self.controler.IA_level = 4
    
    def IA_vs_IA_level2(self):                   
        level2 = self.IA2_level.currentText()        
        if level2 == "Random":
            self.controler.IA2_level = 1
        elif level2 == "Easy":
            self.controler.IA2_level = 2 
        elif level2 == "Ok":
            self.controler.IA2_level = 3
        elif level2 == 'Hard':
            self.controler.IA2_level = 4
    
def main():
    app = QApplication([])
    controler = Controler()
    win = MainWindow(controler)  
    win.show()
    app.exec()
    
    
if __name__ == '__main__':
    main()