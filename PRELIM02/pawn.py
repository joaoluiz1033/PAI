X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

import pieces 
import coordinates

def pawn_moves(g_pos,add_x,add_y,l,board_map,team):   
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

class pawn(pieces.pieces):
    #pawn class inheritance of class pieces
    def __init__(self,name,pos):
        super().__init__(name,pos)
        self.team = name[0]
        
    def diags_possible(self):
        diags=[]
        l = []
        g_pos = coordinates.convert_to_coordinate(self.pos_alg) 
        x = g_pos[0]
        y = g_pos[1]
        if self.team =='w':
            if y < 7:
                if x == 0:
                    diags.append([x+1,y+1])
                elif x == 7:
                    diags.append([x-1,y+1])
                else:
                     diags.append([x-1,y+1])
                     diags.append([x+1,y+1])
          if self.team =='b':
            if y > 0:
                if x == 0:
                    diags.append([x-1,y-1])
                elif x == 7:
                    diags.append([x-1,y+1])
                else:
                     diags.append([x-1,y+1])
                     diags.append([x+1,y+1])
            return diags
          
        
         

                
              
                
            
            
        
    
    def check_moves(self,board_map):
        #check and return possible movements from pawn 
        l = []
        g_pos = coordinates.convert_to_coordinate(self.pos_alg) 
        x = g_pos[0]
        y = g_pos[1]
        if self.team == 'w':
            if  y < Y_MAX:
                y_new = y + 1                
        else:
            if y > Y_MIN:
                y_new = y -1 
        
        if board_map[y_new][x] is None:
            possible_move = coordinates.reconvert_to_alg([x,y_new])        
            l.append(possible_move)
            
        return l

if __name__ == "__main__":
    #p = pieces('wk','a1')
    #p2 = pieces('wk','a1')
    #print(p.__eq__(p2))
    board_map = [ [ None for x in range(8) ] for y in range(8)]
    pw1 = pawn('wp','a2')
    l = pw1.check_moves(board_map)
    print(l)
    
