import tkinter as tk

board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'

def button_click(row, col):
    global current_player

    if board[row][col] == '' and not check_winner():
        if current_player == 'X':
            buttons[row][col].config(text='X', fg='red', bg='aqua')
        else:
            buttons[row][col].config(text='O', fg='blue', bg='yellow')

    if board[row][col] == '' and not check_winner():
        buttons[row][col].config(text=current_player)
        board[row][col] = current_player

        if check_winner():
            result = f"Player {current_player} wins!"
            result_label.config(text=result)
        elif all(board[i][j] != '' for i in range(3) for j in range(3)):
            result_label.config(text="It's a tie!")
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

def reset_game():
    global current_player
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', bg="#f3f0f2", state=tk.NORMAL)
            board[i][j] = ''
    current_player = 'X'
    result_label.config(text="")

ticTacToe = tk.Tk()
ticTacToe.title("'Tic-Tac-Toe' created by Purva Athnere")

# size 
window_width = 300
window_height = 300
screen_width = ticTacToe.winfo_screenwidth()
screen_height = ticTacToe.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
ticTacToe.geometry(f"{window_width}x{window_height}+{x}+{y}")

# buttons
buttons = [[None, None, None] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(ticTacToe, text='', width=10, height=3, command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

result_label = tk.Label(ticTacToe, text="", font=("Helvetica", 16))
result_label.grid(row=3, column=0, columnspan=3)

# reset button
reset_button = tk.Button(ticTacToe, text="Reset", command=reset_game)
reset_button.grid(row=5, column=1)

ticTacToe.mainloop()
