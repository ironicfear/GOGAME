import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
class GOGAME:
    def __init__(self):
        # speichern des bord standes
        self.captured_stones = 0
        self.score_white = 0
        self.score_black = 0
        self.board_size = 9
        self.board = []
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append(0)
            self.board.append(row)


        # Main Window
        self.main_wnd = tk.Tk()
        self.main_wnd.title("GO")
        self.main_wnd.state("zoomed")

        # Bilder
        self.black_stone_img = Image.open("Assets\\black_stone.png")
        self.white_stone_img = Image.open("Assets\white_stone.png")
        self.black_resize = self.black_stone_img.resize((150,150), Image.ANTIALIAS)
        self.white_resize = self.white_stone_img.resize((150,150), Image.ANTIALIAS)
        self.black_stone_img = ImageTk.PhotoImage(self.black_resize)
        self.white_stone_img = ImageTk.PhotoImage(self.white_resize)
        self.bgimage = Image.open("Assets\Tradbgimage.png")
        self.bgimage = self.bgimage.resize((int(self.main_wnd.winfo_screenwidth()), int(self.main_wnd.winfo_screenheight())), Image.ANTIALIAS)
        self.bgimage = ImageTk.PhotoImage(self.bgimage)


        # Größen
        self.screen_width = self.main_wnd.winfo_screenwidth()
        self.screen_height =self.main_wnd.winfo_screenheight()

        self.canvas_width = self.screen_width * 0.8
        self.canvas_height = self.screen_height * 0.8
        self.main_wnd.geometry(f"{int(self.canvas_width)}x{int(self.canvas_height)}")


        self.starting_screen()

    def starting_screen(self):
        self.maincanvas = tk.Canvas(self.main_wnd, width=self.canvas_width, height=self.canvas_height)
        self.maincanvas.pack(fill="both", expand=True)

        self.maincanvas.create_image(0,0, image=self.bgimage, anchor="nw")
        self.maincanvas.create_text(int(self.main_wnd.winfo_screenwidth())*0.5, int(self.main_wnd.winfo_screenheight())*0.2, text="GO Game", font=("Times New Roman", 50))

        self.single_player_button = ttk.Button(self.maincanvas, text="Single Player", command=self.start_game)
        self.singleplayerbuttonwindow = self.maincanvas.create_window(int(self.main_wnd.winfo_screenwidth())*0.5, int(self.main_wnd.winfo_screenheight())*0.35, anchor="nw", window=self.single_player_button)


    def start_game(self):
        self.maincanvas.destroy()
        #Canvas
        self.canvas = tk.Canvas(self.main_wnd, width=950, height=950)
        self.canvas.pack()

        self.canvas.create_rectangle(25,25,925,925, outline="black")

        for i in range(self.board_size + 1):
            self.canvas.create_line(100 * i + 25, 25, 100 * i + 25, 925)
            self.canvas.create_line(25, 100 * i + 25, 925, 100 * i + 25)


        def capture(row,col,opponent):
            captured_stones = 0
            for i in range(self.board_size):
                for j in range(self.board_size):
                    if (row+i >= 0 and row+i < self.board_size) and (col+j >= 0 and col+j < self.board_size):
                        if self.board [row+i][col+j] == opponent:
                            captured_stones += 1
                            self.board[row+i][col+j] = 0
                            self.canvas.delete(col * 100 + 25, row * 100 + 25)
                    
            return captured_stones





    #Place Stone
        self.Color = True

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
            # print(row,col)
            print(self.board[row][col])
            if row < 9 and col < 9 and row >=1 and col >= 1 and self.board [row][col] == 0:
                if self.Color :
                    self.board [row][col] = 1
                    used_img = self.black_stone_img
                    self.Color = False
                    
                    print(self.board[row][col])

                else:       
                    self.board [row][col] = 2
                    used_img = self.white_stone_img
                    self.Color = True
                    
                    print(self.board[row][col])
            
                self.canvas.create_image(col * 100 + 25, row * 100 + 25, image = used_img)
                
                

            else:
                print("Invalid Move")
        self.canvas.bind("<Button-1>", place_stone)

                        



    
    # print(board)


    # def load_game():
    #     pass

    # def save_game():
    #     pass

    # def new_game():
    #     pass

    # # Create Main menu
    # main_menu = tk.Menu(main_wnd)

    # # Create Filesystem
    # file_menu = tk.Menu(main_menu, tearoff=0)
    # file_menu.add_command(label="Load Game", command = load_game)
    # file_menu.add_command(label="Save Game", command = save_game)
    # file_menu.add_separator()
    # file_menu.add_command(label="New Game", command = new_game)
    # file_menu.add_separator()
    # file_menu.add_command(label="Exit", command= main_wnd.quit)

    # # Add Filesystem to Main menu
    # main_menu.add_cascade(label="File", menu=file_menu)

    # # Display Main Menu
    # main_wnd.config(menu=main_menu)





Game = GOGAME()
Game.main_wnd.mainloop()