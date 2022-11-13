X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

import coordinates 

class pieces():    
    def __init__(self,name,pos):
        self.name = name        
        self.pos_alg = pos
        
    def __repr__(self):
        return f"{self.name} at {self.pos_alg}"
    
    def __eq__(self,other):
        return self.name == other.name and self.pos_alg == other.pos_alg
    
    def check_moves(self,board_map):
        pass
    
    def move(self,final_pos):
        #move piece from current position to final position
        self.pos_alg = final_pos

    
# class pawn(pieces):
#     #pawn class inheritance of class pieces
#     def __init__(self,name,pos):
#         super().__init__(name,pos)
#         self.team = name[0]
    
#     def check_moves(self,board_map):
#         #check and return possible movements from pawn 
#         l = []
#         g_pos = coordinates.convert_to_coordinate(self.pos_alg)        
#         if self.team == 'w':
#             if  g_pos[1] < Y_MAX:
#                 new_pos = [g_pos[0],g_pos[1]+1]
                
#         else:
#             if g_pos[1] > Y_MIN:
#                 new_pos = [g_pos[0],g_pos[1]-1]
        
#         if board_map[new_pos[0]][new_pos[1]] is None:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         return l

# class rook(pieces):
#     #rook class inheritance of class pieces
#     def __init__(self,name,pos):
#         super().__init__(name,pos)
#         self.team = name[0]
    
#     def check_moves(self):
#         #check and return possible moves
#         #rook can go into 4 directions
#         l = []
#         g_pos = coordinates.convert_to_coordinate(self.pos_alg)
        
#         # checking postions going to the right
#         found = False
#         g_pos_aux = g_pos[0]
#         limits = g_pos_aux < X_MAX
        
#         while limits and found:
#             g_pos_aux = g_pos_aux + 1
#             new_pos = [g_pos_aux,self.pos_alg[1]]
#             if (board_map[g_pos_aux][g_pos[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         # checking postions going to the left
#         found = False 
#         g_pos_aux = g_pos[0]
#         limits = g_pos_aux > X_MIN
#         while limits and found:
#             g_pos_aux = g_pos_aux - 1
#             new_pos = [g_pos_aux,g_pos[1]]
#             if (board_map[g_pos_aux][g_pos[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         #checking positions going down 
#         found = False 
#         g_pos_aux = g_pos[1] #y direction
#         limits = g_pos_aux > Y_MIN
        
#         while limits and found:
#             g_pos_aux = g_pos_aux - 1
#             new_pos = [g_pos[0],g_pos_aux]
#             if (board_map[g_pos_aux][g_pos[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         #checking positions going up 
#         found = False 
#         g_pos_aux = g_pos[1] #y direction
#         limits = g_pos_aux < Y_MAX
        
#         while limits and found:
#             g_pos_aux = g_pos_aux + 1
#             new_pos = [g_pos[0],g_pos_aux]
#             if (board_map[g_pos_aux][g_pos[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True            
#         return l
    
# class bishop(pieces):
#     #bishop class inheritance of class pieces
#     def __init__(self,name,pos):
#         super().__init__(name,pos)
#         self.team = name[0]
    
#     def check_moves(self):
#         #check and return possible moves
#         #bishop can go into 4 directions 
#         l = []
#         g_pos = coordinates.convert_to_coordinate(self.pos_alg)    
        
#         # upright diagonal 
#         found = False
#         g_pos_aux = [g_pos[0],g_pos[1]]
#         limits = g_pos_aux[0] < X_MAX and g_pos_aux[1] < Y_MAX
        
#         while limits and found:
#             g_pos_aux += [1,1]
#             new_pos = g_pos_aux
#             if (board_map[g_pos_aux[0]][g_pos_aux[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         #downpright diagonal 
#         found = False
#         g_pos_aux = [g_pos[0],g_pos[1]]
#         limits = g_pos_aux[0] < X_MAX and g_pos_aux[1] > Y_MIN
        
#         while limits and found:
#             g_pos_aux += [1,-1]
#             new_pos = g_pos_aux
#             if (board_map[g_pos_aux[0]][g_pos_aux[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
        
#         # upleft diagonal 
#         found = False
#         g_pos_aux = [g_pos[0],g_pos[1]]
#         limits = g_pos_aux[0] > X_MIN and g_pos_aux[1] < Y_MAX
        
#         while limits and found:
#             g_pos_aux += [-1,1]
#             new_pos = g_pos_aux
#             if (board_map[g_pos_aux[0]][g_pos_aux[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         # downleft diagonal 
#         found = False
#         g_pos_aux = [g_pos[0],g_pos[1]]
#         limits = g_pos_aux[0] > X_MIN and g_pos_aux[1] > Y_MIN
        
#         while limits and found:
#             g_pos_aux += [-1,-1]
#             new_pos = g_pos_aux
#             if (board_map[g_pos_aux[0]][g_pos_aux[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
#         return l

# class knight(pieces):      
#     #knight class inheritance of class pieces
#     def __init__(self,name,pos):
#         super().__init__(name,pos)
#         self.team = name[0]
    
#     def check_moves(self):
#         #check and return possible moves
#         #knight can take at maximum 8 positions
#         l = []
#         g_pos = coordinates.convert_to_coordinate(self.pos_alg)
        
