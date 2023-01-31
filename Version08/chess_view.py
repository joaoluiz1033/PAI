import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *

import interface_function as inter_fun
import chess_ql as ql
import coordinates

from chess_control import Controler

def debug_trace():
    from PyQt5.QtCore import pyqtRemoveInputHook
    from pdb import set_trace
    pyqtRemoveInputHook()
    set_trace()


def clearLayout(self, layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())
                

def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
                

class ClickableLabel(QLabel):
    
    clicked = pyqtSignal()    
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
            
            
class startIAGame(QWidget):
    
    def __init__(self, parent, controler):    
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start)
        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        self.setLayout(layout)
        
    def start(self):
        self.controler.game()
        self.start_button.setEnabled(False)
        
    def refresh(self):
        pass       
    
    
class labelGameState(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)
        self.game_state = QTextEdit()
        self.game_state.setPlainText("White's turn")
        layout=QVBoxLayout()
        layout.addWidget(self.game_state)
        self.setLayout(layout)         
        
    def refresh(self):
        s = self.controler.giveHistoryString()
        if self.controler.time == 0:
            if self.controler.result:
                self.game_state.setPlainText(self.controler.string_result)
            else:
                player = self.controler.board.who_plays
                if player == 'w':
                    self.game_state.setPlainText(f"White's turn\n{s}")
                else:
                    self.game_state.setPlainText(f"Black's turn\n{s}") 
        else:
            if self.controler.time == 1:
                self.game_state.setPlainText(f"Blacks win on time\n{s}")
            else:
                self.game_state.setPlainText(f"Whites win on time\n{s}")
            
class ChessTimer(QWidget):
    
    def __init__(self,parent,controler):
        super().__init__(parent) 
        self.setStyleSheet('font-size: 10pt; font-family: ArialBlack;')
        self.controler = controler 
        self.controler.addClient(self)
        self.label = QLabel('Label')
        layout=QVBoxLayout()
        layout2=QVBoxLayout()
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.time = QTime(0, self.controler.timeMAX, 0)
        self.label2 = QLabel('Label2')
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.showTime2)
        self.time2 = QTime(0, self.controler.timeMAX, 0)
        self.editDesign()
        layout2.addWidget(self.label2)
        layout.addWidget(self.label)
        layout_time = QVBoxLayout()
        layout_time.addLayout(layout2)
        layout_time.addLayout(layout)                  
        self.startTimer()
        self.showTime()   
        self.showTime2()         
        self.setLayout(layout_time)
    
    def editDesign(self):
        font = QFont('Arial', 12, QFont.Bold)
        self.label.setFont(font)
        self.label2.setFont(font)
        
    def showTime(self):        
        self.time = self.time.addSecs(-1)
        timeDisplay = self.time.toString('mm:ss')
        self.label.setText(timeDisplay)
        if timeDisplay == '00:00':
            self.controler.time = 1
            self.endTimer()
            self.controler.game()
            
    def showTime2(self):
        self.time2 = self.time2.addSecs(-1)
        timeDisplay2 = self.time2.toString('mm:ss')
        self.label2.setText(timeDisplay2)
        if timeDisplay2 == '00:00':
            self.controler.time = 2
            self.endTimer2()
            self.controler.game()

    def startTimer(self):
        self.timer.start(1000)

    def endTimer(self):
        self.timer.stop()
    
    def startTimer2(self):
        self.timer2.start(1000)
        
    def endTimer2(self):
        self.timer2.stop()        
    
    def refresh(self):
        if self.controler.time == 0:
            if not self.controler.result:        
                if self.controler.turn == 'w':
                    self.startTimer()
                    self.endTimer2()
                    self.showTime()
                if self.controler.turn == 'b':
                    self.endTimer()
                    self.startTimer2()
                    self.showTime2()
            else:
                self.endTimer()
                self.endTimer2()
        
            
            
            
