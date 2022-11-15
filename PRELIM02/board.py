
import numpy as np
import random 

import pieces as pcs
import pawn as p
import rook as r
import knight as n
import bishop as b
import queen as q
import king as k
import coordinates 

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
        
        #defining blacks
        self.blacks_in_board = [r.rook('br','a8'), n.knight('bn','b8'), 
                                b.bishop('bb','c8'), q.queen('bq', 'd8'),
                                k.king('bk','e8'), b.bishop('bb','f8'),
                                n.knight('bn','g8'), r.rook('br','h8'),
                                p.pawn('bp','a7'), p.pawn('bp','b7'),
                                p.pawn('bp','c7'), p.pawn('bp','d7'),
                                p.pawn('bp','e7'), p.pawn('bp','f7'),
                                p.pawn('bp','g7'), p.pawn('bp','h7')]       
    
        self.dead_pieces = [] #dead pieces 
        self.who_plays = 'w' # who is playing 
        self.actual_board()    
        
    def actual_board(self): #put actual pieces in board 
        self.board_map = [ [ None for x in range(8) ] for y in range(8)]
        for pic in self.whites_in_board: #putting whites in board to display
            
            if pic is not None:
                coord = coordinates.convert_to_coordinate(pic.pos_alg)
                self.board_map[coord[1]][coord[0]] = pic.name
            
        for pic in self.blacks_in_board: #putting black in board to display
            if pic is not None:
                coord = coordinates.convert_to_coordinate(pic.pos_alg)
                self.board_map[coord[1]][coord[0]] = pic.name
        
    def prt(self): # print board 
        
        for x in range(8):
            l = self.board_map[7-x]
            for y in l:
                
                if y == None:
                    print('.  ',end='')
                else:
                    print(y+' ',end='')                
            print('\n')
        return 
    
    def remove_piece(self,P): 
        #remove a single piece from board 
        #P is the piece to be removed
        
        team = P.name[0] 
        if team == 'w':
            l = self.whites_in_board
        else:
            l = self.blacks_in_board
        a = P in l #cheking if the piece is in place
        if a == True :
            idx = l.index(P)
            self.dead_pieces.append(P)
            l[idx] = None
        
    def move(self,l): 
#this function moves pieces in board
# l = list of possible movements 
        
        team = self.who_plays #white or black 
        valid = False
        a = random.choice(l) #piece that is going to move
        while valid == False:
            if len(a[1]) != 0:
                p = a[0] #piece
                b = random.choice(a[1]) #random choice from possible moves
                valid = True
            else:
                a = random.choice(l)
        
        if team == 'w':
            if p in self.whites_in_board:
                p.pos_alg = b
            self.who_plays = 'b'
        else:
            if p in self.blacks_in_board:
                p.pos_alg = b  
            self.who_plays = 'w'
        
        self.actual_board()
        
                
        
        
    def round_moves(self):
        # all possible movements 
        if self.who_plays == 'w':
            l_pieces = self.whites_in_board
        else:
            l_pieces = self.blacks_in_board
        
        l_move_poss = []
        
        for P in l_pieces: 
            l_move_poss.append([P,P.check_moves(self.board_map)])
            
        return l_move_poss
            
 
if __name__ == "__main__":
    b = Board()
    #b.remove_piece(pcs.pieces('wr','a1'))
   #b.prt()
    i = 1    
    while i < 5:
        print(f"\n---------rodada {i}----------\n")
        l = b.round_moves()
        
        b.move(l)
        
        l = b.round_moves()
        
        b.move(l)
        
        i += 1
        
        b.prt()
    

    

                  
   
        
     
        
        
        
        