import numpy as np
import random 
import datetime 
import os 
import copy
import pdb
import string
import matplotlib.pyplot as plt
import pickle

from matplotlib.ticker import MaxNLocator

import board as bd
import pieces as pcs
import pawn as p
import rook as r
import knight as n
import bishop as b
import queen as q
import king as k
import coordinates
import chess_IA as chIA
import chess_move as chMV

def save(fileName,vector,vector2):   
    try:
        f = open(fileName, 'wb')
        pickle.dump([vector,vector2], f)
        f.close()
        f = open(fileName, 'rb')
        obj = pickle.load(f)
        f.close()    
    except:
        pass
    
def debug_trace():
    from PyQt5.QtCore import pyqtRemoveInputHook
    from pdb import set_trace
    pyqtRemoveInputHook()
    set_trace()

def is_empty(l): 
    i = 0
    if len(l) == 0 or l is None:
        return True
    else:        
        for x in l:                        
            piece = x[0]
            movements = x[1]
            if len(movements) == 0:
                i += 1
        if i == len(l):            
            return True
        else: 
            return False       

class Game():
    
    def __init__(self,board: bd.Board):   #initial board with all pieces in position      
        self.board = board  
        self.l_enemy_moves = []
        self.l_valid_moves = []
        self.l_possible_moves = []
    
    def possible_moves(self):
        if self.board.who_plays == 'w':
            l_pieces = self.board.whites_in_board            
        else:
            l_pieces = self.board.blacks_in_board            
        l_move_poss = []        
        for P in l_pieces: 
            l_move_poss.append([P,P.check_moves(self.board.board_map)])          
        return l_move_poss
    
    def change_pawn(self, position ,pieces_in_board, pawn_idx,team):        
        a = team
        pieces = [q.queen(a+'q', position)]
        p = pieces[0]        
        pieces_in_board[pawn_idx] = p
        self.board.history[-1] += '=Q'   
        self.board.current_board()
        return [p,p.check_moves(self.board.board_map)]
    
    def register_en_passant(self,x,y,piece,add,enemies_board):        
        X_MIN = 0
        X_MAX = 7            
        if x == X_MIN:
            if self.board.board_map[y][x+1] is not None:                    
                if self.board.board_map[y][x+1].name[1] == 'p' and \
                    self.board.board_map[y][x+1].name[0] != self.board.who_plays:
                        x_pass = x 
                        y_pass = y - add
                        for enemy_p in enemies_board:
                            if enemy_p == self.board.board_map[y][x+1]:
                                enemy_p.en_passante_moves.append(\
                        coordinates.reconvert_to_alg([x_pass,y_pass]))
        elif x == X_MAX:
            if self.board.board_map[y][x-1] is not None:                    
                if self.board.board_map[y][x-1].name[1] == 'p' and \
                    self.board.board_map[y][x-1].name[0] != self.board.who_plays:
                        x_pass = x 
                        y_pass = y - add                        
                        for enemy_p in enemies_board:
                            if enemy_p == self.board.board_map[y][x-1]:
                                enemy_p.en_passante_moves.append(\
                        coordinates.reconvert_to_alg([x_pass,y_pass]))
        else:            
            if self.board.board_map[y][x+1] is not None:                    
                if self.board.board_map[y][x+1].name[1] == 'p' and \
                    self.board.board_map[y][x+1].name[0] != self.board.who_plays:
                        x_pass = x 
                        y_pass = y - add                        
                        for enemy_p in enemies_board:
                            if enemy_p == self.board.board_map[y][x+1]:
                                enemy_p.en_passante_moves.append(\
                        coordinates.reconvert_to_alg([x_pass,y_pass]))                        
            if self.board.board_map[y][x-1] is not None:                    
                if self.board.board_map[y][x-1].name[1] == 'p' and \
                    self.board.board_map[y][x-1].name[0] != self.board.who_plays:
                        x_pass = x
                        y_pass = y - add
                        for enemy_p in enemies_board:
                            if enemy_p == self.board.board_map[y][x-1]:
                                enemy_p.en_passante_moves.append(\
                        coordinates.reconvert_to_alg([x_pass,y_pass]))
        return
    
    
    def change_who_plays(self):
        if self.board.who_plays == 'w':
            self.board.who_plays = 'b'
        else:
            self.board.who_plays = 'w'
        return self.board.who_plays
    
        
    def find_rook(self,pieces_board,direction):        
        idx = 0        
        if direction == 1:
            x_ref = 7
        else:
            x_ref = 0
        for piece in pieces_board:
            idx = pieces_board.index(piece)
            if piece.name[1] == 'r':
                x = coordinates.convert_to_coordinate(piece.pos_alg)[0]
                if x == x_ref:
                    return idx       
        return idx        
            
    def move_piece(self, piece, movement):
        if self.board.who_plays == 'w':
            pieces_board = self.board.whites_in_board
            enemies_board = self.board.blacks_in_board
            king = self.board.w_king
            add = 1
            self.board.who_plays = 'b'            
        else:
            pieces_board = self.board.blacks_in_board
            enemies_board = self.board.whites_in_board
            king = self.board.b_king
            add = -1
            self.board.who_plays = 'w'            
        movement_xy = coordinates.convert_to_coordinate(movement)
        x = movement_xy [0]
        y = movement_xy [1]        
        old_xy = coordinates.convert_to_coordinate(piece.pos_alg)
        old_y = old_xy[1]
        old_x = old_xy[0]           
        if piece in pieces_board:                                
            if self.board.board_map[y][x] is not None and \
            self.board.board_map[y][x].name[0] != piece.name[0]:
                if self.board.board_map[y][x].name[1] == 'k':
                    return []  
                try:
                    enemies_board.remove(self.board.board_map[y][x])
                    eliminate = True 
                except:
                    debug_trace()                    
            else:                
                if piece.name[1] == 'p':
                    if abs(old_x - x) != 0:                            
                        enemies_board.remove(self.board.board_map[y-add][x])
                        eliminated = True  
            idx = pieces_board.index(piece)
            pieces_board[idx].pos_alg = movement            
            if piece.name[1] == 'k':
                king.pos_alg = movement                        
        self.board.current_board()  
        return
    
    def test_roque(self,current_x,movement_x,y,piece):  
        originalX = current_x
        self.change_who_plays()
        if current_x > movement_x:
            add = -1
        else:
            add = 1
        posRook = coordinates.reconvert_to_alg([movement_x+add,y])
        pieceRook = r.rook(piece.name[0]+'r',posRook)
        self.board.board_map[y][movement_x+add] = None
        self.board.board_map[y][current_x] = None
        while(current_x != movement_x): 
            self.board.board_map[y][current_x] = piece
            movement = coordinates.reconvert_to_alg([current_x,y])
            l_enemy_moves = self.possible_moves()
            pieceCopy = copy.deepcopy(piece)
            pieceCopy.pos_alg = movement
            if pieceCopy.is_checked(l_enemy_moves):
                self.board.board_map[y][current_x] = piece
                return False
            self.board.board_map[y][current_x] = None
            current_x += add
        self.board.board_map[y][current_x] = piece
        movement = coordinates.reconvert_to_alg([current_x,y])
        l_enemy_moves = self.possible_moves()
        pieceCopy = copy.deepcopy(piece)
        pieceCopy.pos_alg = movement
        if pieceCopy.is_checked(l_enemy_moves):
            self.board.board_map[y][originalX] = piece
            self.board.board_map[y][movement_x+add] = pieceRook
            return False
        self.board.board_map[y][current_x] = None
        self.board.board_map[y][movement_x+add] = pieceRook
        self.board.board_map[y][originalX] = piece
        return True
    
    def simulate_check(self,l_possible_moves):                
        valid_list = []
        for pair in l_possible_moves:
            piece = pair[0]
            piece_movements = pair[1]
            piece_valid_movements = []
            for movement in piece_movements:
                if piece.pos_alg != movement:
                    test_board = copy.deepcopy(self)
                    if test_board.board.who_plays == 'w':
                        king = test_board.board.w_king
                    else:
                        king = test_board.board.b_king
                    if piece.name[1] != 'k':                    
                        test_board.move_piece(piece, movement)
                        l_enemy_moves = test_board.possible_moves()
                        if not king.is_checked(l_enemy_moves):
                            piece_valid_movements.append(movement)
                    else:                    
                        movement_x = coordinates.convert_to_coordinate(movement)[0]
                        current_x = coordinates.convert_to_coordinate(piece.pos_alg)[0]
                        y =  coordinates.convert_to_coordinate(piece.pos_alg)[1]
                        if abs(movement_x - current_x == 2):
                            valid_roque = test_board.test_roque(current_x,movement_x,y,piece)
                            if valid_roque:
                                piece_valid_movements.append(movement)
                        else:
                            test_board.move_piece(piece, movement)
                            l_enemy_moves = test_board.possible_moves()                
                            if not king.is_checked(l_enemy_moves):
                                piece_valid_movements.append(movement)
            valid_list.append([piece,piece_valid_movements])        
        return valid_list     
    
    def game(self):       
        l_enemy_moves = []        
        end_game = False        
        i = 0
        while not end_game and i <90: 
            print(i)
            L,insuf = self.board.numberOfPieces()
            if insuf:
                print("Draw - Not enough pieces")
                return 2
            if self.board.who_plays == 'w':
                king = self.board.w_king
            else:
                king = self.board.b_king                 
            self.l_possible_moves = self.possible_moves()            
            self.l_valid_moves = self.simulate_check(self.l_possible_moves)                   
            if is_empty(self.l_valid_moves):
                if king.is_checked(self.l_enemy_moves):
                    print(f"Check Mate: {king}")
                    if king.name[0] == 'w':
                        return 1
                    else:
                        return 0
                else:                    
                    print(f"{self.board.who_plays} cannot move")
                    if self.board.who_plays == 'w':
                        return 3
                    else:
                        return 4
                end_game = True
            else:
                if self.board.who_plays == 'w':
                    
                    self.l_enemy_moves = chMV.moveIA_view(self,\
                                  3,self.l_valid_moves,self.l_enemy_moves)
                else:
                    self.l_enemy_moves = chMV.moveIA_view(self,\
                                  1,self.l_valid_moves,self.l_enemy_moves)
                self.l_enemy_moves = self.simulate_check(self.l_enemy_moves)
                self.change_who_plays()            
            i += 1       
        print('Maximum iteration number')
        return 5
    
    
            

    def show_valid_moves(self):
        l_possible_moves = self.possible_moves()            
        l_valid_moves = self.simulate_check(l_possible_moves)
        return l_valid_moves
    
    
    def move_User(self,l_possible_moves,piece,movement):
        return chMV.move_piece_view(self, l_possible_moves, piece, movement)
    
    def move_IA(self, level, l_possible_moves, l_enemy_moves):
        return chMV.moveIA_view(self,level,l_possible_moves,l_enemy_moves)        
        
if __name__ == "__main__":
    tests = 1
    possibleResults = 7
    vecRes =  np.zeros((tests,), dtype=int)
    data = np.zeros((possibleResults,), dtype=int)
    for i in range(tests):
        print(i)
        M = Game(bd.Board())
        try: #erro na chess_IA linha 52
            result = M.game()
            result = np.int32(result)    
            M.board.prt()        
            data[result] += np.int32(1)  
        except:
            data[possibleResults-1] += np.int32(1)
    counts = [0,1,2,3,4,5,6,7]
    save('mediumSimul',range(len(data)),data)

      
        