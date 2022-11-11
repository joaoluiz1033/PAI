# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 22:15:07 2022

@author: danyz
"""

class pieces():
    def __init__(self,name,x:int,y:int):
        self.name=name
        self.x=x
        self.y=y

    def can_move(self,x2,y2):
        x=self.x
        y=self.y
        name=self.name
        if x2>8 or x2 <1 or y2>8 or y2<1:
            return False
        if name=='wr'or name=='br':
            if x==x2 or y==y2:
                return True
        if name=='wkn'or name=='bkn':
            if (abs(x2-x)==1 and abs(y2-y)==2):
                return True
        if name=='wb'or name=='bb':
            if abs(x2-x)==abs(y2-y):
                return True
        if name=='wp'or name=='bp':
            if (name=='wp'):
              if(y==2 and x2==x and y2==4):
                   return True
              if(x2==x and y2-y==1):
                  return True
            if (name=='bp'):
                if (y==7 and x2==x and y2==5):
                    return True
                if (x2==x and y2-y==-1):
                    return True
        if name=='bq' or name=='wq':
            piece1=pieces('wb',x,y);
            piece2=pieces('wr',x,y);
            return piece1.can_move(x2,y2) or piece2.can_move(x2,y2)
        if name=='bki' or name=='wki':
            if abs(x2-x)==1 or abs(y2-y)==1:
                return True
        else:
            return False
    
            
        
        
        
        





    
            
        
            
            
            
             
            
        
            
        
            
        
                
            
        
            
            
        