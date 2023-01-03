import numpy as np
import random 
import datetime 
import os 

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
        
        self.w_king_idx = 4
        #defining blacks
        self.blacks_in_board = [r.rook('br','a8'), n.knight('bn','b8'), 
                                b.bishop('bb','c8'), q.queen('bq', 'd8'),
                                k.king('bk','e8'), b.bishop('bb','f8'),
                                n.knight('bn','g8'), r.rook('br','h8'),
                                p.pawn('bp','a7'), p.pawn('bp','b7'),
                                p.pawn('bp','c7'), p.pawn('bp','d7'),
                                p.pawn('bp','e7'), p.pawn('bp','f7'),
                                p.pawn('bp','g7'), p.pawn('bp','h7')]       

        self.b_king_idx = 4
        

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
    
    def remove_piece(self,P): 
#remove a single piece from board 
#P == Piece to be removed         
        team = P.team
        if team == 'w':
            l = self.whites_in_board
            m_idx = self.w_king_idx
        else:
            l = self.blacks_in_board
            m_idx = self.b_king_idx
        
        if P in l :            
            self.dead_pieces.append(P)
            idx = l.index(P)
            if idx < 4:
                m_idx -= 1
            l.remove(P)
        
    def move(self,l): 
#this function moves pieces in board
#if there is an enemy piece in the final destination
    #the enemy will be eliminated with remove_piece
# l = list of possible movements         

        team = self.who_plays #white or black 
        valid = False
        a = random.choice(l) #piece that is going to move
        while valid == False:
            if len(a[1]) != 0:
                p = a[0] #piece
                pos=p.pos_alg
                b = random.choice(a[1])#random choice from possible moves
                self.history.append(p.name+'_'+pos+'_'+b)
                valid = True
            else:
                a = random.choice(l)
        
        b_coord = coordinates.convert_to_coordinate(b)
        b_x = b_coord[0]
        b_y = b_coord[1]
        
        if team == 'w':
            if p in self.whites_in_board:
                p.pos_alg = b                         
            self.who_plays = 'b'
        else:
            if p in self.blacks_in_board:
                p.pos_alg = b  
            self.who_plays = 'w'
            
        possible_enemy = self.board_map[b_y][b_x]
        if possible_enemy is not None:
            print(f"{possible_enemy} eated by {p}")
            self.remove_piece(possible_enemy) #possible enemy is an enemy
        
        self.actual_board()
        
    # def short_castle(self):
    #     history= self.history
    #     map = self.board_map
    #     valid2=True 
    #     if self.who_plays == 'w' :
    #         no_beetween = ( map[5][1] == None and maps[6][1] == None)
    #         for moves in history:
    #             if 'wra1' in moves or 'wke1' in moves:
    #                 valid2 = False
    #                 break
    #     if self.who_plays == 'b' :
    #         no_beetween=( map[5][7] == None and maps[6][7] == None)
    #         for moves in history:
    #             if 'bra8' in moves or 'bke8' in moves:
    #                 valid2 = False
    #     return no_beetween and valid 2
            
     
                    
                
        
        
    def round_moves(self):
#this function goes to the white/black list of pieces in board
    #and return all possible moves for each of those pieces
#it calls all pieces classes (queen, king, rook, ...)

        if self.who_plays == 'w':
            l_pieces = self.whites_in_board
            
        else:
            l_pieces = self.blacks_in_board
            
        l_move_poss = []
        
        for P in l_pieces: 
            l_move_poss.append([P,P.check_moves(self.board_map)])
            

        return l_move_poss
    
    
    def king_getout_check(self,l_move_king,l_enemies):
#this function verifies if a king can move to get out of check
#l_move_king == all possible moves from king
#l_enemies == all possible enemies moves
        
        for enemies_mov in l_enemies:  #for all enemies \
            #[piece, possible movements]
                for movements in l_move_king: #for the king's \
                    # movement
                        if movements in enemies_mov[1]: 
                            #if possible scape in enemies movement
                            l_move_king.remove(movements) #removing\
                                #king movement (dont get out of check)
    
        return l_move_king
    
    def move_sacrifice(self, l_enemies,l_king,l_move_poss):
