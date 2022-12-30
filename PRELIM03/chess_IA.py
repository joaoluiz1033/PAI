import random
import pdb
import math

import chess_model as chMD
import coordinates 

CENTER = 4


def take_third(elem):
    return elem[2]

def random_move(possible_moves,enemy_moves):
    valid = False
    while not valid:
        l = random.choice(possible_moves)
        idx_pawn = possible_moves.index(l)
        piece = l[0]
        if len(l[1]) > 0:
            valid = True                    
    movement = random.choice(l[1])
    conquer_mid(possible_moves,enemy_moves)
    return [l,idx_pawn,piece,movement]

def conquer_mid(possible_moves,enemy_moves):
    l_movements_scored = []
    for pair in possible_moves:
        piece = pair[0]
        for movement in pair[1]:
            score = piece.score
            piece_xy = coordinates.convert_to_coordinate(piece.pos_alg)
            movement_xy = coordinates.convert_to_coordinate(movement)
            x = CENTER - movement_xy[0]
            y = CENTER - movement_xy[1]
            score -= (x**2 + y**2)
            l_score = [piece,movement,score]
            l_movements_scored.append(l_score)
            if piece.in_danger(movement,enemy_moves):
                score -= piece.score/2 
    l_movements_scored.sort(key=take_third,reverse=True)
    l = l_movements_scored[0:2]
    pdb.set_trace()
    return

def minimax():
    return

def moveIA(level,possible_moves,enemy_moves):
    if level == 1:
        l_infos =random_move(possible_moves,enemy_moves)
        return l_infos
    elif level == 2:
        l_infos = conquer_mid(possible_moves,enemy_moves)
        return l_infos
    elif level == 3:
        l_infos = minimax()
        return l_infos
    
        
def test():
    return [1,2,3]
    
if __name__ == "__main__":
    a = test()[0]
    print(type(a))