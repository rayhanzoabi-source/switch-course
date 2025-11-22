from Matrix import Matrix
import random
class GoldRush(Matrix):
    WALL = "wall"
    EMPTY = "."
    COIN = "coin"
    PLAYER1 = "player1"
    PLAYER2 = "player2"
    WINNING_SCORE = 100
    POINTS_PER_COIN = 10
    MIN_COINS = 10
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.player1_score = 0
        self.player2_score = 0
        self.winner = ""
        self.coins = 0
        
    def load_board(self):
        """Creates a board with walls, coins and empty spaces. Ensures at least MIN_COINS exist."""
        if self.rows == 0 or self.cols == 0:
            self.matrix = []
            return
        while True:  # regenerate until enough coins
            self.matrix = self._generate_board()
            self._place_players()
            if self.coins >= self.MIN_COINS:
                break
        return self.matrix
    def _generate_board(self):
        """Generate the board grid and return it."""
        board = []
        self.coins = 0
        for row in range(self.rows):
            row_cells = self._generate_row(row)
            board.append(row_cells)
            self._inject_random_items(row_cells)
        return board
    def _generate_row(self, row_index):
        """Generate a single row with walls or random items."""
        row = []
        for col in range(self.cols):
            if row_index % 2 == 0:
                row.append(self.WALL)
            else:
                cell = random.choice([self.COIN, self.EMPTY])
                row.append(cell)
                if cell == self.COIN:
                    self.coins += 1
        return row
    def _inject_random_items(self, row):
        """Randomly replace some walls with coins or empty cells."""
        step = random.randint(1, 2)
        for col in range(1, self.cols, step):
            item = random.choice([self.COIN, self.EMPTY])
            if item == self.COIN:
                self.coins += 1
            row[col] = item
            step += 1
    def _place_players(self):
        """Place players on the board."""
        self.matrix[0][0] = self.PLAYER1
        self.matrix[self.rows - 1][self.cols - 1] = self.PLAYER2

    def move_player(self, player: str, direction: str) -> None:
        """Move a player in the given direction."""
        curr_row, curr_col = self._find_player(player)
        moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }
        if direction not in moves:
            return
        d_row, d_col = moves[direction]
        return self._attempt_move(player, curr_row, curr_col, d_row, d_col)
    def _find_player(self, player):
        """Locate a player's position."""
        for r, row in enumerate(self.matrix):
            for c, val in enumerate(row):
                if val == player:
                    return r, c
        curr_row, curr_col = self._find_player(player)
        if curr_row is None:
            raise ValueError(f"Player {player} not on board")
    
    def _attempt_move(self, player, curr_row, curr_col, d_row, d_col):
        """General movement handler."""
        other_player = self._other_player(player)
        new_row, new_col = curr_row + d_row, curr_col + d_col
        if not self._is_in_bounds(new_row, new_col):
            return
        target = self.matrix[new_row][new_col]
        if target in [self.WALL, other_player]:
            return
        if target == self.COIN:
            self._add_score(player)
        self.matrix[curr_row][curr_col] = self.EMPTY
        self.matrix[new_row][new_col] = player
        return self._check_win(player)
    
    def _add_score(self, player):
        if player == self.PLAYER1:
            self.player1_score += self.POINTS_PER_COIN 
        else:
            self.player2_score += self.POINTS_PER_COIN
    def _check_win(self, player):
        score = self.player1_score if player == self.PLAYER1 else self.player2_score
        if score >= 100:
            self.winner = player
            return player
        return None

    def _other_player(self, player):
        return self.PLAYER2 if player == self.PLAYER1 else self.PLAYER1
    def _is_in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols