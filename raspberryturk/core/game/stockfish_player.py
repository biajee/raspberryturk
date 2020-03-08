from chess import engine

class StockfishPlayer(object):
    def __init__(self):
        self._engine = chess.engine.SimpleEngine.popen_uci('stockfish')

    def select_move(self, board):
        board = self._engine.Board(board)
        limit = chess.engine.Limit(time=2.0)
        result = self._engine.play(board, limit)
        return result.move