class ChessBoard(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler 
        self.controler.addClient(self)        
        self.layout = QGridLayout()
        self.board()
        self.board_pieces = ChessPieces(self,controler,self.layout)
        if self.controler.user == 'b':
            self.controler.IA_initial_move()
        
        
        
    def square_clicked(self):
        piece = self.sender()
        self.controler.make_move = True
        self.controler.clicked_piece(piece)        
        
    def move(self):
        case = self.sender()
        self.controler.pos = [case.x,case.j]
        self.controler.game()         
        
    def board(self):
        s = 60
        white = QPixmap(s,s)
        white.fill(QColor(Qt.white))
        black = QPixmap(s,s)
        black.fill(QColor(160,82,45))     
        pos_color = QPixmap(s,s)
        pos_color.fill(QColor(131,111,255)) 
        for i in range(8):
            for j in range(8):                
                if (i + j) % 2 == 0:
                    square = ClickableLabel() 
                    square.clicked.connect(self.square_clicked)             
                    square.setPixmap(white)
                    square.x = -1
                    square.j = -1
                    square.type = 's'
                    self.layout.addWidget(square, i, j)
                else:
                    square = ClickableLabel() 
                    if self.controler.game_type < 3:
                        square.clicked.connect(self.square_clicked)                  
                    square.setPixmap(black)  
                    square.x = -1
                    square.j = -1
                    square.type = 's'
                    self.layout.addWidget(square, i, j)                
                for pos in self.controler.selected_moves_geo:
                    square = ClickableLabel() 
                    if self.controler.game_type < 3:
                        square.clicked.connect(self.move)                 
                    square.setPixmap(pos_color)                    
                    square.j = pos[1]
                    square.x = pos[0]                    
                    square.type = 's'
                    if self.controler.user == 'w':
                        self.layout.addWidget(square, 7-pos[1], pos[0])
                    else:
                        self.layout.addWidget(square, pos[1], pos[0])
        self.setLayout(self.layout)    
    
    def delete_piece(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)
            if len(self.layout) < 65:
                break
        
        
    def refresh(self):
        self.delete_piece()
        self.board()
        
        
        
class ChessPieces(QWidget):
    
    def __init__(self, parent, controler,layout):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)
        self.layout = layout
        self.pieces()          
        
    def piece_clicked(self):         
        piece = self.sender()
        if self.controler.make_move == False:
            self.controler.clicked_piece(piece)
        else:
            if coordinates.reconvert_to_alg([piece.j,7-piece.x]) in \
                self.controler.selected_moves_alg:
                    self.controler.pos = [piece.j,7-piece.x]
                    self.controler.game()
            else:
                self.controler.make_move = False
                self.controler.clicked_piece(piece)
                
    def pieces(self):
        s = 60
        piece_map = self.controler.give_map() 
        if self.controler.user == 'w':        
            for x in range(8):
                l = piece_map[7-x]
                j = 0
                for y in l:
                    if y is not None:
                        piece = ClickableLabel()
                        if self.controler.game_type < 3:
                            piece.clicked.connect(self.piece_clicked)
                        piece_type = inter_fun.add_piece(y.name)                                      
                        piece.setPixmap(piece_type.scaled(s,s))
                        piece.x = x
                        piece.j = j
                        piece.type = 'p'                        
                        self.layout.addWidget(piece, x, j)
                    j += 1
        else:
            for x in range(8):
                l = piece_map[x]
                j = 0
                for y in l:
                    if y is not None:
                        piece = ClickableLabel() 
                        if self.controler.game_type < 3:
                            piece.clicked.connect(self.piece_clicked)
                        piece_type = inter_fun.add_piece(y.name)                                      
                        piece.setPixmap(piece_type.scaled(s,s))
                        piece.x = 7 - x
                        piece.j = j   
                        piece.type = 'p'
                        self.layout.addWidget(piece, x, j)
                    j += 1

    def delete_piece(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)
            if len(self.layout) < 65:
                break
    
    def execute_with_delay(self,delay):
        loop = QEventLoop()
        QTimer.singleShot(delay, loop.quit)
        loop.exec_()
        
    def refresh(self):
        self.pieces()        

