from raspberryturk import lib_path
from raspberryturk.core.vision.helpers import possible_moves_for_board, \
                                              pawn_board_from_colored_board_mask
from raspberryturk.core.game.stockfish_player import StockfishPlayer
from raspberryturk.embedded import game
from raspberryturk.embedded.vision.chess_camera import ChessCamera
from raspberryturk.embedded.motion.coordinator import Coordinator

import io
import chess
import time
import logging

NUM_REQUIRED_MATCHING_CANDIDATES = 2

class Agent(object):
    def __init__(self):
        self._chess_camera = ChessCamera()
        self._motion_coordinator = None
        self._logger = logging.getLogger(__name__)
        self._player = StockfishPlayer()

    def __enter__(self):
        self._motion_coordinator = Coordinator()
        self._motion_coordinator.reset()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._motion_coordinator.close()
        self._motion_coordinator = None
        return False

    def _candidate_move(self):
        cbm = self._chess_camera.current_colored_board_mask()
        b = game.get_board()
        moves = possible_moves_for_board(b, cbm)
        return moves[0] if moves else None

    def _next_move(self):
        candidates = []
        for i in range(NUM_REQUIRED_MATCHING_CANDIDATES):
            candidates.append(self._candidate_move())
            time.sleep(2)
        return candidates[0] if len(set(candidates)) == 1 else None

    def _write_status(self):
        b = game.get_board()
        cbm = self._chess_camera.current_colored_board_mask()
        cbm_board = pawn_board_from_colored_board_mask(cbm)
        pgn = game.pgn()
        formatted_datetime = time.strftime("%x %X")
        text = str("\n\n").join([formatted_datetime, str(cbm_board), str(b), pgn])
        with io.open(lib_path('status.txt'), 'w', encoding='utf8') as f:
            f.write(text)

    def perception_action_sequence(self):
        b = game.get_board()
        if b.is_game_over():
            self._logger.info("Game has ended, result: {}".format(b.result()))
            game.start_new_game()
        elif b.turn == chess.WHITE:
            m = self._next_move()
            if m is not None:
                game.apply_move(m)
        else:
            m = self._player.select_move(b)
            self._motion_coordinator.move_piece(m, b)
            game.apply_move(m)
        self._write_status()
