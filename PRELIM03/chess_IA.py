import random
import pdb
import copy

import chess_model as chMD
import chess_move as chMV
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
    return [l,idx_pawn,piece,movement]

def conquer_mid(board,possible_moves,enemy_moves):
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
            board_test = copy.deepcopy(board)            
            infos = chMV.move_conquerIA(board_test,piece,movement,possible_moves)
            score_piece_removed = infos[1]
            score += score_piece_removed
            l_to_seecheck = infos[0]
            board_test.change_who_plays()
            if board_test.who_plays == 'w':
                king = board_test.w_king
            else:
                king = board_test.b_king
            if king.is_checked(l_to_seecheck):
                score += 1            
    l_movements_scored.sort(key=take_third,reverse=True)
    vec = l_movements_scored[0]
    for elem in possible_moves:
        if elem[0] == vec[0]:
            idx_pawn = possible_moves.index(elem)
    piece = vec[0]
    movement = vec[1]
    l = possible_moves[idx_pawn]
    return [l,idx_pawn,piece,movement]

def minimax():
    return

def moveIA(board,level,possible_moves,enemy_moves):
    if level == 1:
        l_infos =random_move(possible_moves,enemy_moves)
        return l_infos
    elif level == 2:
        l_infos = conquer_mid(board,possible_moves,enemy_moves)
        return l_infos
    elif level == 3:
        l_infos = minimax()
        return l_infos
    
        
def test():
    return [1,2,3]
    
if __name__ == "__main__":
    a = test()[0]
    print(type(a))