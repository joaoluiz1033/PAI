import chess_model as ch


class ControlerBase():
    
    def __init__(self):
        self.clients = list()
        self.message = ""
    
    def addClient(self,client):
        self.clients.append(client)
        
    def refreshAll(self,message):
        self.message = message
        for client in self.clients:
            client.refresh()


class Controler(ControlerBase):
    
    def __init__(self):
        super().__init__()
        self.board = ch.Board()
    
    def give_valid_moves(self):
        l_possible_moves = self.board.possible_moves()            
        l_valid_moves = self.board.simulate_check(l_possible_moves)
        i = 0
        for x in l_valid_moves:            
            print(f"{i} -> ",x[0],x[1])
            i += 1
        return l_valid_moves
    
    def give_map_board(self):
        self.board.prt()
        return
    
    def give_who_plays(self):
        pl = self.board.who_plays()
        return pl
    
    def give_game_state(self,l_valid_moves):
        end_game = False
        if self.board.who_plays == 'w':
            king = self.board.w_king
        else:
            king = self.board.b_king
        if ch.is_empty(l_valid_moves):                                
            end_game = True
        return end_game
    
    def give_final_result(self,l_enemy_moves,king):        
        if ch.king.is_checked(l_enemy_moves):
            print(f"Check Mate: {ch.king}")
        else:                    
            print(f"{self.who_plays} cannot move")
        
    def send_U_move(self, piece, movement,l_possible_moves):
        l_enemy_moves = self.board.move_piece_view(l_possible_moves,piece,movement)
        l_enemy_moves = self.board.simulate_check(l_enemy_moves)
        self.board.change_who_plays()        
        return l_enemy_moves
    
    def send_IA_move(self,l_possible_moves):
        l_enemy_moves = self.board.move(l_possible_moves)
        l_enemy_moves = self.board.simulate_check(l_enemy_moves)
        self.board.change_who_plays()
        return l_enemy_moves

    
      
