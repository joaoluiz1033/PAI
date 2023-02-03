X_MIN = 0
Y_MIN = 0
X_MAX = 7
Y_MAX = 7

import coordinates 

class pieces():    
    def __init__(self,name,pos):
        self.name = name        
        self.pos_alg = pos
        self.score = 0
        self.history_mov = []
        self.global_score = 0        
        
    def __repr__(self):
        return f"{self.name} at {self.pos_alg}"
    
    def __eq__(self,other):
        if other is None:
            return False
        else:
            return self.name == other.name and self.pos_alg == other.pos_alg
    
    def check_moves(self,board_map):
        pass
    
    def move(self,final_pos):
        #move piece from current position to final position
        self.pos_alg = final_pos
        
    def in_danger(self,movement,enemy_moves):
        for sublist in enemy_moves:            
            if movement in sublist[1]:                
                return True         
        return False

    

    




    
            
        
            
            
            
             
            
        
            
        
            
        
                
            
        
            
            
        