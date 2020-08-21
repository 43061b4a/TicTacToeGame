import random


class TicTacToe:

    def __init__(self):
        super().__init__()
        self.board_state = [None for _ in range(9)]
        self.board_with_locations = [str(i + 1) for i in range(9)]

    def draw(self, state=True):
        board = ""
        state = self.board_state if state is True else self.board_with_locations
        for i in range(5):
            if i % 2 == 0:
                row = i // 2
                mid = " | ".join([" " if state[row + i] is None else state[row + i] for i in range(i, i + 3)])
                board += "| " + mid + " |"
            else:
                board += "----" * 3
            board += "\n"
        return board

    def turn(self, position, symbol):
        if position > 9 or position < 1 or self.board_state[position - 1] is not None:
            raise ValueError("Invalid position or {position} position is already taken.")
        else:
            self.board_state[position - 1] = symbol

    def all_positions_taken(self):
        all_taken = True
        if len([x for x in self.board_state if x is None]) > 0:
            all_taken = False
        return all_taken

    def check(self, symbol):
        grid_size = 3

        if self._check_columns(grid_size, symbol):
            return True

        if self._check_rows(grid_size, symbol):
            return True

        if self._check_diag(grid_size, symbol):
            return True

        if self._check_anti_diag(grid_size, symbol):
            return True

        return False

    def _check_anti_diag(self, grid_size, symbol):
        anti_diag = False
        symbol_count = 0
        for i in range(grid_size - 1, grid_size * 2 + 1, grid_size - 1):
            if self.board_state[i] == symbol:
                symbol_count += 1
            if symbol_count == grid_size:
                anti_diag = True
        return anti_diag

    def _check_diag(self, grid_size, symbol):
        diag_check = False
        symbol_count = 0
        for i in range(0, grid_size ** 2, grid_size + 1):
            if self.board_state[i] == symbol:
                symbol_count += 1
            if symbol_count == grid_size:
                diag_check = True
        return diag_check

    def _check_rows(self, grid_size, symbol):
        for i in range(0, grid_size ** 2, 3):
            symbol_count = len([x for x in self.board_state[i:i + grid_size] if x == symbol])
            if symbol_count == grid_size:
                return True
        return False

    def _check_columns(self, grid_size, symbol):
        for i in range(grid_size):
            symbol_count = 0
            for j in range(0, 2 * grid_size + 1, grid_size):
                if self.board_state[i + j] == symbol:
                    symbol_count += 1
            if symbol_count == grid_size:
                return True
        return False
