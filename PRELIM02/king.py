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
            (board_map[y_new][x_new].team != team):
                possible_move = coordinates.reconvert_to_alg([x_new,y_new])  
                l.append(possible_move)
                
                
    
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
        
     
        
#     def is_checked(self,moves):
# #this function verifies if king is in check
# #to be in check
#         coord=self.pos_alg
#         checked=False 
#         for sublist in moves:
#             if coord in sublist[1]:
#                 checked=True 
#                 break
#         return checked 
    def is_checked(self,enemy_moves):
        '''
        this function verifies if king is checked and where it can go 

        Parameters
        ----------
        enemy_moves : List
            possible movements from enemies.

        Returns
        -------
        True if king is in check, False otherwise.

        '''
        
        king_pos = self.pos_alg
        
        # l_king = self.check_moves(board_map)       
              
        for sublist in enemy_moves:
            if king_pos in sublist[1]: #verifying if king is in check
                #print(enemy_moves[i])
                return True
            # for movements in l_king:
            #     if movements in sublist[1]: #verifying if king can escape
            #         l_king.remove(movements) #removing this movement
        
        

    def checker_pos(self,enemy_moves):
#return the position of the enemy piece that puts us in check
#enemy_moves == list of possible movements from enemies 
        l = []
        king_pos = self.pos_alg       
        # l_king = self.check_moves(board_map)       
        for sublist in enemy_moves:
            if king_pos in sublist[1]: #verifying if king is in check
                l.append(sublist)
                
        return l
        
    def stalemate(self,moves):
        return moves == []

            
    
if __name__ == "__main__":
    board_map = [ [ None for x in range(8) ] for y in range(8)]
    k1 = king('wp','d5')
    l = k1.check_moves(board_map)
    print(len(k1))