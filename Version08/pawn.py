X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

import pdb

import pieces 
import coordinates


def debug_trace():
    from PyQt5.QtCore import pyqtRemoveInputHook
    from pdb import set_trace
    pyqtRemoveInputHook()
    set_trace()
    
class pawn(pieces.pieces):
   
    def __init__(self,name,pos):
        super().__init__(name,pos)
        self.team = name[0]
        self.en_passante_moves = []
        self.score = 1         
        
    def diags_possible(self,board_map):
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
        else:
          if y > 0:
              if x == 0:
                  diags.append([x+1,y-1])
              elif x == 7:
                  diags.append([x-1,y-1])
              else:
                   diags.append([x-1,y-1])
                   diags.append([x+1,y-1])
       
        for position in diags:
            if board_map[position[1]][position[0]] is not None:
                if board_map[position[1]][position[0]].team != self.team:
                    l.append(coordinates.reconvert_to_alg(position))
                    
        return l
                   
    def two_square(self,board_map):
        g_pos = coordinates.convert_to_coordinate(self.pos_alg) 
        x = g_pos[0]
        y = g_pos[1]
        l=[]
        if self.team == 'w'  and y == 1 and board_map[x][y+1] is  None and board_map[x][y+2] is  None :
            l.append(coordinates.reconvert_to_alg([x,y+2]))
        elif self.team == 'b' and y == 6 and board_map[x][y-1] is  None and board_map[x][y-2] is  None :
            l.append(coordinates.reconvert_to_alg([x,y-2]))
        return l

            
    def at_max(self):
        cart_pos = coordinates.convert_to_coordinate(self.pos_alg)
        y = cart_pos[1]
        if self.team == 'w':
            if y == Y_MAX:
                return True
        else:
            if y == Y_MIN:
                return True
        return False 
    
    def next_at_max(self):
        cart_pos = coordinates.convert_to_coordinate(self.pos_alg)
        y = cart_pos[1]
        if self.team == 'w':
            if y == Y_MAX - 1:
                return True
        else:
            if y == Y_MIN + 1:
                return True
        return False
          

    def check_moves(self,board_map):
        #check and return possible movements from pawn 
        l = []
        g_pos = coordinates.convert_to_coordinate(self.pos_alg) 
        x = g_pos[0]
        y = g_pos[1]                
        if self.team == 'w':
            if  y < Y_MAX:
                y_new = y + 1   
                if board_map[y_new][x] is None:
                    possible_move = coordinates.reconvert_to_alg([x,y_new])        
                    l.append(possible_move)
                diagonal_moves = self.diags_possible(board_map)                
                for diag in diagonal_moves:
                    l.append(diag)
            if y == 1 :
                y_new = y + 2
                if (board_map[y_new-1][x] is None) and (board_map[y_new][x] is None):
                    possible_move = coordinates.reconvert_to_alg([x,y_new])        
                    l.append(possible_move)
        else:
            if y > Y_MIN:
                y_new = y - 1 
                if board_map[y_new][x] is None:
                    possible_move = coordinates.reconvert_to_alg([x,y_new])        
                    l.append(possible_move)
                diagonal_moves = self.diags_possible(board_map)                 
                for diag in diagonal_moves:
                    l.append(diag)            
            if y == 6:
                y_new = y - 2
                if board_map[y_new][x] is None and board_map[y_new+1][x] is None:
                    possible_move = coordinates.reconvert_to_alg([x,y_new])        
                    l.append(possible_move)                    
        if len(self.en_passante_moves) > 0:            
            if self.team == 'w':
                add = 1
            else:
                add = -1            
            for possible_movement in self.en_passante_moves:                
                geom_pos = coordinates.convert_to_coordinate(\
                 possible_movement)
                x = geom_pos[0]
                y = geom_pos[1]
                if board_map[y][x] is None:
                    if board_map[y-add][x] is not None and \
                        board_map[y-add][x].name[0] != self.name[0]:
                        if board_map[y-add][x].name[1] == 'p' and \
                            board_map[y-add][x].name[0] != self.team:
                                l.append(possible_movement)
                else:
                    self.en_passante_moves.remove(possible_movement)
            
        return l

if __name__ == "__main__":
    #p = pieces('wk','a1')
    #p2 = pieces('wk','a1')
    #print(p.__eq__(p2))
    board_map = [ [ None for x in range(8) ] for y in range(8)]
    pw1 = pawn('wp','a2')
    l = pw1.check_moves(board_map)
    pw2 = pawn('wp','a2')
    print(pw1.name)
    
