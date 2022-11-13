X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

import pieces 
import coordinates

class rook(pieces.pieces):
    #rook class inheritance of class pieces
    def __init__(self,name,pos):
        super().__init__(name,pos)
        self.team = name[0]
    
    def check_moves(self,board_map):
        #check and return possible moves
        #rook can go into 4 directions
        l = []
        g_pos = coordinates.convert_to_coordinate(self.pos_alg)
        
        # checking postions going to the right
        found = False
        g_pos_aux = g_pos[0]
        limits = g_pos_aux < X_MAX
        
        while limits and (not found):            
            g_pos_aux = g_pos_aux + 1
            new_pos = [g_pos_aux,g_pos[1]]
            if (board_map[new_pos[0]][new_pos[1]] is None):                
                possible_move = coordinates.reconvert_to_alg(new_pos)        
                l.append(possible_move)
            else:
                if (board_map[new_pos[0]][new_pos[1]][0] != self.team):
                    possible_move = coordinates.reconvert_to_alg(new_pos)        
                    l.append(possible_move)
                found = True
            limits = g_pos_aux < X_MAX
                
        # checking postions going to the left
        found = False 
        g_pos_aux = g_pos[0]
        limits = g_pos_aux > X_MIN
        while limits and (not found):
            g_pos_aux = g_pos_aux - 1
            new_pos = [g_pos_aux,g_pos[1]]
            if (board_map[new_pos[0]][new_pos[1]] is None):
                possible_move = coordinates.reconvert_to_alg(new_pos)        
                l.append(possible_move)
            else:
                if (board_map[new_pos[0]][new_pos[1]][0] != self.team):
                    possible_move = coordinates.reconvert_to_alg(new_pos)        
                    l.append(possible_move)
                found = True
            limits = g_pos_aux > X_MIN
                
        #checking positions going down 
        found = False 
        g_pos_aux = g_pos[1] #y direction
        limits = g_pos_aux > Y_MIN
        while limits and (not found):
            g_pos_aux = g_pos_aux - 1
            new_pos = [g_pos[0],g_pos_aux]
            if (board_map[new_pos[0]][new_pos[1]] is None):
                possible_move = coordinates.reconvert_to_alg(new_pos)        
                l.append(possible_move)
            else:
                if (board_map[new_pos[0]][new_pos[1]][0] != self.team):
                    possible_move = coordinates.reconvert_to_alg(new_pos)        
                    l.append(possible_move)
                found = True
            limits = g_pos_aux > Y_MIN
                
        #checking positions going up 
        found = False 
        g_pos_aux = g_pos[1] #y direction
        limits = g_pos_aux < Y_MAX
        
        while limits and (not found):
            g_pos_aux = g_pos_aux + 1
            new_pos = [g_pos[0],g_pos_aux]
            if (board_map[new_pos[0]][new_pos[1]] is None):
                possible_move = coordinates.reconvert_to_alg(new_pos)        
                l.append(possible_move)
            else:
                if (board_map[new_pos[0]][new_pos[1]][0] != self.team):
                    possible_move = coordinates.reconvert_to_alg(new_pos)        
                    l.append(possible_move)
                found = True
            limits = g_pos_aux < Y_MAX
                
        return l

if __name__ == "__main__":
    board_map = [ [ None for x in range(8) ] for y in range(8)]
    r1 = rook('wp','a1')
    l = r1.check_moves(board_map)
    print(l)
    