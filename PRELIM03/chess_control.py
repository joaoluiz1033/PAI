import chess_model as ch


class ControlBase():
    
    def __init__(self):
        self.clients = list()
        self.message = ""
    
    def addClient(self,client):
        self.clients.append(client)
        
    def regreshAll(self,message):
        self.message = message
        for client in self.clients:
            client.refresh()


class Control(ControlBase):
    
    def __init__(self):
        super().__init__()
        self.board = ch.Board()
    
    def move_options(self):
        l_valid_moves = self.board.show_valid_moves()
        i = 0
        for x in l_valid_moves:
            print(i,x[0],x[1])
            i += 1
        return l_valid_moves
    
    def User_move(self,piece,move):             
        pass
  
      
if __name__ == "__main__":
    bd = Control()    
    bd.board.prt()
    