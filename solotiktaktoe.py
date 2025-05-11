import tkinter as tk
from tkinter import messagebox

# global variables 
board = {0:"",1:"",2:""
         ,3:"",4:"",5:""
         ,6:"",7:"",8:""}

player = 'X'
xscore = 0
oscore = 0

def print_board(board):
    print("\nCurrent Board:")
    for i in range(0, 9, 3):
        row = [board[i], board[i+1], board[i+2]]
        print(" | ".join(cell if cell != "" else " " for cell in row))
        if i < 6:
            print("--+---+--")

def is_draw(b):
    a = list(b.values())
    if "" not in a:
        return True
    return False

def is_win(boardcopy, p):
    b = list(boardcopy.values())
    
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for x, y, z in wins:
        if b[x] == b[y] == b[z] == p:
            return True
    return False

def check_win_and_update_score():
    global xscore, oscore, player
    if is_win(board, player):
        if player == "X":
            xscore += 1
            x_score_variable.set(f'X: {xscore}')
        else:
            oscore += 1
            y_score_variable.set(f'O: {oscore}')
        return True
    return False

def minimax(boardcopy, isMaximizing):

    if is_win(boardcopy, "O"):
        return 1
    if is_win(boardcopy, "X"):
        return -1
    if is_draw(boardcopy):
        return 0

    if isMaximizing:
        best_score = -100

        for key in boardcopy:
            if boardcopy[key] == "":
                boardcopy[key] = "O"
                score = minimax(boardcopy, False)
                boardcopy[key] = ""
                if score > best_score:
                    best_score = score
        return best_score
    
    else:
        best_score = 100
        for key in boardcopy:
            if boardcopy[key] == "":
                boardcopy[key] = "X"
                score = minimax(boardcopy, True)
                boardcopy[key] = ""
                if score < best_score:
                    best_score = score
        return best_score        

def computer_move():
    global player, board

    boardcopy = board.copy()
    best_score = -100
    best_move = None

    for key in boardcopy:
        if boardcopy[key] == "":
            boardcopy[key] = "O"
            score = minimax(boardcopy, False)
            boardcopy[key] = ""
            if score > best_score:
                best_score = score
                best_move = key

    if best_move is not None:
        board[best_move] = "O"
        variables[best_move].set("O")
        player = "O"


        if check_win_and_update_score():
            messagebox.showinfo("Game Over", "Computer wins!")
            for widget in frame_bottom.winfo_children():
                widget.config(state='disabled')
        elif is_draw(board):
            messagebox.showinfo("Game Over", "It's a Draw!")
            for widget in frame_bottom.winfo_children():
                widget.config(state='disabled')
        else:
            player = "X"

def move(index):
    global board, player

    if board[index] == "":
        board[index] = player
        variables[index].set(player)

        if check_win_and_update_score():
            for widget in frame_bottom.winfo_children():
                widget.config(state='disabled')
            messagebox.showinfo("Game Over", f"{player} is the winner")
        elif is_draw(board):
            messagebox.showinfo("Game Over", "It's a Draw!")
            for widget in frame_bottom.winfo_children():
                widget.config(state='disabled')
        else:
            player = "O"
            computer_move()

def reset_game():
    global board, player

    board = {0:"",1:"",2:""
            ,3:"",4:"",5:""
            ,6:"",7:"",8:""}
    
    player = 'X'

    for widget in frame_bottom.winfo_children():
        widget.config(state='normal')
    for index in range(9):
        variables[index].set("")

def reset_score():
    global board, player, xscore, oscore

    board = {0:"",1:"",2:""
            ,3:"",4:"",5:""
            ,6:"",7:"",8:""}
    
    player = 'X'
    xscore = 0
    oscore = 0
    x_score_variable.set('X: 0')
    y_score_variable.set('O: 0')
    for widget in frame_bottom.winfo_children():
        widget.config(state='normal')
    for index in range(9):
        variables[index].set("")

# GUI
window =  tk.Tk()
window.geometry('350x350')
window.title('Tik Tak Toe')

# score frame
frame = tk.Frame(master=window)
x_score_variable = tk.StringVar(value=f'X: {xscore}')
x_score = tk.Label(master=frame, font='Calibri 20 bold', textvariable=x_score_variable)
y_score_variable = tk.StringVar(value=f'O: {oscore}')
y_score = tk.Label(master=frame, font='Calibri 20 bold', textvariable=y_score_variable)
frame.pack(pady=10)
x_score.pack(side='left', padx=10)
y_score.pack(side='right', padx=10)

# grid frame
frame_bottom = tk.Frame(window)
frame_bottom.pack()

#button text variable
btn0_variable = tk.StringVar()
btn1_variable = tk.StringVar()
btn2_variable = tk.StringVar()
btn3_variable = tk.StringVar()
btn4_variable = tk.StringVar()
btn5_variable = tk.StringVar()
btn6_variable = tk.StringVar()
btn7_variable = tk.StringVar()
btn8_variable = tk.StringVar()

variables = [
    btn0_variable, btn1_variable, btn2_variable,
    btn3_variable, btn4_variable, btn5_variable,
    btn6_variable, btn7_variable, btn8_variable
]

btn0 = tk.Button(frame_bottom, text="", 
                  font=("Arial", 24), 
                  width=5, 
                  height=2, 
                  command=lambda:move(0),
                  textvariable=btn0_variable)

btn1 = tk.Button(frame_bottom, text="", 
                  font=("Arial", 24), 
                  width=5, 
                  height=2, 
                  command=lambda:move(1),
                  textvariable=btn1_variable)

btn2 = tk.Button(frame_bottom, text="", 
                  font=("Arial", 24), 
                  width=5, 
                  height=2, 
                  command=lambda:move(2),
                  textvariable=btn2_variable)

btn3 = tk.Button(frame_bottom, text="", 
                  font=("Arial", 24), 
                  width=5, 
                  height=2, 
                  command=lambda:move(3),
                  textvariable=btn3_variable)

btn4 = tk.Button(frame_bottom, text="", 
                  font=("Arial", 24), 
                  width=5, 
                  height=2, 
                  command=lambda:move(4),
                  textvariable=btn4_variable)

btn5 = tk.Button(frame_bottom, text="", 
                  font=("Arial", 24), 
                  width=5, 
                  height=2, 
                  command=lambda:move(5),
                  textvariable=btn5_variable)

btn6 = tk.Button(frame_bottom, text="", 
                  font=("Arial", 24), 
                  width=5, 
                  height=2, 
                  command=lambda:move(6),
                  textvariable=btn6_variable)

btn7 = tk.Button(frame_bottom, text="", 
                  font=("Arial", 24), 
                  width=5, 
                  height=2, 
                  command=lambda:move(7),
                  textvariable=btn7_variable)

btn8 = tk.Button(frame_bottom, text="", 
                  font=("Arial", 24), 
                  width=5, 
                  height=2, 
                  command=lambda:move(8),
                  textvariable=btn8_variable)

buttons = [btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8]

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)
btn5.grid(row=1, column=2)
btn6.grid(row=2, column=0)
btn7.grid(row=2, column=1)
btn8.grid(row=2, column=2)

# reset buttons
tk.Button(window, text='Reset game', font=("Arial",10),
          width=10, height=2, command=reset_game).pack(padx=5, pady=20, side='left')
tk.Button(window, text='Reset score', font=("Arial",10),
          width=10, height=2, command=reset_score).pack(padx=5, pady=20, side='right')

window.mainloop()

