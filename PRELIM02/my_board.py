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
        self.current_board()  
        self.dead_pieces=[] #dead pieces
        
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
        
        return [p,p.check_moves(self.board_map)]
    
    def move(self,l_possible_moves):
        '''
        Parameters
        ----------
        l_possible_moves : LIST
            LIST OF POSSIBLE MOVES FOR THE PLAYER.

        Returns
        -------
        l_possible_moves : LIST
            POSSIBLE MOVES MODIFIED (RECENT MOVE DELETED).

        '''
        a = False
        l1 = []
        
        # print(self.who_plays,l_possible_moves)
        if is_empty(l_possible_moves):
            return l_possible_moves
        else:
            
            if self.who_plays == 'w':
                pieces_board = self.whites_in_board
                enemies_board = self.blacks_in_board
                king = self.w_king
                self.who_plays = 'b'
            else:
                pieces_board = self.blacks_in_board
                enemies_board = self.whites_in_board
                king = self.b_king
                self.who_plays = 'w'
            
            valid = False
            while not valid:
                l = random.choice(l_possible_moves)
                idx_pawn = l_possible_moves.index(l)
                piece = l[0]
                if len(l[1]) > 0:
                    valid = True
                    
            movement = random.choice(l[1])
            # l_copy = copy.deepcopy(l_possible_moves)
            
            
            movement_xy = coordinates.convert_to_coordinate(movement)
            x = movement_xy [0]
            y = movement_xy [1]
            
            
            if piece in pieces_board:
                #print(f"{piece} to {movement}")                
                if self.board_map[y][x] is not None:                    
                    if self.board_map[y][x].name[1] == 'k':
                        return []                                                                                   
                    enemies_board.remove(self.board_map[y][x])
                    # print(f"{self.board_map[y][x]} eliminated at {movement}")
                       
                    
                idx = pieces_board.index(piece)
                pieces_board[idx].pos_alg = movement  
                l[1].remove(movement)
                if piece.name[1] == 'k':
                    king.pos_alg = movement
                
                    
                if piece.name[1] == 'p':
                    if pieces_board[idx].at_max():
                        
                        new_l = self.change_pawn(movement,pieces_board,\
                          idx,pieces_board[idx].team )                           
                        l_possible_moves[idx_pawn] = new_l
                       
                    
                    
            self.current_board()
            
            if a:
                return []
            else:
                return l_possible_moves

    

    
    def simulate_check(self,possible_moves,enemy_moves):      
        
        team = self.who_plays   
        valid_list = []
        for x in possible_moves:            
            piece = x[0]
            movements = x[1]
            valid_movements = []
            for movement in movements:
                b_simulation = copy.deepcopy(self)
                movement_xy = coordinates.convert_to_coordinate(movement)
                x = movement_xy [0]
                y = movement_xy [1]
                
                if team == 'w':
                    pieces_board = b_simulation.whites_in_board
                    enemy_board = b_simulation.blacks_in_board
                    king = b_simulation.w_king
                    enemy = 'b'
                else:
                    pieces_board = b_simulation.blacks_in_board
                    enemy_board = b_simulation.whites_in_board
                    king = b_simulation.b_king
                    enemy = 'w'
                
                if piece in pieces_board:                    
                    if b_simulation.board_map[y][x] is not None:                        
                        enemy_board.remove(b_simulation.board_map[y][x])
                    idx = pieces_board.index(piece)
                    pieces_board[idx].pos_alg = movement
                    
                    if piece.name[1] == 'k':
                        king.pos_alg = movement
                        
                b_simulation.current_board()
                
                                    
                    
                b_simulation.who_plays = enemy
                #print('\n',king, piece,movement,'\n') 
                #b_simulation.prt()
                #print(king.pos_alg,b_simulation.possible_moves())                
                if king.is_checked(b_simulation.possible_moves()) == False:
                    
                    valid_movements.append(movement)
                    
            valid_list.append([piece,valid_movements])
        
        return valid_list
    
    
    
    def game(self):
        '''
        Simulation of a game 

        Returns
        -------
        None.

        '''
        
        l_enemy_moves = []
        
        check_mate = False
        i = 0
        while not check_mate and i <1000:
            
            l_possible_moves = self.possible_moves()
            l_possible_moves = self.simulate_check(l_possible_moves\
                                        , l_enemy_moves)
            #print(l_possible_moves)
            if self.who_plays == 'w':
                king = self.w_king
            else:
                king = self.b_king
            
            if king.is_checked(l_enemy_moves):
                
                l_out = self.simulate_check(l_possible_moves\
                                            , l_enemy_moves)
                if is_empty(l_out):
                    print(f"check mate {king}")
                    #self.prt()
                    #print(l_enemy_moves)
                    check_mate = True
                else:   
                    
                    l_out = self.move(l_out)
                    l_enemy_moves = l_out
            else:
                
                if is_empty(l_possible_moves):
                    print(f"check mate {king}")
                    check_mate = True
                else:     
                    
                    l_possible_moves = self.move(l_possible_moves)
                    l_enemy_moves = l_possible_moves                    
            i += 1
        if check_mate:
            return
        else:
            print('Draw - exceeded number of plays')

 
if __name__ == "__main__":
    bd = Board()
    bd.game()
    bd.prt()
    # b_c = b
    # b_c.w_king = k.king('bk','a3')
    # print(b.w_king)
    
    

