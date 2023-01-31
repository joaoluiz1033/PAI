import chess_model as chMD
import chess_IA as chIA
import coordinates
import pdb
import copy

def debug_trace():
    from PyQt5.QtCore import pyqtRemoveInputHook
    from pdb import set_trace
    pyqtRemoveInputHook()
    set_trace()

def move_conquerIA(game_model,piece,movement,l_possible_moves):
    a = False       
    if chMD.is_empty(l_possible_moves):
        return l_possible_moves
    else:            
        if game_model.board.who_plays == 'w':
            pieces_game_model = game_model.board.whites_in_board
            enemies_game_model = game_model.board.blacks_in_board
            king = game_model.board.w_king
            add = 1
        else:
            pieces_game_model = game_model.board.blacks_in_board
            enemies_game_model = game_model.board.whites_in_board
            king = game_model.board.b_king
            add = -1  
        for elem in l_possible_moves:
            if elem[0] == piece:
                idx_pawn = l_possible_moves.index(elem)
                l = copy.deepcopy(l_possible_moves[idx_pawn])
        movement_xy = coordinates.convert_to_coordinate(movement)
        x = movement_xy [0]
        y = movement_xy [1]            
        old_xy = coordinates.convert_to_coordinate(piece.pos_alg)
        old_y = old_xy[1]
        old_x = old_xy[0]    
        score_piece_removed = 0                    
        if piece in pieces_game_model:                               
            if game_model.board.board_map[y][x] is not None:
                score_piece_removed = game_model.board.board_map[y][x].score                    
                if game_model.board.board_map[y][x].name[1] == 'k':
                    return [] 
                try:
                    enemies_game_model.remove(game_model.board.board_map[y][x])
                except:
                    pdb.set_trace()                    
            else:
                if piece.name[1] == 'p':
                    if abs(old_x - x) != 0:                            
                        enemies_game_model.remove(game_model.board.board_map[y-add][x]) 
                elif  piece.name[1] == 'k' and abs(x - old_x) == 2:
                    if x > old_x:
                        idx_rook = game_model.find_rook(pieces_game_model, 1)
                        rook_pos = coordinates.reconvert_to_alg([x-1,y])
                        pieces_game_model[idx_rook].pos_alg = rook_pos
                    else:
                        idx_rook = game_model.find_rook(pieces_game_model, -1) 
                        rook_pos = coordinates.reconvert_to_alg([x+1,y])
                        pieces_game_model[idx_rook].pos_alg = rook_pos
            idx = pieces_game_model.index(piece)
            pieces_game_model[idx].pos_alg = movement
            piece.history_mov.append(movement)                
            game_model.last_movement = movement
            if elem[0] == piece:
                l[1].remove(movement)
            if piece.name[1] == 'k':
                king.pos_alg = movement          
            if piece.name[1] == 'p':                   
                if pieces_game_model[idx].at_max():                        
                    new_l = game_model.change_pawn(movement,pieces_game_model,\
                      idx,pieces_game_model[idx].team ) 
                    try:
                        l_possible_moves2 = copy.deepcopy(l_possible_moves)                          
                        l_possible_moves2[idx_pawn] = new_l
                    except:
                        debug_trace()
                elif abs(old_y - y) == 2:                        
                    game_model.register_en_passant(x,y,piece,add,enemies_game_model)
        game_model.board.current_board()
        l_possible_moves2 = game_model.possible_moves()
        
        if a:
            return []
        else:
            return [l_possible_moves,score_piece_removed,l_possible_moves2]

