import numpy as np
import random 
import datetime 
import os 
import copy

import pieces as pcs
import pawn as p
import rook as r
import knight as n
import bishop as b
import queen as q
import king as k
import coordinates 
import datetime
import os

def is_empty(l):
    
    ''' 
    
    Parameters
    ----------
    l : list containin a piece and its possible movements

    Returns True is empty 
    -------
   

    '''
    return           

    
        

def convert_notation(move): 
    move=move.split('_')
    piece=move[0][1]
    debut=move[1]
    fin=move[2]
    if piece == 'p':
        piece=''
    else:
        piece= piece.upper() 
    return piece+debut+fin
        

def convert_pgn(moves):
    myDate=datetime.datetime.now()
    name_of_file=myDate.strftime('%Y_%m_%d_%H_%M_%S')
    path=os.getcwd()+'\\parties\\'
    f=open(path+name_of_file+'txt','w')
    i=1
    count=0
    for move in moves:
        move2=convert_notation(move)
        if count%2 == 0:
            f.write(str(i)+move2+' ')
            count+=1
        else:
            f.write(move2+'\n')
            count+=1
            i=i+1
    f.close()

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
        self.actual_board()  
        self.dead_pieces=[] #dead pieces
        
    def actual_board(self): #put actual pieces in board 
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
    
    
    def move(self,possible_moves):
        
        l1 = []
        
        
        if is_empty(possible_moves):
            return possible_moves
        else:
            
            if self.who_plays == 'w':
                pieces_board = self.whites_in_board
                king = self.w_king
                self.who_plays = 'b'
            else:
                pieces_board = self.blacks_in_board
                king = self.b_king
                self.who_plays = 'w'
            
            valid = False
            while not valid:
                l = random.choice(possible_moves)
                piece = l[0]
                if len(l[1]) > 0:
                    valid = True
                    
            movement = random.choice(l[1])
            
            l[1].remove(movement)
            
            movement_xy = coordinates.convert_to_coordinate(movement)
            x = movement_xy [0]
            y = movement_xy [1]
            
            if piece in pieces_board:
                print(f"{piece} to {movement}")
                idx = pieces_board.index(piece)
                pieces_board[idx].pos_alg = movement
                if piece == king:
                    king.pos_alg = movement
                if self.board_map[y][x] is not None:
                    print(self.board_map[y][x],pieces_board)
                    pieces_board.remove(self.board_map[y][x])
                    print(f"{self.board_map[y][x]} eliminated at \
                          {movement}")
                
            
            return possible_moves
    
    def simulate_check(self,possible_moves):
        return
    
    
    
    def game(self):
        '''
        Simulation of a game 

        Returns
        -------
        None.

        '''
        
        
        i = 0
        
        while  i < 200:
            
            l1 = self.possible_moves()
            l1 = self.move(l1)
            
            l2 = self.possible_moves()
            
            if self.who_plays == 'w':
                king = self.w_king
            else:
                king = self.b_king
            
            if king.is_checked(l1):
                
                l3 = self.simulate_check(l2)
                
                if is_empty(l3):
                    print(f"Check mate at {king}")
                    return
                else:
                    l3 = self.move(l3)
            else:
                l2 = self.move(l2)
                
            i += 1
        

 
if __name__ == "__main__":
    b = Board()
    b.game()
    