#         #first pos 
#         g_aux = g_pos + [1,2] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         #second pos 
#         g_aux = g_pos + [2,1] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         #third pos
#         g_aux = g_pos + [2,-1] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         #fourth pos
#         g_aux = g_pos + [1,-2] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         #fifth pos
#         g_aux = g_pos + [-1,2] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         #sixth pos
#         g_aux = g_pos + [-1,-2] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         g_aux = g_pos + [-2,-1] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         g_aux = g_pos + [-1,-2] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         return l

# class queen(pieces):
#     #queen class inheritance of class pieces
#     def __init__(self,name,pos):
#         super().__init__(name,pos)
#         self.team = name[0]
    
#     def check_moves(self):
#         #check and return possible moves
#         #queen moves like bishop + rook
#         l = []
#         g_pos = coordinates.convert_to_coordinate(self.pos_alg)
        
#         # upright diagonal 
#         found = False
#         g_pos_aux = [g_pos[0],g_pos[1]]
#         limits = g_pos_aux[0] < X_MAX and g_pos_aux[1] < Y_MAX
        
#         while limits and found:
#             g_pos_aux += [1,1]
#             new_pos = g_pos_aux
#             if (board_map[g_pos_aux[0]][g_pos_aux[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         #downpright diagonal 
#         found = False
#         g_pos_aux = [g_pos[0],g_pos[1]]
#         limits = g_pos_aux[0] < X_MAX and g_pos_aux[1] > Y_MIN
        
#         while limits and found:
#             g_pos_aux += [1,-1]
#             new_pos = g_pos_aux
#             if (board_map[g_pos_aux[0]][g_pos_aux[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
        
#         # upleft diagonal 
#         found = False
#         g_pos_aux = [g_pos[0],g_pos[1]]
#         limits = g_pos_aux[0] > X_MIN and g_pos_aux[1] < Y_MAX
        
#         while limits and found:
#             g_pos_aux += [-1,1]
#             new_pos = g_pos_aux
#             if (board_map[g_pos_aux[0]][g_pos_aux[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         # downleft diagonal 
#         found = False
#         g_pos_aux = [g_pos[0],g_pos[1]]
#         limits = g_pos_aux[0] > X_MIN and g_pos_aux[1] > Y_MIN
        
#         while limits and found:
#             g_pos_aux += [-1,-1]
#             new_pos = g_pos_aux
#             if (board_map[g_pos_aux[0]][g_pos_aux[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         # checking postions going to the right
#         found = False
#         g_pos_aux = g_pos[0]
#         limits = g_pos_aux < X_MAX
        
#         while limits and found:
#             g_pos_aux = g_pos_aux + 1
#             new_pos = [g_pos_aux,self.pos_alg[1]]
#             if (board_map[g_pos_aux][g_pos[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         # checking postions going to the left
#         found = False 
#         g_pos_aux = g_pos[0]
#         limits = g_pos_aux > X_MIN
#         while limits and found:
#             g_pos_aux = g_pos_aux - 1
#             new_pos = [g_pos_aux,g_pos[1]]
#             if (board_map[g_pos_aux][g_pos[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         #checking positions going down 
#         found = False 
#         g_pos_aux = g_pos[1] #y direction
#         limits = g_pos_aux > Y_MIN
        
#         while limits and found:
#             g_pos_aux = g_pos_aux - 1
#             new_pos = [g_pos[0],g_pos_aux]
#             if (board_map[g_pos_aux][g_pos[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True
                
#         #checking positions going up 
#         found = False 
#         g_pos_aux = g_pos[1] #y direction
#         limits = g_pos_aux < Y_MAX
        
#         while limits and found:
#             g_pos_aux = g_pos_aux + 1
#             new_pos = [g_pos[0],g_pos_aux]
#             if (board_map[g_pos_aux][g_pos[1]] is None):
#                 possible_move = coordinates.reconvert_to_alg(new_pos)        
#                 l.append(possible_move)
#             else:
#                 found = True  
                
#         return l

# def king(pieces):
#     #king class inheritance of class pieces
#     # king can go to 8 positions 
#     def __init__(self,name,pos):
#         super().__init__(name,pos)
#         self.team = name[0]
    
#     def check_moves(self):
#         l = []
#         g_pos = coordinates.convert_to_coordinate(self.pos_alg)
#         #first pos 
#         g_aux = g_pos + [1,0] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         #second pos 
#         g_aux = g_pos + [0,1] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         #third pos
#         g_aux = g_pos + [1,1] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         #fourth pos
#         g_aux = g_pos + [1,-1] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         #fifth pos
#         g_aux = g_pos + [-1,1] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         #sixth pos
#         g_aux = g_pos + [-1,-1] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         g_aux = g_pos + [-1,0] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         g_aux = g_pos + [0,-1] 
#         limits = (g_aux[0] < X_MAX) and (g_aux[0] > X_MIN) and \
#         (g_aux[1] > Y_MIN) and (g_aux[1] < Y_MAX)
#         new_pos = g_aux
#         if (board_map[g_aux[0]][g_aux[1]] is None) and limits:
#             possible_move = coordinates.reconvert_to_alg(new_pos)        
#             l.append(possible_move)
            
#         return l
    
    




    
            
        
            
            
            
             
            
        
            
        
            
        
                
            
        
            
            
        