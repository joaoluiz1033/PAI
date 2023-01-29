import numpy as np
import random 
import datetime 
import os 
import copy
import pdb
import string

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

class Board():
    
    def __init__(self):   #initial board with all pieces in position      
        self.board_map = [ [ None for x in range(8) ] for y in range(8)] #board to display
        #defining whites
        self.whites_in_board = [r.rook('wr','a1'), n.knight('wn','b1'), 
                                b.bishop('wb','c1'), q.queen('wq', 'd1'),
                                k.king('wk','e1'), b.bishop('wb','f1'),
                                n.knight('wn','g1'), r.rook('wr','h1'),
                                p.pawn('wp','a2'), p.pawn('wp','b2'),
                                p.pawn('wp','c2'), p.pawn('wp','d2'),
                                p.pawn('wp','e2'), p.pawn('wp','f2'),
                                p.pawn('wp','g2'), p.pawn('wp','h2')] 
        
        self.w_king = k.king('wk','e1')
        #defining blacks
        self.blacks_in_board = [r.rook('br','a8'), n.knight('bn','b8'), 
                                b.bishop('bb','c8'), q.queen('bq', 'd8'),
                                k.king('bk','e8'), b.bishop('bb','f8'),
                                n.knight('bn','g8'), r.rook('br','h8'),
                                p.pawn('bp','a7'), p.pawn('bp','b7'),
                                p.pawn('bp','c7'), p.pawn('bp','d7'),
                                p.pawn('bp','e7'), p.pawn('bp','f7'),
                                p.pawn('bp','g7'), p.pawn('bp','h7')]       

        self.b_king = k.king('bk','e8')        

        self.dead_pieces = [] #dead pieces 
    
        self.history = [] #history of moves
        self.who_plays = 'w' # who is playing 
        self.current_board()  
        self.dead_pieces=[] #dead pieces
        self.lat_mov = 'None'
    
    def current_board(self): #put actual pieces in board 
        self.board_map = [ [ None for x in range(8) ] for y in range(8)]
        for pic in self.whites_in_board: #putting whites in board to display
            
            if pic is not None:
                coord = coordinates.convert_to_coordinate(pic.pos_alg)
                self.board_map[coord[1]][coord[0]] = pic
            
        for pic in self.blacks_in_board: #putting black in board to display
            if pic is not None:
                coord = coordinates.convert_to_coordinate(pic.pos_alg)
                self.board_map[coord[1]][coord[0]] = pic
        
    
    def prt(self): # print board         
        for x in range(8):
            l = self.board_map[7-x]
            for y in l:                
                if y == None:
                    print('.  ',end='')
                else:
                    print(y.name+' ',end='')                
            print('\n')
        return 
    
    def prt_silenced(self): # print board 
        s = []
        s.append('\t')
        for x in range(8):
            l = self.board_map[7-x]
            for y in l:                
                if y == None:
                    s.append('.  ')
                else:
                    s.append(y.name+' ')                
            s.append("\n\t")
        s = ''.join(s)
        return s
    
    def possible_moves(self):
        '''
        this function goes to the white/black list of pieces in board
        and return all possible moves for each of those pieces
        it calls all pieces classes (queen, king, rook, ...)

        Returns
        -------
        list of possible moves

        '''
        if self.who_plays == 'w':
            l_pieces = self.whites_in_board
            
        else:
            l_pieces = self.blacks_in_board
            
        l_move_poss = []
        
        for P in l_pieces: 
            l_move_poss.append([P,P.check_moves(self.board_map)])
            

        return l_move_poss
    
    def change_pawn(self, position ,pieces_in_board, pawn_idx,team):        
        a = team        
        pieces = [q.queen(a+'q', position),n.knight(a+'n',position),b.bishop(a+'b', position),r.rook(a+'r',position)]
        p = random.choice(pieces)        
        pieces_in_board[pawn_idx] = p
        self.history[-1] += '=Q'        
        return [p,p.check_moves(self.board_map)]
    
    def register_en_passant(self,x,y,piece,add,enemies_board):        
        X_MIN = 0
        X_MAX = 7            
        if x == X_MIN:
            if self.board_map[y][x+1] is not None:                    
                if self.board_map[y][x+1].name[1] == 'p' and \
                    self.board_map[y][x+1].name[0] != self.who_plays:
                        x_pass = x 
                        y_pass = y - add
                        for enemy_p in enemies_board:
                            if enemy_p == self.board_map[y][x+1]:
                                enemy_p.en_passante_moves.append(\
                        coordinates.reconvert_to_alg([x_pass,y_pass]))
        elif x == X_MAX:
            if self.board_map[y][x-1] is not None:                    
                if self.board_map[y][x-1].name[1] == 'p' and \
                    self.board_map[y][x-1].name[0] != self.who_plays:
                        x_pass = x 
                        y_pass = y - add
                        
                        for enemy_p in enemies_board:
                            if enemy_p == self.board_map[y][x-1]:
                                enemy_p.en_passante_moves.append(\
                        coordinates.reconvert_to_alg([x_pass,y_pass]))
        else:            
            if self.board_map[y][x+1] is not None:                    
                if self.board_map[y][x+1].name[1] == 'p' and \
                    self.board_map[y][x+1].name[0] != self.who_plays:
                        x_pass = x 
                        y_pass = y - add                        
                        for enemy_p in enemies_board:
                            if enemy_p == self.board_map[y][x+1]:
                                enemy_p.en_passante_moves.append(\
                        coordinates.reconvert_to_alg([x_pass,y_pass]))                        
            if self.board_map[y][x-1] is not None:                    
                if self.board_map[y][x-1].name[1] == 'p' and \
                    self.board_map[y][x-1].name[0] != self.who_plays:
                        x_pass = x
                        y_pass = y - add
                        for enemy_p in enemies_board:
                            if enemy_p == self.board_map[y][x-1]:
                                enemy_p.en_passante_moves.append(\
                        coordinates.reconvert_to_alg([x_pass,y_pass]))
        return
    
    def change_who_plays(self):
        if self.who_plays == 'w':
            self.who_plays = 'b'
        else:
            self.who_plays = 'w'
        return self.who_plays
    
    def move_choose(self,l_possible_moves):        
        a = False       
        if is_empty(l_possible_moves):
            return l_possible_moves
        else:            
            if self.who_plays == 'w':
                pieces_board = self.whites_in_board
                enemies_board = self.blacks_in_board
                king = self.w_king
                add = 1
            else:
                pieces_board = self.blacks_in_board
                enemies_board = self.whites_in_board
                king = self.b_king
                add = -1                
            valid = False
            while not valid:
                i = 0
                for l in l_possible_moves:
                    print(i,l)
                    i += 1
                l = input("Choose a piece (its number): ")   
                l = int(l)
                idx_pawn = l_possible_moves[l]
                piece = l_possible_moves[l][0]
                if len(l_possible_moves[l][1]) > 0:
                    valid = True            
            for s in l_possible_moves[l][1]:
                print(s)                  
            movement = input('Choose a movement: ')      
            movement_xy = coordinates.convert_to_coordinate(movement)
            x = movement_xy [0]
            y = movement_xy [1]            
            old_xy = coordinates.convert_to_coordinate(piece.pos_alg)
            old_y = old_xy[1]
            old_x = old_xy[0]                        
            if piece in pieces_board:                               
                if self.board_map[y][x] is not None:                    
                    if self.board_map[y][x].name[1] == 'k':
                        return [] 
                    try:
                        enemies_board.remove(self.board_map[y][x])
                    except:
                        pdb.set_trace()                    
                else:
                    if piece.name[1] == 'p':
                        if abs(old_x - x) != 0:                            
                            enemies_board.remove(self.board_map[y-add][x]) 
                    elif  piece.name[1] == 'k' and abs(x - old_x) == 2:
                        if x > old_x:
                            idx_rook = self.find_rook(pieces_board, 1)
                            rook_pos = coordinates.reconvert_to_alg([x-1,y])
                            pieces_board[idx_rook].pos_alg = rook_pos
                        else:
                            idx_rook = self.find_rook(pieces_board, -1) 
                            rook_pos = coordinates.reconvert_to_alg([x+1,y])
                            pieces_board[idx_rook].pos_alg = rook_pos
                idx = pieces_board.index(piece)
                pieces_board[idx].pos_alg = movement
                piece.history_mov.append(movement)                
                self.last_movement = movement
                l_possible_moves[l][1].remove(movement)
                if piece.name[1] == 'k':
                    king.pos_alg = movement          
                if piece.name[1] == 'p':                   
                    if pieces_board[idx].at_max():                        
                        new_l = self.change_pawn(movement,pieces_board,\
                          idx,pieces_board[idx].team )                           
                        l_possible_moves[idx_pawn] = new_l                  
                    elif abs(old_y - y) == 2:                        
                        self.register_en_passant(x,y,piece,add,enemies_board)
            self.current_board()
            l_possible_moves = self.possible_moves()           
            if a:
                return []
            else:
                return l_possible_moves
    
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
        if self.who_plays == 'w':
            pieces_board = self.whites_in_board
            enemies_board = self.blacks_in_board
            king = self.w_king
            add = 1
            self.who_plays = 'b'            
        else:
            pieces_board = self.blacks_in_board
            enemies_board = self.whites_in_board
            king = self.b_king
            add = -1
            self.who_plays = 'w'            
        movement_xy = coordinates.convert_to_coordinate(movement)
        x = movement_xy [0]
        y = movement_xy [1]        
        old_xy = coordinates.convert_to_coordinate(piece.pos_alg)
        old_y = old_xy[1]
        old_x = old_xy[0]               
        if piece in pieces_board:                                
            if self.board_map[y][x] is not None:
                if old_x != x:
                    enemies_board.remove(self.board_map[y][x])     
            else:
                if piece.name[1] == 'p':
                    if abs(old_x - x) != 0:                        
                        enemies_board.remove(self.board_map[y-add][x])
            idx = pieces_board.index(piece)
            pieces_board[idx].pos_alg = movement            
            if piece.name[1] == 'k':
                king.pos_alg = movement  
        self.current_board()  
        return
    
    def test_roque(self,current_x,movement_x,y,piece):        
        if current_x > movement_x:
            add = -1
        else:
            add = 1            
        while(current_x != movement_x):
            movement = coordinates.reconvert_to_alg([current_x,y])
            l_enemy_moves = self.possible_moves()            
            if piece.is_checked(l_enemy_moves):
                return False
            current_x += add            
        movement = coordinates.reconvert_to_alg([current_x,y])
        l_enemy_moves = self.possible_moves()
        if piece.is_checked(l_enemy_moves):
            return  False
        else:
            return True
    
    def simulate_check(self,l_possible_moves):        
        valid_list = []
        for pair in l_possible_moves:
            piece = pair[0]
            piece_movements = pair[1]
            piece_valid_movements = []            
            for movement in piece_movements:
                test_board = copy.deepcopy(self)
                if test_board.who_plays == 'w':
                    king = test_board.w_king
                else:
                    king = test_board.b_king
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
        while not end_game and i <1000: 
            self.prt()
            if self.who_plays == 'w':
                king = self.w_king
            else:
                king = self.b_king                 
            l_possible_moves = self.possible_moves()            
            l_valid_moves = self.simulate_check(l_possible_moves)                   
            if is_empty(l_valid_moves):
                if king.is_checked(l_enemy_moves):
                    print(f"Check Mate: {king}")
                else:                    
                    print(f"{self.who_plays} cannot move")                    
                end_game = True
            else:
                if self.who_plays == 'w':
                    l_enemy_moves = self.move_choose(l_valid_moves)
                else:
                    l_enemy_moves = chMV.moveIA_view(self,\
                                  2,l_valid_moves,l_enemy_moves)
                l_enemy_moves = self.simulate_check(l_enemy_moves)
                self.change_who_plays()            
            i += 1       
        if end_game:            
            return
        else:            
            print('Maximum iteration number')

    def show_valid_moves(self):
        l_possible_moves = self.possible_moves()            
        l_valid_moves = self.simulate_check(l_possible_moves)
        return l_valid_moves
    
    
    def move_User(self,l_possible_moves,piece,movement):
        return chMV.move_piece_view(self, l_possible_moves, piece, movement)
    
    def move_IA(self, level, l_possible_moves, l_enemy_moves):
        return chMV.moveIA_view(self,level,l_possible_moves,l_enemy_moves)        
        
            
                       
if __name__ == "__main__":
    l = ['wpe4', 'bpa6', 'wbc4', 'bpa5', 'wqf3', 'bpa4', 'wqf7']   
    l_new = []
    print(l)
    
     
    

