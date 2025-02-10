import tkinter as tk
from random import randrange
# Global flag to track whose turn it is
turn_counter = 0  # Always start with computer

def display_board(board):
    # Create the main window with a fixed size
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    root.configure(bg="beige")
    root.resizable(False, False)  # Make the window unresizeable

    # Create a frame for the Tic-Tac-Toe grid with beige background
    frame = tk.Frame(root, bg="beige")
    frame.grid(row=0, column=0)

    # Create a grid of buttons for the board with beige background
    buttons = [[None for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(frame, text=str(board[row][col]), width=10, height=3,
                                          command=lambda r=row, c=col: on_button_click(r, c),
                                          font=("Arial", 16), bg="beige", fg="black")
            buttons[row][col].grid(row=row, column=col)

    # Create a label to display the winner message with a white background
    result_label = tk.Label(root, text="", font=("Arial", 16), bg="white", width=20, height=2)
    result_label.grid(row=1, column=0, padx=10, pady=10)

    # Replay button that resets the game
    def replay_game():
        global turn_counter
        # Reset the board and result
        nonlocal board, result_label
        board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
        result_label.config(text="", fg="black")
        update_buttons()
        enable_buttons()
        turn_counter = 0  # Always start with the computer

    replay_button = tk.Button(root, text="Replay", font=("Arial", 16), command=replay_game, bg="lightgray")
    replay_button.grid(row=2, column=0, padx=10, pady=10)

    def on_button_click(row, col):
        # Handle button click
        if board[row][col] not in ['O', 'X']:
            board[row][col] = 'O'  # human move
            buttons[row][col].config(text='O', fg="blue")
            if victory_for(board, 'O'):
                result_label.config(text="You won!", fg="green")
                disable_buttons()
                return
            if len(make_list_of_free_fields(board)) > 0:
                draw_move(board)  # computer move
                update_buttons()
                if victory_for(board, 'X'):
                    result_label.config(text="The computer won", fg="red")
                    disable_buttons()
                    return
            if len(make_list_of_free_fields(board)) == 0:  # Check if board is full and no winner
                result_label.config(text="It's a tie!", fg="black")
                disable_buttons()
                return

    def update_buttons():
        # Update button labels to reflect the current board state
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    buttons[row][col].config(text='X', fg="red")
                elif board[row][col] == 'O':
                    buttons[row][col].config(text='O', fg="blue")
                else:
                    buttons[row][col].config(text=str(board[row][col]), fg="black")

    def disable_buttons():
        # Disable all buttons after the game ends
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(state="disabled")

    def enable_buttons():
        # Enable all buttons for a new game
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(state="normal", text=str(board[row][col]))

    def make_list_of_free_fields(board):
        free = []
        for row in range(3):
            for col in range(3):
                if board[row][col] not in ['O', 'X']:
                    free.append((row, col))
        return free

    def victory_for(board, sgn):
        if sgn == "X":
            who = 'me'
        elif sgn == "O":
            who = 'you'
        else:
            who = None
        cross1 = cross2 = True
        for rc in range(3):
            if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
                return who
            if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
                return who
            if board[rc][rc] != sgn:
                cross1 = False
            if board[2 - rc][rc] != sgn:  # Fixed diagonal condition
                cross2 = False
        if cross1 or cross2:
            return who
        return None

    def draw_move(board):
        free = make_list_of_free_fields(board)
        cnt = len(free)
        if cnt > 0:
            this = randrange(cnt)
            row, col = free[this]
            board[row][col] = 'X'

    # Initialize the game
    global turn_counter
    board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
    board[1][1] = 'X'  # set first 'X' in the middle
    update_buttons()

    # Start the Tkinter event loop
    root.mainloop()


# Display the game interface
display_board([[3 * j + i + 1 for i in range(3)] for j in range(3)])

