# Gold_Rush
import random
from typing import List, Optional, Tuple


POINTS_PER_COIN = 10
WINNING_SCORE = 100
MIN_COINS_REQUIRED = 10

COIN = "$"
EMPTY = "."
WALL = "wall"

class GoldRush:
    """
    Clean refactor of the GoldRush game board.
    Expects a Matrix-like parent or compatible interface, but implemented
    here standalone for clarity (only uses rows, cols, matrix attributes).
    """

    def __init__(self, rows: int, cols: int):
        """
        Initialize board dimensions and game state.
        """
        self.rows = rows
        self.cols = cols
        self.matrix: List[List[str]] = []
        self.player1_score = 0
        self.player2_score = 0
        self.winner: Optional[str] = None
        self.total_coins = 0

    def load_board(self) -> List[List[str]]:
        """
        Initializes the game board with walls, empty spaces and coins.
        Ensures at least MIN_COINS_REQUIRED are present.
        Returns the initialized matrix.
        """
        # Handle trivial empty board
        if self.rows == 0 or self.cols == 0:
            self.matrix = []
            self.total_coins = 0
            return self.matrix

        # Try generating until enough coins exist
        while True:
            self.matrix = []
            coins_count = 0
            elements = [COIN, EMPTY, WALL]

            for i in range(self.rows):
                row: List[str] = []
                for j in range(self.cols):
                    if i % 2 == 1:
                        # odd rows: place coin or empty
                        rand_element = random.choice(elements[:2])  # COIN or EMPTY
                        row.append(rand_element)
                        if rand_element == COIN:
                            coins_count += 1
                    else:
                        # even rows: mostly walls
                        row.append(WALL)
                # small randomness: replace some positions in the row
                # choose a step >=1 to avoid IndexError
                step = random.randint(1, max(1, self.cols // 2))
                for k in range(1, self.cols, step):
                    rand_element = random.choice(elements[:2])
                    row[k] = rand_element
                    if rand_element == COIN:
                        coins_count += 1

                self.matrix.append(row)

            # place players (ensure board big enough)
            self.matrix[0][0] = "player1"
            self.matrix[self.rows - 1][self.cols - 1] = "player2"

            self.total_coins = coins_count
            if self.total_coins >= MIN_COINS_REQUIRED:
                break
            # otherwise regenerate

        return self.matrix

    # ----------------------
    # Helper: other player
    # ----------------------
    def other_player(self, player: str) -> str:
        """Return the other player's id string."""
        return "player2" if player == "player1" else "player1"

    # ----------------------
    # Scoring & win check
    # ----------------------
    def add_score(self, player: str) -> int:
        """
        Increase player's score by POINTS_PER_COIN and return new score.
        """
        if player == "player1":
            self.player1_score += POINTS_PER_COIN
            return self.player1_score
        else:
            self.player2_score += POINTS_PER_COIN
            return self.player2_score

    def get_score(self, player: str) -> int:
        """Return current score for player."""
        return self.player1_score if player == "player1" else self.player2_score

    def check_win(self, player: str) -> Optional[str]:
        """
        If the player's score reached WINNING_SCORE or more, set and return winner.
        Otherwise return None.
        """
        if self.get_score(player) >= WINNING_SCORE:
            self.winner = player
            return self.winner
        return None

    # ----------------------
    # Movement logic
    # ----------------------
    def _move(self, curr_row: int, curr_col: int, player: str,
              delta_row: int, delta_col: int) -> Optional[str]:
        """General move method; returns winner if move caused a win, else None."""
        other = self.other_player(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        # boundary check
        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return None

        destination = self.matrix[new_row][new_col]
        # Can't move into wall or the other player
        if destination in (WALL, other):
            return None

        # If coin, collect and update total_coins
        if destination == COIN:
            self.add_score(player)
            # decrement total coin count so we track remaining coins if needed
            self.total_coins = max(0, self.total_coins - 1)

        # Move player
        self.matrix[curr_row][curr_col] = EMPTY
        self.matrix[new_row][new_col] = player

        # Check for win
        return self.check_win(player)

    def move_down(self, curr_row: int, curr_col: int, player: str) -> Optional[str]:
        return self._move(curr_row, curr_col, player, 1, 0)

    def move_up(self, curr_row: int, curr_col: int, player: str) -> Optional[str]:
        return self._move(curr_row, curr_col, player, -1, 0)

    def move_right(self, curr_row: int, curr_col: int, player: str) -> Optional[str]:
        return self._move(curr_row, curr_col, player, 0, 1)

    def move_left(self, curr_row: int, curr_col: int, player: str) -> Optional[str]:
        return self._move(curr_row, curr_col, player, 0, -1)

    # ----------------------
    # Public API
    # ----------------------
    def find_player(self, player: str) -> Optional[Tuple[int, int]]:
        """Return (row, col) for player, or None if not found."""
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if val == player:
                    return (i, j)
        return None

    def move_player(self, player: str, direction: str) -> Optional[str]:
        """
        Find the player on the board, move them in the given direction
        ('up', 'down', 'left', 'right') and return winner if any.
        """
        pos = self.find_player(player)
        if pos is None:
            return None
        r, c = pos

        if direction == "down":
            return self.move_down(r, c, player)
        if direction == "up":
            return self.move_up(r, c, player)
        if direction == "right":
            return self.move_right(r, c, player)
        if direction == "left":
            return self.move_left(r, c, player)
        return None

    # ----------------------
    # Utility / debug helpers
    # ----------------------
    def pretty_print(self) -> None:
        """Prints the board in a readable format."""
        for row in self.matrix:
            print(" ".join(row))
        print(f"P1 score: {self.player1_score}  P2 score: {self.player2_score}  Winner: {self.winner}")

