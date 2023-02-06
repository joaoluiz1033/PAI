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
        self.history = [] #history of moves
        self.who_plays = 'w' # who is playing 
        self.current_board()
    
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
    
    def historyToString(self):
        L = (len(self.history))
        s = ''
        aux = 1
        for i in range(L):
            j = i + 1;
            if j%2 != 0:
               s += str(aux) +' '
               aux += 1
            s += self.history[i] + ' '
        return s
               
    def numberOfPieces(self):
        L = len(self.whites_in_board) + len(self.blacks_in_board)
        if L <= 3:
            if L < 3:
                return L,True
            else:
                for piece in self.whites_in_board:
                    if piece.name[1] == 'n':
                        return L,True
                for piece in self.blacks_in_board:
                    if piece.name[1] == 'n':
                        return L,True
        return L,False
        
if __name__ == "__main__":
    b = Board()