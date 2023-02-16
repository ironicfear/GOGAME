import tkinter as tk
from PIL import Image, ImageTk


# speichern des bord standes
captured_stones = 0
score_white = 0
score_black = 0
board_size = 9
board = []
for i in range(board_size -1):
    row = []
    for j in range(board_size-1):
        row.append(0)
    board.append(row)


# Main Window
main_wnd = tk.Tk()
main_wnd.title("GO")
main_wnd.state("zoomed")
black_stone_img = Image.open("Assets\\black_stone.png")
white_stone_img = Image.open("Assets\white_stone.png")
black_resize = black_stone_img.resize((150,150), Image.ANTIALIAS)
white_resize = white_stone_img.resize((150,150), Image.ANTIALIAS)
black_stone_img = ImageTk.PhotoImage(black_resize)
white_stone_img = ImageTk.PhotoImage(white_resize)

# Größen
screen_width = main_wnd.winfo_screenwidth()
screen_height = main_wnd.winfo_screenheight()

canvas_width = screen_width * 0.8
canvas_height = screen_height * 0.8
main_wnd.geometry(f"{int(canvas_width)}x{int(canvas_height)}")

#Canvas
canvas = tk.Canvas(main_wnd, width=950, height=950)
canvas.pack()

canvas.create_rectangle(25,25,925,925, outline="black")

for i in range(10):
    canvas.create_line(100 * i + 25, 25, 100 * i + 25, 925)
    canvas.create_line(25, 100 * i + 25, 925, 100 * i + 25)


def capture(row,col,opponent):
    captured_stones = 0
    for i in range(board_size):
        for j in range(board_size):
            if (row+i >= 0 and row+i < board_size) and (col+j >= 0 and col+j < board_size):
                if board [row+i][col+j] == opponent:
                    captured_stones += 1
                    board[row+i][col+j] = 0
                    canvas.delete(col * 100 + 25, row * 100 + 25)
            
    return captured_stones

def GameOver():
    # for i in range(board_size):
    #     for j in range(board_size):
    #         if board[i][j] == 0:
    #             return False
    if score_black >= 2 or score_white >= 2:
        return True
    return False



def check_captures(row, col):
    captures = []
    # Check north
    if row > 0 and board[row-1][col] != board[row][col] and is_surrounded(row-1, col, board[row-1][col]):
        captures.append((row-1, col))
    # Check south
    if row < board_size-1 and board[row+1][col] != board[row][col] and is_surrounded(row+1, col, board[row+1][col]):
        captures.append((row+1, col))
    # Check west
    if col > 0 and board[row][col-1] != board[row][col] and is_surrounded(row, col-1, board[row][col-1]):
        captures.append((row, col-1))
    # Check east
    if col < board_size-1 and board[row][col+1] != board[row][col] and is_surrounded(row, col+1, board[row][col+1]):
        captures.append((row, col+1))
    return captures

def is_surrounded(row, col, stone_color):
    # Check north
    if row == 0 or board[row-1][col] == 0 or board[row-1][col] == stone_color:
        return False
    # Check south
    if row == board_size-1 or board[row+1][col] == 0 or board[row+1][col] == stone_color:
        return False
    # Check west
    if col == 0 or board[row][col-1] == 0 or board[row][col-1] == stone_color:
        return False
    # Check east
    if col == board_size-1 or board[row][col+1] == 0 or board[row][col+1] == stone_color:
        return False
    return True

#Place Stone
Color = True

def place_stone(event):
    global Color, score_white, score_black
    x,y = event.x, event.y
    print(y,x)
    row, col = int(y  / 100), int(x / 100)
    print(row,col)
    # if x - row >= 75 :
    #     row = row +1
    # if y - col >= 75 :
    #     col = col +1
    print(row,col)
    print(board[row][col])
    if row < 9 and col < 9 and row >=1 and col >= 1 and board [row][col] == 0:
        if Color :
            board [row][col] = 1
            used_img = black_stone_img
            Color = False
            #capture(row, col, 2)

            captures  = check_captures(row, col)
            print(board[row][col])

        else:       
            board [row][col] = 2
            used_img = white_stone_img
            Color = True
            #capture(row, col, 1)
            captures = check_captures(row, col)
            print(board[row][col])
    
        canvas.create_image(col * 100 + 25, row * 100 + 25, image = used_img)
        # rowdel, coldel = captures[0], captures[1]
        # print(rowdel,coldel)
        print(board)
        print(captures)
        print(captures[0][0], captures[0][1])
        print(len(captures))

        captures1 = captures
        board[captures1[0][0]][captures1[0][1]] = 0
        print(board[captures1[0][0]][captures1[0][1]])
        canvas.delete(int(captures1[0][1]) * 100 +25, int(captures1[0][1] * 100 + 25))


        # if GameOver():
        #     print("Game Over!")

    else:
        print("Invalid Move")


                    



canvas.bind("<Button-1>", place_stone)
print(board)


def load_game():
    pass

def save_game():
    pass

def new_game():
    pass

# Create Main menu
main_menu = tk.Menu(main_wnd)

# Create Filesystem
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="Load Game", command = load_game)
file_menu.add_command(label="Save Game", command = save_game)
file_menu.add_separator()
file_menu.add_command(label="New Game", command = new_game)
file_menu.add_separator()
file_menu.add_command(label="Exit", command= main_wnd.quit)

# Add Filesystem to Main menu
main_menu.add_cascade(label="File", menu=file_menu)

# Display Main Menu
main_wnd.config(menu=main_menu)





main_wnd.mainloop()