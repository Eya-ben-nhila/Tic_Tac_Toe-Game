# Tic_Tac_Toe-Game

This is a simple Tic-Tac-Toe game implemented using Python and Tkinter. The game provides an interactive graphical interface where a player can compete against the computer.

1-Features:

Single-player mode: Play against an AI opponent.

Graphical Interface: Uses Tkinter for a user-friendly game board.

Automatic Moves: The computer (AI) plays as 'X' and always starts first.

Game Logic: Checks for wins, ties, and available moves.

Replay Option: Restart the game without closing the application.

2-How to Play:

Run the Python script.

The game board will appear with an initial 'X' placed in the center.

Click on any available cell to place your 'O'.

The AI will make its move automatically.

The game continues until there is a winner or a tie.

Click the "Replay" button to restart the game.

3-Game Rules:

The board consists of a 3x3 grid.

The player uses 'O', and the computer uses 'X'.

The game alternates turns between the player and the AI.

A player wins by placing three marks in a row, column, or diagonal.

If all spaces are filled and no player has won, the game ends in a tie.

4-Code Overview

display_board(board): Initializes the game window and board.

on_button_click(row, col): Handles player moves.

draw_move(board): Allows the AI to make a move.

victory_for(board, sgn): Checks for a winner.

make_list_of_free_fields(board): Identifies open spots on the board.

update_buttons(): Refreshes the board UI.

disable_buttons(): Disables input after game ends.

enable_buttons(): Resets the board for a new game.

5-Requirements

Python 3.x

Tkinter (comes pre-installed with Python)

6-Running the Game

Save the script as tic_tac_toe.py and run it using:

python tic_tac_toe.py

Enjoy playing Tic-Tac-Toe!

