X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

import pieces 
import coordinates

class pawn(pieces.pieces):
    #pawn class inheritance of class pieces
    def __init__(self,name,pos):
        super().__init__(name,pos)
        self.team = name[0]
    
    def check_moves(self,board_map):
        #check and return possible movements from pawn 
        l = []
        g_pos = coordinates.convert_to_coordinate(self.pos_alg)        
        if self.team == 'w':
            if  g_pos[1] < Y_MAX:
                new_pos = [g_pos[0],g_pos[1]+1]                
        else:
            if g_pos[1] > Y_MIN:
                new_pos = [g_pos[0],g_pos[1]-1]
        
        if board_map[new_pos[0]][new_pos[1]] is None:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
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
    