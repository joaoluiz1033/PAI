import chess_model as chMD
import coordinates
import pdb
import copy

def move_conquerIA(board,piece,movement,l_possible_moves):
    a = False       
    if chMD.is_empty(l_possible_moves):
        return l_possible_moves
    else:            
        if board.who_plays == 'w':
            pieces_board = board.whites_in_board
            enemies_board = board.blacks_in_board
            king = board.w_king
            add = 1
        else:
            pieces_board = board.blacks_in_board
            enemies_board = board.whites_in_board
            king = board.b_king
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
        if piece in pieces_board:                               
            if board.board_map[y][x] is not None:
                score_piece_removed = board.board_map[y][x].score                    
                if board.board_map[y][x].name[1] == 'k':
                    return [] 
                try:
                    enemies_board.remove(board.board_map[y][x])
                except:
                    pdb.set_trace()                    
            else:
                if piece.name[1] == 'p':
                    if abs(old_x - x) != 0:                            
                        enemies_board.remove(board.board_map[y-add][x]) 
                elif  piece.name[1] == 'k' and abs(x - old_x) == 2:
                    if x > old_x:
                        idx_rook = board.find_rook(pieces_board, 1)
                        rook_pos = coordinates.reconvert_to_alg([x-1,y])
                        pieces_board[idx_rook].pos_alg = rook_pos
                    else:
                        idx_rook = board.find_rook(pieces_board, -1) 
                        rook_pos = coordinates.reconvert_to_alg([x+1,y])
                        pieces_board[idx_rook].pos_alg = rook_pos
            idx = pieces_board.index(piece)
            pieces_board[idx].pos_alg = movement
            piece.history_mov.append(movement)                
            board.last_movement = movement
            l[1].remove(movement)
            if piece.name[1] == 'k':
                king.pos_alg = movement          
            if piece.name[1] == 'p':                   
                if pieces_board[idx].at_max():                        
                    new_l = board.change_pawn(movement,pieces_board,\
                      idx,pieces_board[idx].team )                           
                    l_possible_moves[idx_pawn] = new_l                  
                elif abs(old_y - y) == 2:                        
                    board.register_en_passant(x,y,piece,add,enemies_board)
        board.current_board()
        l_possible_moves = board.possible_moves()
        
        if a:
            return []
        else:
            return [l_possible_moves,score_piece_removed]
