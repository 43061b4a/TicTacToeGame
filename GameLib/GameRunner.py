import random
from GameLib.TicTacToe import TicTacToe


class GameRunner:

    def __init__(self):
        super().__init__()
        self.game = TicTacToe()
        self.player_count = 2
        self.current_player = random.randint(0, self.player_count - 1)
        self.symbols = ['✕', '◉']

    def get_current_player(self):
        return self.current_player

    def get_current_player_symbol(self):
        return self.symbols[self.current_player]

    def take_turn(self, position):
        if not self.game.all_positions_taken():
            self.game.turn(position, self.symbols[self.current_player])
            self.current_player = (self.current_player + 1) % self.player_count
            return True
        else:
            return False

    def get_winner(self):
        result = []
        for i in range(self.player_count):
            if self.game.check(self.symbols[i]):
                result.append(i)
        return result
