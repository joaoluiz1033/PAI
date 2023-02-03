X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

import pieces 
import coordinates


def bishop_moves(g_pos,add_x,add_y,l,board_map,team):
#describe a general movement for bishop logic
#g_pos == current coordinates x,y
#add_x, add_y == aditions coordinates in x,y
#l == list with possible movements 
#board_map == board map with current pieces \
    #board_map[y][x] is the correct use 
#team == pieces' team (black or white)  
    found = False     
    x = g_pos[0]
    y = g_pos[1]
    x_new = x + add_x
    y_new = y + add_y
    limits = (x_new <= X_MAX) and (x_new >= X_MIN) and \
    (y_new >= Y_MIN) and (y_new <= Y_MAX)

    while limits and (not found):      

        if (board_map[y_new][x_new] is None):

            possible_move = coordinates.reconvert_to_alg([x_new,y_new])        
            l.append(possible_move)

        else:
            if (board_map[y_new][x_new].team != team):
                possible_move = coordinates.reconvert_to_alg([x_new,y_new])        
                l.append(possible_move)
            found = True

        x_new += add_x
        y_new += add_y
        limits = (x_new <= X_MAX) and (x_new >= X_MIN) and \
        (y_new >= Y_MIN) and (y_new <= Y_MAX)
    
   
    return l

class bishop(pieces.pieces):
    #bishop class inheritance of class pieces
    def __init__(self,name,pos):
        super().__init__(name,pos)
        self.team = name[0]
        self.score = 3
        self.global_score = self.score
    
    def check_moves(self,board_map):
        #check and return possible moves
        #bishop can go into 4 directions 
        l = []
        g_pos = coordinates.convert_to_coordinate(self.pos_alg)    
        
        l = bishop_moves(g_pos,1,1,l,board_map,self.team) #upright diagonal        
        l = bishop_moves(g_pos,1,-1,l,board_map,self.team) #downright 
        l = bishop_moves(g_pos,-1,1,l,board_map,self.team) #upleft
        l = bishop_moves(g_pos,-1,-1,l,board_map,self.team) #downleft
        return l
    
if __name__ == "__main__":
    board_map = [ [ None for x in range(8) ] for y in range(8)]
    b1 = bishop('wp','a1')
    l = b1.check_moves(board_map)
    print(l)