import sys
import chess_model as ch
import pdb


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
        self.IA_level = 2
        self.user = 'w'
        self.move_history = []
    
    def give_valid_moves(self):
        l_possible_moves = self.board.possible_moves()            
        l_valid_moves = self.board.simulate_check(l_possible_moves)        
        return l_valid_moves
    
    def give_map(self):
        return self.board.board_map
    
    def give_map_board(self):
        self.board.prt()
        return 
    
    def give_who_plays(self): 
        return self.board.who_plays()
    
    def give_game_state(self,l_valid_moves):
        end_game = False
        if ch.is_empty(l_valid_moves):                                
            end_game = True
        return end_game
    
    def give_final_result(self,l_enemy_moves,king):        
        if king.is_checked(l_enemy_moves):
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
        
    def send_U_move(self, piece, movement,l_possible_moves):
        l_enemy_moves = self.board.move_User(l_possible_moves,piece,movement)
        l_enemy_moves = self.board.simulate_check(l_enemy_moves)
        self.board.change_who_plays()        
        return l_enemy_moves
    
    def send_IA_move(self,l_possible_moves,l_enemy_moves):
        l_enemy_moves = self.board.move_IA(self.IA_level,l_possible_moves,\
                                        l_enemy_moves)
        l_enemy_moves = self.board.simulate_check(l_enemy_moves)
        self.board.change_who_plays()  
        self.refreshAll()
        return l_enemy_moves

if __name__ == "__main__":
    pass
      
