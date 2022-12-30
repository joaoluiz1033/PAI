import random 

def random_move(possible_moves):
    valid = False
    while not valid:
        l = random.choice(possible_moves)
        idx_pawn = possible_moves.index(l)
        piece = l[0]
        if len(l[1]) > 0:
            valid = True                    
    movement = random.choice(l[1])
    return [l,idx_pawn,piece,movement]

def conquer_midle(possible_moves):
    for pair in possible_moves:
        pass
    return

def minimax():
    return

def moveIA(level,possible_moves):
    if level == 1:
        l_infos =random_move(possible_moves)
        return l_infos
    elif level == 2:
        l_infos = conquer_midle()
        return l_infos
    elif level == 3:
        l_infos = minimax()
        return l_infos
    
        
def test():
    return [1,2,3]
    
if __name__ == "__main__":
    a = test()[0]
    print(type(a))