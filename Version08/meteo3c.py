from meteom import * 

class ControlerBase:
    
    def __init__(self):
        self.clients = list()
        self.message = ""

    def addClient(self, client):
        self.clients.append(client)
        # print(client)        

    def refreshAll(self, message):
        self.message = message
        # print(self.clients)        
        for client in self.clients:            
            client.refresh()


class Controler(ControlerBase):
    
    def __init__(self):
        super().__init__()
        self.towns = loadlistoftowns()        
        self.town = None
        self.data = None
        self.date = None
        self.select_town_by_name('NICE')
        
    def select_town_by_name(self,name):
        self.town=name
        code=self.towns
        filename=f'.csv'
        self.data=readsynopfile(filename)
        self.refreshAll(f'Nouvelle ville selectionnee ')
        
    def select_date(self, date):
        self.date = date  
        self.refreshAll("nouvelle date selectionnee: ")
        
        