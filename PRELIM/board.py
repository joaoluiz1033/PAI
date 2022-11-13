
import numpy as np

import pieces as pcs
import coordinates 

class Board():
    
    def __init__(self):   #initial board with all pieces in position      
        self.board_map = [ [ None for x in range(8) ] for y in range(8)] #board to display
        #defining whites
        self.whites_in_board = [pcs.pieces('wr','a1'), pcs.pieces('wn','b1'), 
                                pcs.pieces('wb','c1'), pcs.pieces('wq', 'd1'),
                                pcs.pieces('wk','e1'), pcs.pieces('wb','f1'),
                                pcs.pieces('wn','g1'), pcs.pieces('wr','h1'),
                                pcs.pieces('wp','a2'), pcs.pieces('wp','b2'),
                                pcs.pieces('wp','c2'), pcs.pieces('wp','d2'),
                                pcs.pieces('wp','e2'), pcs.pieces('wp','f2'),
                                pcs.pieces('wp','g2'), pcs.pieces('wp','h2')] 
        
        #defining blacks
        self.blacks_in_board = [pcs.pieces('br','a8'), pcs.pieces('bn','b8'), 
                                pcs.pieces('bb','c8'), pcs.pieces('bq', 'd8'),
                                pcs.pieces('bk','e8'), pcs.pieces('bb','f8'),
                                pcs.pieces('bn','g8'), pcs.pieces('br','h8'),
                                pcs.pieces('bp','a7'), pcs.pieces('bp','b7'),
                                pcs.pieces('bp','c7'), pcs.pieces('bp','d7'),
                                pcs.pieces('bp','e7'), pcs.pieces('bp','f7'),
                                pcs.pieces('bp','g7'), pcs.pieces('bp','h7')]       
    
        self.dead_pieces = [] #dead pieces 
            
    def actual_board(self): #put actual pieces in board 
        for pic in self.whites_in_board: #putting whites in board to display
            
            if pic is not None:
                coord = coordinates.convert_to_coordinate(pic.pos_alg)
                self.board_map[coord[1]][coord[0]] = pic.name
            
        for pic in self.blacks_in_board: #putting black in board to display
            if pic is not None:
                coord = coordinates.convert_to_coordinate(pic.pos_alg)
                self.board_map[coord[1]][coord[0]] = pic.name
    
    def prt(self): # print board 
        self.actual_board()
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
        
    def move(self,P,m1): 
        #  move piece P in the board 
        team = P.name[0]
        if team == 'w':
            l = self.whites_in_board
        else:
            l = self.blacks_in_board
        idx = l.index(P)
        l[idx].move(m1)
        
 
if __name__ == "__main__":
    b = Board()
    #b.remove_piece(pcs.pieces('wr','a1'))
    #b.prt()
    b.move(pcs.pieces('wp','a2'),'a3')
    b.prt()

                  
   
        
     
        
        
        
        