import random
import pdb
import copy

import chess_model as chMD
import chess_move as chMV
import coordinates 

CENTER = 4

def debug_trace():
    from PyQt5.QtCore import pyqtRemoveInputHook
    from pdb import set_trace
    pyqtRemoveInputHook()
    set_trace()
    
def is_empty(l): 
    i = 0
    if len(l) == 0 or l is None:
        return True
    else:        
        for x in l:                        
            piece = x[0]
            movements = x[1]
            if len(movements) == 0:
                i += 1
        if i == len(l):            
            return True
        else: 
            return False  

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


def easyLevel(board,possible_moves,enemy_moves):
    l_movements_scored = []
    max_piece = 9
    for pair in possible_moves:
        piece = pair[0]
        for movement in pair[1]:
            score = 0
            danger = False
            piece_xy = coordinates.convert_to_coordinate(piece.pos_alg)
            movement_xy = coordinates.convert_to_coordinate(movement)
            x = CENTER - movement_xy[0]
            y = CENTER - movement_xy[1]            
            if piece.in_danger(movement,enemy_moves):
                score -= 9/piece.score
                danger = True
            board_test = copy.deepcopy(board)            
            if piece.name[1] == 'p':
                if piece.next_at_max:
                    score += 1
            infos = chMV.move_conquerIA(board_test,piece,movement,possible_moves)
            try:
                score_piece_removed = infos[1]
            except:
                debug_trace()
            if score_piece_removed > 0:
                score += score_piece_removed 
            l_to_seecheck = infos[2]
            board_test.change_who_plays()
            if board_test.board.who_plays == 'w':
                king = board_test.board.w_king
            else:
                king = board_test.board.b_king
            if king.is_checked(l_to_seecheck) and not danger:
                score += 1 + 1/piece.score 
            if piece.global_score != 0 :
                score = score/piece.global_score
            piece.global_score = score            
            l_score = [piece,movement,score]
            l_movements_scored.append(l_score)
    l_movements_scored.sort(key=take_third,reverse=True)
    score_max = l_movements_scored[0][2]
    l_movements_max = []
    for list_movements in l_movements_scored:
        if list_movements[2] == score_max:
            l_movements_max.append(list_movements)
    vec = random.choice(l_movements_max)   
    for elem in infos[0]:
        if elem[0] == vec[0]:
            idx_pawn = possible_moves.index(elem)
    piece = vec[0]
    movement = vec[1]    
    try:
        l = possible_moves[idx_pawn]
    except:
        l = infos[2][idx_pawn]
    return [l,idx_pawn,piece,movement]


def mediumLevelDepth(board,possible_moves,enemy_moves):
    l_movements_scored = []
    max_piece = 9
    for pair in possible_moves:
        piece = pair[0]
        for movement in pair[1]:
            score = 0
            danger = False
            piece_xy = coordinates.convert_to_coordinate(piece.pos_alg)
            movement_xy = coordinates.convert_to_coordinate(movement)
            x = CENTER - movement_xy[0]
            y = CENTER - movement_xy[1]            
            if piece.in_danger(movement,enemy_moves):
                score -= 9/piece.score
                danger = True
            board_test = copy.deepcopy(board)            
            if piece.name[1] == 'p':
                if piece.next_at_max():
                    score += 1
            infos = chMV.move_conquerIA(board_test,piece,movement,possible_moves)
            try:
                score_piece_removed = infos[1]
            except:
                debug_trace()
            if score_piece_removed > 0:
                score += score_piece_removed 
            l_to_seecheck = infos[2]
            board_test.change_who_plays()
            if board_test.board.who_plays == 'w':
                king = board_test.board.w_king
            else:
                king = board_test.board.b_king
            if king.is_checked(l_to_seecheck) and not danger:
                score += 1 + 1/piece.score 
            if piece.global_score != 0 :
                score = score/piece.global_score
            piece.global_score = score            
            l_score = [piece,movement,score]
            l_movements_scored.append(l_score)
    lMovementsScore = copy.deepcopy(l_movements_scored)    
    for trio in lMovementsScore:
        piece2 = trio[0]
        movement2 = trio[1]        
        gameCopy = copy.deepcopy(board)
        gameCopy.move_piece(piece2,movement2)
        gameCopy.change_who_plays()
        enemyMoves = gameCopy.possible_moves()
        enemyMoves = gameCopy.simulate_check(enemyMoves)
        gameCopy.change_who_plays()
        depthMoves = gameCopy.possible_moves()
        depthMoves =  gameCopy.simulate_check(depthMoves)
        if len(depthMoves) > 0 and not is_empty(depthMoves):            
            l_movements_scoredFake = []            
            for pair in depthMoves:
                piece = pair[0]
                for movement in pair[1]:                    
                    scoreFake = 0
                    danger = False
                    piece_xy = coordinates.convert_to_coordinate(\
                                                         piece.pos_alg)
                    movement_xy = coordinates.convert_to_coordinate(\
                                                            movement)
                    x = CENTER - movement_xy[0]
                    y = CENTER - movement_xy[1]            
                    if piece.in_danger(movement,enemyMoves):                    
                        scoreFake -= 9/piece.score
                        danger = True
                    board_test = copy.deepcopy(gameCopy)
                    if piece.name[1] == 'p':
                        if piece.next_at_max():
                            scoreFake += 1
                    infosFake = chMV.move_conquerIA(board_test,\
                                                piece,movement,depthMoves)
                    try:
                        score_piece_removed = infosFake[1]
                    except:
                        debug_trace()
                    if score_piece_removed > 0:
                        scoreFake += score_piece_removed 
                    l_to_seecheck = infosFake[2]
                    board_test.change_who_plays()
                    if board_test.board.who_plays == 'w':
                        king = board_test.board.w_king
                    else:
                        king = board_test.board.b_king
                    if king.is_checked(l_to_seecheck) and not danger:
                        scoreFake += 1 + 1/piece.score 
                    if piece.global_score != 0 :
                        scoreFake = scoreFake/piece.global_score
                    piece.global_score = scoreFake            
                    l_score = [piece,movement,scoreFake]
                    l_movements_scoredFake.append(l_score)       
            l_movements_scoredFake.sort(key=take_third,reverse = True)
            try:
                score_max = l_movements_scoredFake[0][2]
            except:
                debug_trace()
            trio[2] += score_max 
        else:            
            trio[2] = 2*trio[2]    
    l_movements_min = []
    lMovementsScore.sort(key=take_third)
    score_min =  lMovementsScore[0][2]
    l_movements_min = []
    for list_movements in lMovementsScore:
        if list_movements[2] == score_min:
            l_movements_min.append(list_movements)
    vec = random.choice(l_movements_min)   
    for elem in infos[0]:
        if elem[0] == vec[0]:
            idx_pawn = possible_moves.index(elem)
    piece = vec[0]
    movement = vec[1]    
    try:
        l = possible_moves[idx_pawn]
    except:
        l = infos[2][idx_pawn]
    return [l,idx_pawn,piece,movement]