class SaveFile(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self. save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_data)
        layout = QVBoxLayout()
        layout.addWidget(self.save_button)
        self.setLayout(layout)
        self.hist = []
        
    def save_data(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,\
              "QFileDialog.getOpenFileName()", ""," (*.pkl)", options=options)
        self.controler.save(fileName)


class RestartInterface(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self. res_button = QPushButton("Restart")
        self.res_button.clicked.connect(restart)
        layout = QVBoxLayout()
        layout.addWidget(self.res_button)
        self.setLayout(layout)  
        
        
class chessUI(QWidget):

    def __init__(self, parent, controler):
        super().__init__(parent)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.chess_board = ChessBoard(self, controler)
        self.game_state = labelGameState(self,controler)
        if controler.game_type == 2 :         
            self.chess_timer = ChessTimer(self,controler)
        self.save_options = SaveFile(self,controler)
        self.restart_options = RestartInterface(self,controler) 
        vlayout_board = QVBoxLayout()          
        vlayout_board.addWidget(self.chess_board,0)
        vlayout_board.addWidget(self.game_state,1)
        hlayout.addLayout(vlayout_board)          
        vlayout_options = QVBoxLayout()
        vlayout_options.addWidget(self.save_options)
        vlayout_options.addWidget(self.restart_options)        
        if controler.game_type == 3:
            self.start_option = startIAGame(self,controler)
            vlayout_options.addWidget(self.start_option)
        vlayout_options.addStretch(1)
        if controler.game_type == 2:
           vlayout_time = QVBoxLayout() 
           vlayout_time.addWidget(self.chess_timer,0)
           hlayout.addLayout(vlayout_time)        
        hlayout.addLayout(vlayout_options)
        vlayout.addLayout(hlayout,0)        
        self.setLayout(vlayout)
        

class MainWindow(QMainWindow):

    def __init__(self, controler):
        super().__init__()
        self.setStyleSheet('font-size: 10pt; font-family: Courier;')
        self.setWindowTitle("Xadrez")
        self.setWindowIcon(QIcon('./images/bk.png'))
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        self.controler = controler
        status_bar.showMessage('Xadrez version 1.0')         
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
        self.setGeometry(300, 35, 500, 200)
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
        self.load = QComboBox()
        load_label = QLabel("Load a game?")
        self.load.addItems(['No','Yes'])
        self.load.currentTextChanged.connect(\
                                              self.loadFile)
        self.layout.addWidget(IA_level_label)
        self.layout.addWidget(self.IA_level)
        self.layout.addWidget(User_team_label)
        self.layout.addWidget(self.User_team) 
        self.layout.addWidget(load_label)
        self.layout.addWidget(self.load)
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
    
    def change_time(self):
        self.controler.timeMAX = int(self.time_max.currentText())
    
    def player_vs_player(self):
        self.time_max = QComboBox()
        self.time_max.addItems(['1','3','5','10','30'])
        self.time_max.currentTextChanged.connect(\
                                              self.change_time)
        time_max_label = QLabel("Game Time (minutes)")
        self.load = QComboBox()
        load_label = QLabel("Load a game?")
        self.load.addItems(['No','Yes'])
        self.load.currentTextChanged.connect(\
                                              self.loadFile)
        self.layout.addWidget(time_max_label)
        self.layout.addWidget(self.time_max)
        self.layout.addWidget(load_label)
        self.layout.addWidget(self.load)
        self.start_button.setParent(None)
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)        
    
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
    
    def loadFile(self):
        if self.load.currentText() == 'Yes':
            options = QFileDialog.Options()
            try:
                fileName, _ = QFileDialog.getOpenFileName(self,\
                  "QFileDialog.getOpenFileName()", ""," (*.pkl);;Python Files (*.py)", options=options)
                self.controler.load(fileName)
            except:
                pass
    
def main():
    app = QApplication(sys.argv)
    controler = Controler()
    win = MainWindow(controler)   
    win.show()
    app.exec()
    
    
if __name__ == '__main__':
    main()