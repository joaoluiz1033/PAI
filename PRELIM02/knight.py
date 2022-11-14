X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

import pieces 
import coordinates
import board as bd

def knight_moves(g_pos,add_x,add_y,l,board_map,team):   
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
            (board_map[y_new][x_new][0] != team):
                possible_move = coordinates.reconvert_to_alg([x_new,y_new])  
                l.append(possible_move)
                
                
    
    return l

class knight(pieces.pieces):      
    #knight class inheritance of class pieces
    
    def __init__(self,name,pos):
        super().__init__(name,pos)
        self.team = name[0]
        

    
    def check_moves(self,board_map):
        #check and return possible moves
        #knight can take at maximum 8 positions
        l = []
        g_pos = coordinates.convert_to_coordinate(self.pos_alg) 
        
        #knight possible movements
        l = knight_moves(g_pos,1,2,l,board_map,self.team)
        l = knight_moves(g_pos,2,1,l,board_map,self.team)
        l = knight_moves(g_pos,2,-1,l,board_map,self.team)
        l = knight_moves(g_pos,1,-2,l,board_map,self.team)
        l = knight_moves(g_pos,-1,-2,l,board_map,self.team)
        l = knight_moves(g_pos,-2,-1,l,board_map,self.team)
        l = knight_moves(g_pos,-2,1,l,board_map,self.team)
        l = knight_moves(g_pos,-1,2,l,board_map,self.team)
       
        return l
    
if __name__ == "__main__":
    board_map = [ [ None for x in range(8) ] for y in range(8)]
    n1 = knight('wp','b1')
    l = n1.check_moves(board_map)
    print(l)