X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

import pieces 
import coordinates

class king(pieces.pieces):
    #king class inheritance of class pieces
    # king can go to 8 positions 
    def __init__(self,name,pos):
        super().__init__(name,pos)
        self.team = name[0]
    
    def check_moves(self,board_map):
        l = []
        g_pos = coordinates.convert_to_coordinate(self.pos_alg)
        
        #first pos
        g_aux = [None,None]
        g_aux[0] = g_pos[0] + 1 
        g_aux[1] = g_pos[1] + 0
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        #second pos 
        
        g_aux[0] = g_pos[0] + 0 
        g_aux[1] = g_pos[1] + 1
        
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        #third pos
        
        g_aux[0] = g_pos[0] + 1 
        g_aux[1] = g_pos[1] + 1
        
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        #fourth pos
        
        g_aux[0] = g_pos[0] - 1 
        g_aux[1] = g_pos[1] - 1
        
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        #fifth pos
        
        g_aux[0] = g_pos[0] - 1 
        g_aux[1] = g_pos[1] + 0
         
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        #sixth pos
       
        g_aux[0] = g_pos[0] + 0 
        g_aux[1] = g_pos[1] - 1
        
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
        #seventh
        
        g_aux[0] = g_pos[0] + 1 
        g_aux[1] = g_pos[1] - 1
        
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
        #eigth
        
        g_aux[0] = g_pos[0] - 1 
        g_aux[1] = g_pos[1] + 1
        
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        return l
    
if __name__ == "__main__":
    board_map = [ [ None for x in range(8) ] for y in range(8)]
    k1 = king('wp','d5')
    l = k1.check_moves(board_map)
    print(l)