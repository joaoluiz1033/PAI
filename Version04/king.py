X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7
import pdb

import pieces 
import coordinates

def king_moves(g_pos,add_x,add_y,l,board_map,team):   
# describes general movement 
#g_pos == current coordinates x,y
#add_x, add_y == aditions coordinates in x,y
#l == list with possible movements
#board_map == board map with current pieces \
    #board_map[y][x] is the correct use 
#team == pieces' team (black or white)
     
    x = g_pos[0]
    y = g_pos[1]
    x_new = x + add_x
    y_new = y + add_y
    
    limits = (x_new <= X_MAX) and (x_new >= X_MIN) and \
    (y_new >= Y_MIN) and (y_new <= Y_MAX)
    
    if limits:
        if (board_map[y_new][x_new] == None) or \
            (board_map[y_new][x_new].team != team):
                possible_move = coordinates.reconvert_to_alg([x_new,y_new])  
                l.append(possible_move)
                
                
    
    return l

class king(pieces.pieces):
    #king class inheritance of class pieces
    # king can go to 8 positions 
    def __init__(self,name,pos):
        super().__init__(name,pos)
        self.team = name[0]
        self.score = 10
    
    def can_reach(self,board_map,y,x,x_target,add):
        x += add
        while(x != x_target):
            if board_map[y][x] is not None:
                return False
            x += add
        return True
    
    def roque(self,board_map):
        
        l_possible_roque = []
        
        if len(self.history_mov) == 0:
            
            g_pos = coordinates.convert_to_coordinate(self.pos_alg)
            x = g_pos[0]
            y = g_pos[1]
            
            if board_map[y][X_MAX] is not None:
                if len(board_map[y][X_MAX].history_mov) == 0:
                    if self.can_reach(board_map,y,x,X_MAX,1):
                        g_roque = coordinates.reconvert_to_alg([x+2,y])
                        l_possible_roque.append(g_roque)
            if board_map[y][X_MIN] is not None:
                if len(board_map[y][X_MIN].history_mov) == 0:
                    if self.can_reach(board_map,y,x,X_MIN,-1):
                        g_roque = coordinates.reconvert_to_alg([x-2,y])
                        l_possible_roque.append(g_roque)
                
        return l_possible_roque
    
    def check_moves(self,board_map):
        l = []
        g_pos = coordinates.convert_to_coordinate(self.pos_alg)
        
        l = king_moves(g_pos,1,-1,l,board_map,self.team)
        l = king_moves(g_pos,1,0,l,board_map,self.team)
        l = king_moves(g_pos,1,1,l,board_map,self.team)
        l = king_moves(g_pos,0,-1,l,board_map,self.team)
        l = king_moves(g_pos,0,1,l,board_map,self.team)
        l = king_moves(g_pos,-1,-1,l,board_map,self.team)
        l = king_moves(g_pos,-1,0,l,board_map,self.team)
        l = king_moves(g_pos,-1,1,l,board_map,self.team)            
        l_roque = self.roque(board_map)        
        for move_roque in l_roque:
            l.append(move_roque)        
        return l

    def is_checked(self,enemy_moves):        
        king_pos = self.pos_alg      
        for sublist in enemy_moves:            
            if king_pos in sublist[1]: #verifying if king is in check                
                return True         
        return False
        

    def checker_pos(self,enemy_moves):
#return the position of the enemy piece that puts us in check
#enemy_moves == list of possible movements from enemies 
        l = []
        king_pos = self.pos_alg       
        # l_king = self.check_moves(board_map)       
        for sublist in enemy_moves:
            if king_pos in sublist[1]: #verifying if king is in check
                l.append(sublist)
                
        return l
        
    
    
            
    
if __name__ == "__main__":
    board_map = [ [ None for x in range(8) ] for y in range(8)]
    k1 = king('wp','f6')
    l = k1.check_moves(board_map)
    print(l)