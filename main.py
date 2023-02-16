import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import time
class GOGAME:
    def __init__(self):
        # speichern des bord standes
        self.captured_stones = 0
        self.score_white = 0
        self.score_black = 0


        # Main Window
        self.main_wnd = tk.Tk()
        self.main_wnd.title("GO")
        self.main_wnd.state("zoomed")
        self.main_wnd.attributes("-fullscreen", True)
        self.main_wnd.bind("<Escape>", lambda event: self.main_wnd.attributes("-fullscreen", False))

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
        # self.adjust_wdh = int(self.screen_width / 15)
        self.adjust_hgt = int(self.screen_height / 15)
        self.adjust_wdt = int(self.screen_height / 15)

        self.canvas_width = self.screen_width * 0.8
        self.canvas_height = self.screen_height * 0.8
        self.main_wnd.geometry(f"{int(self.canvas_width)}x{int(self.canvas_height)}")


        self.starting_screen()


    # Starting screen
    def starting_screen(self):
        self.maincanvas = tk.Canvas(self.main_wnd, width=self.canvas_width, height=self.canvas_height)
        self.maincanvas.pack(fill="both", expand=True)

        self.maincanvas.create_image(0,0, image=self.bgimage, anchor="nw")
        self.maincanvas.create_text(int(self.main_wnd.winfo_screenwidth())*0.5, int(self.main_wnd.winfo_screenheight())*0.2, text="GO Game", font=("Times New Roman", 50))

        self.stylebtn = ttk.Style()
        self.stylebtn.configure("my.TButton", font=("ColfaxAI", 15 ), padding=20)

        self.single_player_button = ttk.Button(self.maincanvas, text="Single Player", command=self.start_game, style="my.TButton")
        self.singleplayerbuttonwindow = self.maincanvas.create_window(int(self.main_wnd.winfo_screenwidth())*0.465, int(self.main_wnd.winfo_screenheight())*0.3, anchor="nw", window=self.single_player_button)

        self.sizeslider = tk.Scale(self.maincanvas, from_=8, to=12, orient=tk.HORIZONTAL, length=150, sliderlength=20, showvalue=1)
        self.sizeslider.set(8)
        self.maincanvas.create_text(int(self.main_wnd.winfo_screenwidth())*0.5, int(self.main_wnd.winfo_screenheight())*0.39, text="Board Size", font=("ColfaxAI", 14))
        self.sliderwindow = self.maincanvas.create_window(int(self.main_wnd.winfo_screenwidth())*0.467, int(self.main_wnd.winfo_screenheight())*0.4, anchor="nw", window=self.sizeslider)


    # Game Board
    def start_game(self):
        print(self.sizeslider.get())
        self.board_size = self.sizeslider.get() + 1
        self.board = []
        for ii in range(self.board_size-1):
            row = []
            for j in range(self.board_size-1):
                row.append(0)
            self.board.append(row)
        
        self.maincanvas.destroy()
        #Canvas
        self.canvas = tk.Canvas(self.main_wnd, width= self.adjust_hgt* self.board_size + 50, height=self.adjust_hgt*self.board_size + 50 +200)
        self.canvas.pack()

        

        self.canvas.create_rectangle(25,25,self.adjust_hgt* self.board_size + 25,self.adjust_hgt* self.board_size + 25, outline="black")

        for i in range(self.board_size):
            self.canvas.create_line(self.adjust_hgt * i + 25, 25, self.adjust_hgt * i + 25,self.adjust_hgt * self.board_size + 25)
            self.canvas.create_line(25, self.adjust_hgt * i + 25,self.adjust_hgt * self.board_size + 25, self.adjust_hgt * i + 25)

        self.stylerst = ttk.Style()
        self.stylerst.configure("my.TButton", font=("ColfaxAI", 15),padding=10)
        #self.resetbutton = ttk.Button(self.canvas, text="Reset",command=restartgame, style="my.TButton")
        #self.resetbuttonwnd = self.canvas.create_window(self.adjust_wdt * self.board_size * 0.5,self.adjust_hgt * self.board_size + 100, anchor="center", window=self.resetbutton)

        #Frame
        # frame = tk.Frame(self.main_wnd, width=int(self.winfo_screenwidth()), height=int(self.winfo_screenheight()), bg='white')
        # frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Rules
        

        
        


        def detect_surrounded_fields():
            result_list = []

            for i in range(self.board_size-1):
                for j in range(self.board_size-1):
                    if self.board[i][j] != 0:
                        group = [(i,j)]
                        to_check = [(i,j)]
                        visited = set(to_check)
                        surrounded = True

                        while to_check:
                            curr = to_check.pop()
                            neighbors = [(curr[0]-1, curr[1]), (curr[0]+1, curr[1]), (curr[0], curr[1]-1), (curr[0], curr[1]+1)]

                            for neighbor in neighbors:
                                if neighbor[0] < 0 or neighbor[0] >= self.board_size or neighbor[1] < 0 or neighbor[1] >= self.board_size:
                                    surrounded = False
                                    continue

                                if neighbor not in visited and self.board[neighbor[0]][neighbor[1]] == self.board[i][j]:
                                    group.append(neighbor)
                                    to_check.append(neighbor)
                                    visited.add(neighbor)

                        if surrounded:
                            surrounded_group = True
                            for cell in group:
                                neighbors = [(cell[0]-1, cell[1]), (cell[0]+1, cell[1]), (cell[0], cell[1]-1), (cell[0], cell[1]+1)]

                                for neighbor in neighbors:
                                    if neighbor[0] < 0 or neighbor[0] >= self.board_size or neighbor[1] < 0 or neighbor[1] >= self.board_size:
                                        continue

                                    if self.board[neighbor[0]][neighbor[1]] == 0:
                                        surrounded_group = False
                                        break

                                if not surrounded_group:
                                    break

                            if surrounded_group:
                                result_list.append(group)

            return result_list




        
        





    #Place Stone
        self.Color = True

        def place_stone(event):
            global Color, score_white, score_black
            x,y = event.x, event.y
            print(y,x)
            row, col = int(y  / self.adjust_hgt -1), int(x / self.adjust_hgt-1 )
            print(row,col)
            print(self.board[row][col])
            if row < self.board_size and col < self.board_size and row >=0 and col >= 0 and self.board [row][col] == 0:
                if self.Color :
                    self.board [row][col] = 1
                    used_img = self.black_stone_img
                    self.Color = False
                    opponent = 2
                    print(self.board[row][col])

                else:       
                    self.board [row][col] = 2
                    used_img = self.white_stone_img
                    self.Color = True
                    opponent = 1
                    print(self.board[row][col])

                self.canvas.create_image((col + 1) * self.adjust_hgt + 25, (row + 1) * self.adjust_hgt + 25, image = used_img)
                
                if len(detect_surrounded_fields()) != 0:
                    stonestodelete = detect_surrounded_fields()               
                    stonestodelete = stonestodelete[0]
                    for deleted in stonestodelete:
                        row1,col1 = deleted
                        self.winner = self.board[row1][col1]
                        self.board[row1][col1] = 0
                        time.sleep(0.1)
                        deletenow = self.canvas.find_closest((col1 + 1) * self.adjust_hgt + 25, (row1 + 1) * self.adjust_hgt + 25)
                        self.canvas.delete(deletenow)
                        winning()
                
                    print(self.board)   
                    print(stonestodelete)

            else:
                print("Invalid Move")
            
        def winning():
            self.canvas.create_rectangle(self.adjust_wdt * self.board_size *0.3,self.adjust_wdt * self.board_size *0.3, self.adjust_wdt * self.board_size *0.8,self.adjust_wdt * self.board_size *0.7, fill="White")
            if self.winner == 2:
                self.canvas.create_text(self.adjust_wdt * self.board_size * 0.55,self.adjust_wdt * self.board_size * 0.5, text="Black Won", font=("Times New Roman", 50))
            else:
                self.canvas.create_text(self.adjust_wdt * self.board_size * 0.55,self.adjust_wdt * self.board_size * 0.5, text="White Won", font=("Times New Roman", 50))
        self.canvas.bind("<Button-1>", place_stone)


    
        

                        



Game = GOGAME()
Game.main_wnd.mainloop()