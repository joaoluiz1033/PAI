# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 22:02:44 2022

@author: danyz
"""
import numpy as np
class Board():
    def _init_(self):
        self.board=[["null" for i in range(8)] for j in range(8)]
    def is_piece(self,x,y):
        board=self.board
        board[x][y]!='null'
    def set_initial(self):
        self.board=[['wr', 'wkn', 'wb', 'wq', 'wki', 'wb', 'wkn', 'wr'],
         ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
         ['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],
         ['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],
         ['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],
         ['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],
         ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
         ['br', 'bkn', 'bb', 'bq', 'bki', 'bb', 'bkn', 'br']]
        
        
boards=Board()
boards.set_initial()
mat=boards.board
print(mat[7][6])      
        
     
        
        
        
        