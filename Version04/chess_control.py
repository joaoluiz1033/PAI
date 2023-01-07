import sys
import chess_model as ch
import pdb
import time

from PyQt5.QtTest import *

import coordinates

class ControlerBase():
    
    def __init__(self):
        self.clients = []
    
    def addClient(self,client):
        self.clients.append(client)
        
        
    def refreshAll(self):
        for client in self.clients:
            client.refresh()

class Controler(ControlerBase):
    
    def __init__(self):
        super().__init__()
        self.board = ch.Board()
        self.game_type = 1
        self.IA_level = 1
        self.IA2_level = 1
        self.user = 'w'
        self.turn = 'w'
        self.server = 1
        self.move_history = []
        self.IA2_level = 1
        self.selected_moves_alg = []
        self.selected_moves_geo = []
        self.piece = []
        self.pos = []
        self.make_move = False
        self.l_enemy_moves = []
        self.refresh_functions = False
        self.timeMAX = 1
        self.stop = False
        self.begin = True
   
    def give_valid_moves(self):
        self.l_possible_moves = self.board.possible_moves()            
        self.l_valid_moves = self.board.simulate_check(self.l_possible_moves)        
        return self.l_valid_moves
    
    def give_map(self):
        return self.board.board_map
    
    def give_map_board(self):
        self.board.prt()
        return 
    
    def give_who_plays(self): 
        return self.board.who_plays()
    
    def give_game_state(self):
        end_game = False
        if ch.is_empty(self.l_valid_moves):                                
            end_game = True
        return end_game
    
    def give_final_result(self,king):        
        if king.is_checked(self.l_enemy_moves):
            print(f"Check Mate: {king}")
        else:                    
            print(f"{self.board.who_plays} cannot move")            
            
    def give_who_plays(self):
        if self.board.who_plays == 'w':
            return self.board.w_king
        else:
            return self.board.b_king
    
    def send_who_plays(self):
        self.board.change_who_plays()
        
    def send_U_move(self, piece, movement):
        self.l_enemy_moves = self.board.move_User(self.l_possible_moves,piece,movement)
        self.l_enemy_moves = self.board.simulate_check(self.l_enemy_moves)
        self.turn = self.board.change_who_plays()
        return self.l_enemy_moves
    
    def send_IA_move(self,IA_level):
        self.l_enemy_moves = self.board.move_IA(IA_level,self.l_valid_moves,\
                                        self.l_enemy_moves)
        self.l_enemy_moves = self.board.simulate_check(self.l_enemy_moves)
        self.turn = self.board.change_who_plays()
        return self.l_enemy_moves
    
    def clicked_piece(self,piece):
        self.selected_moves_alg = []
        self.selected_moves_geo = []
        m = self.give_map()
        if piece.type == 'p':
            p = m[7-piece.x][piece.j]
            self.l_valid_moves = self.give_valid_moves()
            for pair in self.l_valid_moves:
                if p == pair[0]:
                    self.piece = pair[0]
                    for move in pair[1]:
                        self.selected_moves_alg.append(move)
                        self.selected_moves_geo.append(coordinates.\
                            convert_to_coordinate(move))
        self.make_move = True
        self.refreshAll()
    
    def user_vs_IA(self):
        movement = coordinates.reconvert_to_alg(self.pos)
        self.l_valid_moves = self.give_valid_moves()
        self.l_enemy_moves = self.send_U_move(self.piece,movement)
        king = self.give_who_plays()
        self.l_valid_moves = self.give_valid_moves()        
        if not self.give_game_state():
            self.l_enemy_moves = self.send_IA_move()            
        else:            
            self.give_final_result(king)
        self.selected_moves_alg = []
        self.selected_moves_geo = []
        self.make_move = False        
        self.refreshAll()
           
        
    def IA_initial_move(self):
        self.l_valid_moves = self.give_valid_moves()
        self.l_enemy_moves = self.send_IA_move(self.IA_level)
        self.refreshAll()    
    
    def user_move(self):
        movement = coordinates.reconvert_to_alg(self.pos)
        self.l_valid_moves = self.give_valid_moves()
        self.l_enemy_moves = self.send_U_move(self.piece,movement) 
        king = self.give_who_plays()  
        self.l_valid_moves = self.give_valid_moves()        
        if not self.give_game_state():
            pass            
        else:            
            self.give_final_result(king)
        self.selected_moves_alg = []
        self.selected_moves_geo = []
        self.make_move = False        
        self.stop = True
        self.begin = False
        self.refreshAll()
        return self.give_game_state()
        
    def IA_move(self,IA_level):
        king = self.give_who_plays()  
        self.l_valid_moves = self.give_valid_moves()
        if not self.give_game_state():
            self.l_enemy_moves = self.send_IA_move(IA_level)            
        else:            
            self.give_final_result(king)
        self.selected_moves_alg = []
        self.selected_moves_geo = []
        self.make_move = False        
        self.begin = True
        self.stop = False
        self.refreshAll()
        return self.give_game_state()
    
    def user_vs_user(self):
        movement = coordinates.reconvert_to_alg(self.pos)
        self.l_valid_moves = self.give_valid_moves()
        self.l_enemy_moves = self.send_U_move(self.piece,movement)
        self.stop = True
        self.begin = False
        king = self.give_who_plays()  
        self.l_valid_moves = self.give_valid_moves()        
        if not self.give_game_state():
            pass            
        else:            
            self.give_final_result(king)
        self.selected_moves_alg = []
        self.selected_moves_geo = []
        self.make_move = False
        self.refreshAll() 
                
    def game(self):
        if self.game_type == 1:
            if self.turn == self.user:
                game_state = self.user_move()
            if not game_state:
                QTest.qWait(250)
                self.IA_move(self.IA_level)
            #self.user_vs_IA()
        elif self.game_type == 2:
            self.user_vs_user()
        else:
            i = 0
            game_state = False
            while game_state == False and i<250:
                game_state = self.IA_move(self.IA_level)
                if not game_state:
                    QTest.qWait(250)
                    self.IA_move(self.IA2_level)
                    i += 1
                    print(i)
                print(game_state)
            
if __name__ == "__main__":
    pass
      
