import tkinter as tk
from tkinter import messagebox

# Function to check the winner
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    
    # Check for tie
    for row in board:
        if "" in row:
            return None
    return "Tie"

# Function to handle button click
def on_button_click(row, col):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        winner = check_winner()

        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a Tie!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)

# Set up the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize the game state
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

# Create buttons for the game board
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('normal', 40), width=5, height=2, 
                                  command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Create a reset button
reset_button = tk.Button(root, text="Reset Game", font=('normal', 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Run the main event loop
root.mainloop()
