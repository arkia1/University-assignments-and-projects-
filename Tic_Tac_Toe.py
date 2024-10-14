import tkinter as tk
from tkinter import messagebox

# Class that handles the game logic
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # A list to represent the 3x3 board
        self.current_winner = None  # Keep track of the winner!
        self.current_turn = "X"     # Player X always goes first

    def make_move(self, square, player):
        # If the move is valid (the square is empty)
        if self.board[square] == " ":
            self.board[square] = player
            if self.check_winner(player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, player):
        # Check for winning combinations: 3 rows, 3 columns, 2 diagonals
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_board_full(self):
        return " " not in self.board  # True if no more moves are possible


# Class that handles the GUI using Tkinter
class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToe()
        self.root = root
        self.root.title("Tic Tac Toe")
        self.buttons = []  # A list to store buttons
        self.create_buttons()
        self.create_reset_button()

    def create_buttons(self):
        # Create a 3x3 grid of buttons
        for i in range(9):
            button = tk.Button(self.root, text=" ", font="Arial 20", width=5, height=2,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def create_reset_button(self):
        # Add a reset button at the bottom of the grid
        reset_button = tk.Button(self.root, text="Restart Game", font="Arial 15", command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3)

    def button_click(self, index):
        # When a button is clicked, make a move
        if self.game.make_move(index, self.game.current_turn):
            self.update_button(index)
            if self.game.current_winner:
                self.end_game(f"Player {self.game.current_turn} wins!")
            elif self.game.is_board_full():
                self.end_game("It's a draw!")
            else:
                self.switch_turn()

    def update_button(self, index):
        # Update the button text to show the player's move
        self.buttons[index].config(text=self.game.current_turn)

    def switch_turn(self):
        # Switch turns between player X and O
        self.game.current_turn = "O" if self.game.current_turn == "X" else "X"

    def end_game(self, message):
        # Display the winner and disable all buttons
        messagebox.showinfo("Game Over", message)
        for button in self.buttons:
            button.config(state="disabled")

    def reset_game(self):
        # Reset the game board for a new game
        self.game = TicTacToe()
        for button in self.buttons:
            button.config(text=" ", state="normal")


# Main application runner
if __name__ == "__main__":
    root = tk.Tk()
    game_app = TicTacToeGUI(root)
    root.mainloop()
