X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

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
            (board_map[y_new][x_new][0] != team):
                possible_move = coordinates.reconvert_to_alg([x_new,y_new])  
                l.append(possible_move)
                print(x_new,y_new)
                print(coordinates.reconvert_to_alg([x_new,y_new]))
                
    
    return l

class king(pieces.pieces):
    #king class inheritance of class pieces
    # king can go to 8 positions 
    def __init__(self,name,pos):
        super().__init__(name,pos)
        self.team = name[0]
    
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
            
        return l
        
    def is_checked(self,moves):
        coord=self.pos_alg
        checked=False 
        for sublist in moves:
            if coord in sublist[1]:
                checked=True 
                break
        return checked 
        
    def stalemate(self,moves):
        return moves==[]
            
    
if __name__ == "__main__":
    board_map = [ [ None for x in range(8) ] for y in range(8)]
    k1 = king('wp','d5')
    l = k1.check_moves(board_map)
    print(l)