def mediumLevel(board,possible_moves,enemy_moves):
    l_movements_scored = []
    max_piece = 9
    for pair in possible_moves:
        piece = pair[0]
        actual_danger = False
        piece_xy = coordinates.convert_to_coordinate(piece.pos_alg)
        if piece.in_danger(piece_xy,enemy_moves):
            actual_danger = True            
        for movement in pair[1]:
            score = piece.global_score           
            movement_xy = coordinates.convert_to_coordinate(movement)
            if actual_danger:
                score += 11*piece.score 
            board_test = copy.deepcopy(board)            
            if piece.name[1] == 'p':
                if piece.next_at_max:
                    score += 10
            infos = chMV.move_conquerIA(board_test,piece,movement,possible_moves)
            try:
                score_piece_removed = infos[1]
            except:
                debug_trace()            
            l_to_seecheck = infos[2]
            board_test.change_who_plays()
            if board_test.board.who_plays == 'w':
                king = board_test.board.w_king
            else:
                king = board_test.board.b_king
            m = board_test.possible_moves()
            m = board_test.simulate_check(m)
            danger = piece.in_danger(movement,m)
            if danger:
                score -= 10*piece.score
                danger = True
            if score_piece_removed > 0:
                if not danger:
                    score += 10*(score_piece_removed/piece.score)                    
                else:
                    score -= 10*(score_piece_removed/piece.score)
            if king.is_checked(l_to_seecheck) :               
                if not danger:                    
                    score += 10*piece.score
                else:
                    score -= 100*piece.score
            l_score = [piece,movement,score]
            l_movements_scored.append(l_score)
    l_movements_scored.sort(key=take_third,reverse=True)
    score_max = l_movements_scored[0][2]
    l_movements_max = []
    for list_movements in l_movements_scored:
        possible_danger = list_movements[1]
        if not piece.in_danger(movement,enemy_moves):
            if list_movements[2] == score_max:
                l_movements_max.append(list_movements)
    if len(l_movements_max) == 0:
        for list_movements in l_movements_scored:
            if list_movements[2] == score_max:
                l_movements_max.append(list_movements)
    vec = random.choice(l_movements_max)   
    for elem in infos[0]:
        if elem[0] == vec[0]:
            idx_pawn = possible_moves.index(elem)
    piece = vec[0]
    movement = vec[1]
    # if piece.global_score != 0 :
    #     score = vec[2]/(piece.global_score)
    # piece.global_score = score 
    try:
        l = possible_moves[idx_pawn]
    except:
        l = infos[2][idx_pawn]
    return [l,idx_pawn,piece,movement]

def moveIA(board,level,possible_moves,enemy_moves):
    if level == 1:
        l_infos =random_move(possible_moves,enemy_moves)
        return l_infos
    elif level == 2:
        l_infos = easyLevel(board,possible_moves,enemy_moves)
        return l_infos
    elif level == 3:
        l_infos = mediumLevel(board,possible_moves,enemy_moves)
        return l_infos
    
        
def test():
    return [1,2,3]
    
if __name__ == "__main__":
    a = test()[0]
    print(type(a))