#verificar se as posicoes possiveis podem estar entre a peça e rei        
        l = []
        enemies = l_king.checker_pos(l_enemies)
        
        if len(enemies) != 1: #a sacrifice cannot be made
            return []
        else:
            pos = enemies[0] #position of the enemie that puts us in check
            l = coordinates.get_one_to_other(l_king.pos_alg, pos)
        return l
    
    
    def round_check_moves(self,l_enemies):
#this function defines movement when the king is in check and return \
#a list of possible movements. If in check, we verify the possible \
#king movements and if other piece can 'make a sacrifice'
#l_enemies == list of enemies movements
        
        l_move_poss = []        
        l_outof_check = []
        l_sacrifice = []
        if self.who_plays == 'w':
            l_pieces = self.whites_in_board
            m_indx = self.w_king_idx
        else:
            l_pieces = self.blacks_in_board        
            m_indx = self.b_king_idx
        
        l_move_poss = self.round_moves() #all possible moves
        l_king = l_pieces[m_indx] #king in check 
        
        for sublist in l_move_poss: #for all [piece,possible movements]
            if sublist[0] == l_king: #check if piece == king
                l_move_king = sublist[1]
                l_move_poss = self.king_getout_check(l_move_king,l_enemies)
                l_outof_check += [l_king,l_move_poss] 
                
            else: #not king, verifies potential sacrifice
                l_sacrifice = self.move_sacrifice(l_enemies,l_king,l_move_poss)
                l_outof_check += l_sacrifice
                
        return l_outof_check
        
    # def short_castle(self):
    #     history= self.history
    #     map = self.board_map
    #     valid2=True 
    #     if self.who_plays == 'w' :
    #         no_beetween = ( map[5][1] == None and maps[6][1] == None)
    #         for moves in history:
    #             if 'wra1' in moves or 'wke1' in moves:
    #                 valid2 = False
    #                 break
    #     if self.who_plays == 'b' :
    #         no_beetween=( map[5][7] == None and maps[6][7] == None)
    #         for moves in history:
    #             if 'bra8' in moves or 'bke8' in moves:
    #                 valid2 = False
    #     return no_beetween and valid 2
    
    def game(self):
#this function simulates a game of chess untill a possible checkmate
# check == 2 means check mate, == 1 means check, == 0 not check        
        check = 0
        team = self.who_plays
        
        #first movement made in board 
        l = self.round_moves()
        l_check = [] #possible moves to get out of check
        self.move(l)
        i = 1
        #next moves need to be checked (minimum moves for check mate?)
        while check < 2 or i < 200:           
            
            if team == 'w':
                king = self.whites_in_board[self.w_king_idx]                
            else:
                king = self.blacks_in_board[self.b_king_idx]
            
            check = king.is_checked(l) #cheking if A king is in check \
                #with possible moves of B team 
            
            if check == 0: #if not in check, move normally
                l = self.round_moves()
                self.move(l)
                
            if check == 1: #if in check, give possile moves to get out
                l_check = self.round_check_moves(king,l)
                if len(l_check) == 0:
                    check = 2
                else:
                    self.move(l_check)
            
            i += 1            

        return l_check
        
    


        

 
if __name__ == "__main__":
    b = Board()
    #b.remove_piece(pcs.pieces('wr','a1'))
   #b.prt()
    i = 1    
    while i < 200:
        print(f"\n-----------------------rodada {i}-----------------------\n")
        l = b.round_moves()
        print('-----------------Possible white moves\n',l)
        b.move(l)
        
        l = b.round_moves()
        print('\n-----------------Possible black moves\n',l)
        b.move(l)
        
        i += 1
        print('')
        b.prt()
        
    print(b.history)