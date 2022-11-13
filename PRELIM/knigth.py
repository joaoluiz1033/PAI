X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

import pieces 
import coordinates

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
        
        #first pos
        g_aux = [None,None]
        g_aux[0] = g_pos[0] + 1 
        g_aux[1] = g_pos[1] + 2
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        #second pos 
        
        g_aux[0] = g_pos[0] + 2 
        g_aux[1] = g_pos[1] + 1
        
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        #third pos
        
        g_aux[0] = g_pos[0] + 2 
        g_aux[1] = g_pos[1] + -1
        
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        #fourth pos
        
        g_aux[0] = g_pos[0] - 1 
        g_aux[1] = g_pos[1] + 2
               
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        #fifth pos
        
        g_aux[0] = g_pos[0] - 1 
        g_aux[1] = g_pos[1] - 2
         
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
            
        #sixth pos
       
        g_aux[0] = g_pos[0] + 2 
        g_aux[1] = g_pos[1] - 1
        
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
        #seventh
        
        g_aux[0] = g_pos[0] - 2 
        g_aux[1] = g_pos[1] - 1
        
        limits = (g_aux[0] <= X_MAX) and (g_aux[0] >= X_MIN) and \
        (g_aux[1] >= Y_MIN) and (g_aux[1] <= Y_MAX)
        new_pos = g_aux
        if (board_map[new_pos[0]][new_pos[1]] is None or \
            board_map[new_pos[0]][new_pos[1]][0] != self.team) and limits:
            possible_move = coordinates.reconvert_to_alg(new_pos)        
            l.append(possible_move)
        #eigth
        
        g_aux[0] = g_pos[0] - 2 
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
    n1 = knight('wp','b1')
    l = n1.check_moves(board_map)
    print(l)