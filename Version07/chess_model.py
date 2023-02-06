import numpy as np
import random
import datetime
import os
import copy
import pdb
import string

import board as bd
import pieces as pcs
import pawn as p
import rook as r
import knight as n
import bishop as b
import queen as q
import king as k
import coordinates
import chess_IA as chIA
import chess_move as chMV


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


class Game():

    def __init__(self, board: bd.Board):  # initial board with all pieces in position
        self.board = board

    def possible_moves(self):
        if self.board.who_plays == 'w':
            l_pieces = self.board.whites_in_board
        else:
            l_pieces = self.board.blacks_in_board
        l_move_poss = []
        for P in l_pieces:
            l_move_poss.append([P, P.check_moves(self.board.board_map)])
        return l_move_poss

    def change_pawn(self, position, pieces_in_board, pawn_idx, team):
        a = team
        pieces = [q.queen(a + 'q', position), n.knight(a + 'n', position), b.bishop(a + 'b', position),
                  r.rook(a + 'r', position)]
        p = random.choice(pieces)
        pieces_in_board[pawn_idx] = p
        self.board.history[-1] += '=Q'
        return [p, p.check_moves(self.board.board_map)]

    def register_en_passant(self, x, y, piece, add, enemies_board):
        X_MIN = 0
        X_MAX = 7
        if x == X_MIN:
            if self.board.board_map[y][x + 1] is not None:
                if self.board.board_map[y][x + 1].name[1] == 'p' and \
                        self.board.board_map[y][x + 1].name[0] != self.board.who_plays:
                    x_pass = x
                    y_pass = y - add
                    for enemy_p in enemies_board:
                        if enemy_p == self.board.board_map[y][x + 1]:
                            enemy_p.en_passante_moves.append(
                                coordinates.reconvert_to_alg([x_pass, y_pass]))
        elif x == X_MAX:
            if self.board.board_map[y][x - 1] is not None:
                if self.board.board_map[y][x - 1].name[1] == 'p' and \
                        self.board.board_map[y][x - 1].name[0] != self.board.who_plays:
                    x_pass = x
                    y_pass = y - add

                    for enemy_p in enemies_board:
                        if enemy_p == self.board.board_map[y][x - 1]:
                            enemy_p.en_passante_moves.append( \
                                coordinates.reconvert_to_alg([x_pass, y_pass]))
        else:
            if self.board.board_map[y][x + 1] is not None:
                if self.board.board_map[y][x + 1].name[1] == 'p' and \
                        self.board.board_map[y][x + 1].name[0] != self.board.who_plays:
                    x_pass = x
                    y_pass = y - add
                    for enemy_p in enemies_board:
                        if enemy_p == self.board.board_map[y][x + 1]:
                            enemy_p.en_passante_moves.append( \
                                coordinates.reconvert_to_alg([x_pass, y_pass]))
            if self.board.board_map[y][x - 1] is not None:
                if self.board.board_map[y][x - 1].name[1] == 'p' and \
                        self.board.board_map[y][x - 1].name[0] != self.board.who_plays:
                    x_pass = x
                    y_pass = y - add
                    for enemy_p in enemies_board:
                        if enemy_p == self.board.board_map[y][x - 1]:
                            enemy_p.en_passante_moves.append( \
                                coordinates.reconvert_to_alg([x_pass, y_pass]))
        return

    def change_who_plays(self):
        if self.board.who_plays == 'w':
            self.board.who_plays = 'b'
        else:
            self.board.who_plays = 'w'
        return self.board.who_plays

    def move_choose(self, l_possible_moves):
        a = False
        if is_empty(l_possible_moves):
            return l_possible_moves
        else:
            if self.board.who_plays == 'w':
                pieces_board = self.board.whites_in_board
                enemies_board = self.board.blacks_in_board
                king = self.board.w_king
                add = 1
            else:
                pieces_board = self.board.blacks_in_board
                enemies_board = self.board.whites_in_board
                king = self.board.b_king
                add = -1
            valid = False
            while not valid:
                i = 0
                for l in l_possible_moves:
                    print(i, l)
                    i += 1
                l = input("Choose a piece (its number): ")
                l = int(l)
                idx_pawn = l_possible_moves[l]
                piece = l_possible_moves[l][0]
                if len(l_possible_moves[l][1]) > 0:
                    valid = True
            for s in l_possible_moves[l][1]:
                print(s)
            movement = input('Choose a movement: ')
            movement_xy = coordinates.convert_to_coordinate(movement)
            x = movement_xy[0]
            y = movement_xy[1]
            old_xy = coordinates.convert_to_coordinate(piece.pos_alg)
            old_y = old_xy[1]
            old_x = old_xy[0]
            if piece in pieces_board:
                if self.board.board_map[y][x] is not None:
                    if self.board.board_map[y][x].name[1] == 'k':
                        return []
                    try:
                        enemies_board.remove(self.board.board_map[y][x])
                    except:
                        pdb.set_trace()
                else:
                    if piece.name[1] == 'p':
                        if abs(old_x - x) != 0:
                            enemies_board.remove(self.board.board_map[y - add][x])
                    elif piece.name[1] == 'k' and abs(x - old_x) == 2:
                        if x > old_x:
                            idx_rook = self.find_rook(pieces_board, 1)
                            rook_pos = coordinates.reconvert_to_alg([x - 1, y])
                            pieces_board[idx_rook].pos_alg = rook_pos
                        else:
                            idx_rook = self.find_rook(pieces_board, -1)
                            rook_pos = coordinates.reconvert_to_alg([x + 1, y])
                            pieces_board[idx_rook].pos_alg = rook_pos
                idx = pieces_board.index(piece)
                pieces_board[idx].pos_alg = movement
                piece.history_mov.append(movement)
                self.last_movement = movement
                l_possible_moves[l][1].remove(movement)
                if piece.name[1] == 'k':
                    king.pos_alg = movement
                if piece.name[1] == 'p':
                    if pieces_board[idx].at_max():
                        new_l = self.change_pawn(movement, pieces_board, \
                                                 idx, pieces_board[idx].team)
                        l_possible_moves[idx_pawn] = new_l
                    elif abs(old_y - y) == 2:
                        self.register_en_passant(x, y, piece, add, enemies_board)
            self.board.current_board()
            l_possible_moves = self.possible_moves()
            if a:
                return []
            else:
                return l_possible_moves

    def find_rook(self, pieces_board, direction):
        idx = 0
        if direction == 1:
            x_ref = 7
        else:
            x_ref = 0
        for piece in pieces_board:
            idx = pieces_board.index(piece)
            if piece.name[1] == 'r':
                x = coordinates.convert_to_coordinate(piece.pos_alg)[0]
                if x == x_ref:
                    return idx
        return idx

    def move_piece(self, piece, movement):
        if self.board.who_plays == 'w':
            pieces_board = self.board.whites_in_board
            enemies_board = self.board.blacks_in_board
            king = self.board.w_king
            add = 1
            self.board.who_plays = 'b'
        else:
            pieces_board = self.board.blacks_in_board
            enemies_board = self.board.whites_in_board
            king = self.board.b_king
            add = -1
            self.board.who_plays = 'w'
        movement_xy = coordinates.convert_to_coordinate(movement)
        x = movement_xy[0]
        y = movement_xy[1]
        old_xy = coordinates.convert_to_coordinate(piece.pos_alg)
        old_y = old_xy[1]
        old_x = old_xy[0]
        if piece in pieces_board:
            if self.board.board_map[y][x] is not None:
                if self.board.board_map[y][x].name[1] == 'k':
                    return []
                enemies_board.remove(self.board.board_map[y][x])
                eliminate = True
            else:
                if piece.name[1] == 'p':
                    if abs(old_x - x) != 0:
                        enemies_board.remove(self.board.board_map[y - add][x])
                        eliminated = True
            idx = pieces_board.index(piece)
            pieces_board[idx].pos_alg = movement
            if piece.name[1] == 'k':
                king.pos_alg = movement

        self.board.current_board()
        return

    def test_roque(self, current_x, movement_x, y, piece):
        if current_x > movement_x:
            add = -1
        else:
            add = 1
        while (current_x != movement_x):
            movement = coordinates.reconvert_to_alg([current_x, y])
            l_enemy_moves = self.possible_moves()
            if piece.is_checked(l_enemy_moves):
                return False
            current_x += add
        movement = coordinates.reconvert_to_alg([current_x, y])
        l_enemy_moves = self.possible_moves()
        if piece.is_checked(l_enemy_moves):
            return False
        else:
            return True

    def simulate_check(self, l_possible_moves):
        valid_list = []
        for pair in l_possible_moves:
            piece = pair[0]
            piece_movements = pair[1]
            piece_valid_movements = []
            for movement in piece_movements:
                test_board = copy.deepcopy(self)
                if test_board.board.who_plays == 'w':
                    king = test_board.board.w_king
                else:
                    king = test_board.board.b_king
                if piece.name[1] != 'k':
                    test_board.move_piece(piece, movement)
                    l_enemy_moves = test_board.possible_moves()
                    if not king.is_checked(l_enemy_moves):
                        piece_valid_movements.append(movement)
                else:
                    movement_x = coordinates.convert_to_coordinate(movement)[0]
                    current_x = coordinates.convert_to_coordinate(piece.pos_alg)[0]
                    y = coordinates.convert_to_coordinate(piece.pos_alg)[1]
                    if abs(movement_x - current_x == 2):
                        valid_roque = test_board.test_roque(current_x, movement_x, y, piece)
                        if valid_roque:
                            piece_valid_movements.append(movement)
                    else:
                        test_board.move_piece(piece, movement)
                        l_enemy_moves = test_board.possible_moves()
                        if not king.is_checked(l_enemy_moves):
                            piece_valid_movements.append(movement)
            valid_list.append([piece, piece_valid_movements])
        return valid_list

    def game(self):
        l_enemy_moves = []
        end_game = False
        i = 0
        while not end_game and i < 1000:
            self.prt()
            if self.board.who_plays == 'w':
                king = self.board.w_king
            else:
                king = self.board.b_king
            l_possible_moves = self.possible_moves()
            l_valid_moves = self.simulate_check(l_possible_moves)
            if is_empty(l_valid_moves):
                if king.is_checked(l_enemy_moves):
                    print(f"Check Mate: {king}")
                else:
                    print(f"{self.board.who_plays} cannot move")
                end_game = True
            else:
                if self.board.who_plays == 'w':
                    l_enemy_moves = self.move_choose(l_valid_moves)
                else:
                    l_enemy_moves = chMV.moveIA_view(self, \
                                                     2, l_valid_moves, l_enemy_moves)
                l_enemy_moves = self.simulate_check(l_enemy_moves)
                self.change_who_plays()
            i += 1
        if end_game:
            return
        else:
            print('Maximum iteration number')

    def show_valid_moves(self):
        l_possible_moves = self.possible_moves()
        l_valid_moves = self.simulate_check(l_possible_moves)
        return l_valid_moves

    def move_User(self, l_possible_moves, piece, movement):
        return chMV.move_piece_view(self, l_possible_moves, piece, movement)

    def move_IA(self, level, l_possible_moves, l_enemy_moves):
        return chMV.moveIA_view(self, level, l_possible_moves, l_enemy_moves)


if __name__ == "__main__":
    l = ['wpe4', 'bpa6', 'wbc4', 'bpa5', 'wqf3', 'bpa4', 'wqf7']
    l_new = []
    print(l)
