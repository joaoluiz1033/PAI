import sys
import pdb
import time
import pickle

import coordinates
import chess_model as ch
import board as bd


def debug_trace():
    from PyQt5.QtCore import pyqtRemoveInputHook
    from pdb import set_trace
    pyqtRemoveInputHook()
    set_trace()


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
        self.board = bd.Board()
        self.model = ch.Game(self.board)
        self.game_type = 1
        self.IA_level = 1
        self.IA2_level = 1
        self.user = 'w'
        self.turn = 'w'
        self.server = 1        
        self.IA2_level = 1
        self.selected_moves_alg = []
        self.selected_moves_geo = []
        self.piece = []
        self.pos = []
        self.make_move = False
        self.l_enemy_moves = []
        self.refresh_functions = False
        self.timeMAX = 1
        self.result = False
        self.string_result = ''
        self.time = 0
        self.i = 0
        self.iMax = 90
   
    def give_valid_moves(self):
        self.l_possible_moves = self.model.possible_moves()       
        self.l_valid_moves = self.model.simulate_check(self.l_possible_moves)        
        return self.l_valid_moves
    
    def give_map(self):
        return self.model.board.board_map
    
    def give_map_board(self):
        self.model.board.prt()
        return 
    
    def give_who_plays(self): 
        return self.model.board.who_plays()
    
    def give_game_state(self):        
        end_game = False              
        self.l_valid_moves = self.give_valid_moves()
        if ch.is_empty(self.l_valid_moves):                              
            end_game = True
            self.result = True
        return end_game
        
    
    def give_final_result(self,king):
        if king.is_checked(self.l_enemy_moves):
            if self.model.board.history[-1][-1] != '+':
                self.model.board.history[-1] = self.model.board.history[-1] + '#'
            else:
                self.model.board.history[-1] = \
                    self.model.board.history[-1].replace("+","#")
            s = self.giveHistoryString()
            self.string_result = f"Check Mate: {king}\n{s}"
        else:
            if self.i < self.iMax:
                self.result = True                    
                s = self.giveHistoryString()
                if self.L > 3:
                    self.string_result = \
                    f"{self.model.board.who_plays} cannot move\n{s}" 
                else:
                    self.string_result = "Draw\n{s}"
            else:
                self.result = True
                s = self.giveHistoryString()
                self.string_result = \
                    f"Draw by maximum iteration number {self.iMax}\n{s}"
        self.refreshAll()
        return
    
    def giveHistoryString(self):
        return self.model.board.historyToString()
    
    def give_who_plays(self):
        if self.model.board.who_plays == 'w':
            return self.model.board.w_king
        else:
            return self.model.board.b_king
    
    def send_who_plays(self):
        self.model.change_who_plays()
        
    def send_U_move(self, piece, movement):
        self.l_enemy_moves = self.model.move_User(self.l_possible_moves,piece,movement)
        self.l_enemy_moves = self.model.simulate_check(self.l_enemy_moves)
        self.turn = self.model.change_who_plays()        
        return self.l_enemy_moves
    
    def send_IA_move(self,IA_level):
        self.l_enemy_moves = self.model.move_IA(IA_level,self.l_valid_moves,\
                                        self.l_enemy_moves)
        self.l_enemy_moves = self.model.simulate_check(self.l_enemy_moves)
        self.turn = self.model.change_who_plays()
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
        if king.is_checked(self.l_enemy_moves):
            self.model.board.history[-1] = self.model.board.history[-1] + '+'
        self.l_valid_moves = self.give_valid_moves()        
        if not self.give_game_state():
            pass            
        else:            
            self.give_final_result(king)
        self.selected_moves_alg = []
        self.selected_moves_geo = []
        self.make_move = False
        self.refreshAll()
        
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
        self.refreshAll()
        return self.give_game_state()
    
    def user_vs_user(self):
        movement = coordinates.reconvert_to_alg(self.pos)
        self.l_valid_moves = self.give_valid_moves()
        self.l_enemy_moves = self.send_U_move(self.piece,movement)
        king = self.give_who_plays()
        if king.is_checked(self.l_enemy_moves) and \
            not self.give_game_state():
            self.model.board.history[-1] = self.model.board.history[-1] + '+'
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
        client = self.clients[1]
        if self.game_type == 1:
            if self.turn == self.user:
                game_state = self.user_move()
                self.L,game_state = self.model.board.numberOfPieces()
            if not game_state:
                client.execute_with_delay(250)
                self.IA_move(self.IA_level)
        elif self.game_type == 2:
            if self.time == 0:
                self.user_vs_user()
            else:
                self.l_valid_moves = []
                self.refreshAll()
        else:
            game_state = False
            game_state2 = False
            while (not game_state and not game_state2) and self.i<self.iMax:                
                game_state = self.IA_move(self.IA_level)
                self.L,game_state2 = self.model.board.numberOfPieces()
                client.execute_with_delay(250)
                if not game_state and not game_state2:
                    game_state = self.IA_move(self.IA2_level)
                    self.L,game_state2 = self.model.board.numberOfPieces()
                    client.execute_with_delay(250)                    
                    self.i += 1
            self.give_final_result(self.give_who_plays())            
            
    def save(self,fileName):   
        try:
            f = open(fileName, 'wb')
            pickle.dump([self.model.board.history,self.model], f)
            f.close()
            f = open(fileName, 'rb')
            obj = pickle.load(f)
            f.close()    
        except:
            pass
                
    def load(self,fileName):
        f = open(fileName, 'rb')
        obj = pickle.load(f)
        f.close()        
        self.model = obj[1]
        self.model.board.history = obj[0]
        
if __name__ == "__main__":
    pass
      