def move_piece_view(game_model,l_possible_moves,piece,movement):    
    a = False    
    eliminated = False
    roque1 = False
    roque2 = False
    constant = ''
    if chMD.is_empty(l_possible_moves):
        return l_possible_moves
    else:            
        if game_model.board.who_plays == 'w':
            pieces_game_model = game_model.board.whites_in_board
            enemies_game_model = game_model.board.blacks_in_board
            king = game_model.board.w_king
            add = 1
        else:
            pieces_game_model = game_model.board.blacks_in_board
            enemies_game_model = game_model.board.whites_in_board
            king = game_model.board.b_king
            add = -1
        for elem in l_possible_moves:
            if elem[0] == piece:
                idx_pawn = l_possible_moves.index(elem)
                l = copy.deepcopy(l_possible_moves[idx_pawn])    
        movement_xy = coordinates.convert_to_coordinate(movement)
        x = movement_xy [0]
        y = movement_xy [1]            
        old_xy = coordinates.convert_to_coordinate(piece.pos_alg)
        old_y = old_xy[1]
        old_x = old_xy[0]                        
        if piece in pieces_game_model:                                   
            if game_model.board.board_map[y][x] is not None:                    
                if game_model.board.board_map[y][x].name[1] == 'k':
                    return [] 
                try:
                    enemies_game_model.remove(game_model.board.board_map[y][x])
                    eliminated = True
                except:
                    debug_trace()                    
            else:
                if piece.name[1] == 'p':
                    if abs(old_x - x) != 0 and not eliminated:                            
                        enemies_game_model.remove(game_model.board.board_map[y-add][x])
                        eliminated = True
                elif  piece.name[1] == 'k' and abs(x - old_x) == 2:
                    if x > old_x:
                        roque1 = True
                        idx_rook = game_model.find_rook(pieces_game_model, 1)
                        rook_pos = coordinates.reconvert_to_alg([x-1,y])
                        pieces_game_model[idx_rook].pos_alg = rook_pos
                    else:
                        roque2 = True
                        idx_rook = game_model.find_rook(pieces_game_model, -1) 
                        rook_pos = coordinates.reconvert_to_alg([x+1,y])
                        pieces_game_model[idx_rook].pos_alg = rook_pos
            idx = pieces_game_model.index(piece)
            pieces_game_model[idx].pos_alg = movement
            piece.history_mov.append(movement)                
            game_model.last_movement = movement
            if piece.name[1] == 'k':
                king.pos_alg = movement          
            if piece.name[1] == 'p':                   
                if pieces_game_model[idx].at_max():                        
                    new_l = game_model.change_pawn(movement,pieces_game_model,\
                      idx,pieces_game_model[idx].team )                           
                    l_possible_moves[idx_pawn] = new_l                  
                elif abs(old_y - y) == 2:                        
                    game_model.register_en_passant(x,y,piece,add,enemies_game_model)
        game_model.board.current_board()
        l_possible_moves = game_model.possible_moves()     
        if eliminated:
            constant = 'X'            
        elif roque1:
            constant = 'O-O'
        elif roque2:
            constant = 'O-O-O'
        game_model.board.history.append(piece.name+movement+constant)
        if a:
            return []
        else:
            return l_possible_moves
        
def moveIA_view(game_model,level,l_possible_moves,l_enemy_moves):
    a = False
    eliminated = False
    roque1 = False
    roque2 = False
    constant = ''
    if chMD.is_empty(l_possible_moves):
        return l_possible_moves
    else:            
        if game_model.board.who_plays == 'w':
            pieces_game_model = game_model.board.whites_in_board
            enemies_game_model = game_model.board.blacks_in_board
            king = game_model.board.w_king
            add = 1
        else:
            pieces_game_model = game_model.board.blacks_in_board
            enemies_game_model = game_model.board.whites_in_board
            king = game_model.board.b_king
            add = -1
        l_infos = chIA.moveIA(game_model,level,l_possible_moves,l_enemy_moves)
        l = l_infos[0]
        idx_pawn = l_infos[1]
        piece = l_infos[2]
        movement = l_infos[3]
        movement_xy = coordinates.convert_to_coordinate(movement)
        x = movement_xy [0]
        y = movement_xy [1]            
        old_xy = coordinates.convert_to_coordinate(piece.pos_alg)
        old_y = old_xy[1]
        old_x = old_xy[0]                 
        if piece in pieces_game_model:                              
            if game_model.board.board_map[y][x] is not None:                    
                if game_model.board.board_map[y][x].name[1] == 'k':
                    return []  
                enemies_game_model.remove(game_model.board.board_map[y][x]) 
                eliminate = True                   
            else:
                if piece.name[1] == 'p':
                    if abs(old_x - x) != 0:                            
                        enemies_game_model.remove(game_model.board.board_map[y-add][x])
                        eliminated = True
                elif  piece.name[1] == 'k' and abs(x - old_x) == 2:
                    if x > old_x:
                        roque1 = True
                        idx_rook = game_model.find_rook(pieces_game_model, 1)
                        rook_pos = coordinates.reconvert_to_alg([x-1,y])
                        pieces_game_model[idx_rook].pos_alg = rook_pos
                    else:
                        roque2 = True
                        idx_rook = game_model.find_rook(pieces_game_model, -1) 
                        rook_pos = coordinates.reconvert_to_alg([x+1,y])
                        pieces_game_model[idx_rook].pos_alg = rook_pos
            idx = pieces_game_model.index(piece)
            pieces_game_model[idx].pos_alg = movement
            piece.history_mov.append(movement)                
            game_model.last_movement = movement
            l[1].remove(movement)
            if piece.name[1] == 'k':
                king.pos_alg = movement         
            if piece.name[1] == 'p':                   
                if pieces_game_model[idx].at_max():                        
                    new_l = game_model.change_pawn(movement,pieces_game_model,\
                      idx,pieces_game_model[idx].team )                           
                    l_possible_moves[idx_pawn] = new_l                
                elif abs(old_y - y) == 2:
                    game_model.register_en_passant(x,y,piece,add,enemies_game_model)
        game_model.board.current_board()
        l_possible_moves = game_model.possible_moves() 
        if eliminated:
            constant = 'X'            
        elif roque1:
            constant = 'O-O'
        elif roque2:
            constant = 'O-O-O'        
        game_model.board.history.append(piece.name+movement+constant)        
        if a:
            return []
        else:
            return l_possible_moves
        
