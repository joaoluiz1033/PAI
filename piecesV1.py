# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 22:15:07 2022

@author: danyz
"""

class pieces():
    
    def __init__(self,name,pos):
        self.name = name        
        self.pos_alg = pos
        
    def __repr__(self):
        return f"{self.name} at {self.pos_alg}"
    
    def __eq__(self,other):
        return self.name == other.name and self.pos_alg == other.pos_alg
    

   
            
        
 
if __name__ == "__main__":
    p = pieces('wk','a1')
    p2 = pieces('wk','a1')
    print(p.__eq__(p2))
            
        
        





    
            
        
            
            
            
             
            
        
            
        
            
        
                
            
        
            
            
        