import tkinter as tk
from tkinter import messagebox, font
from image.image_utils import generate_images, display_images
from timeWindow.timeWindow import timeLimit

class ColorBlockGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Color Block Game")

        self.center_window(400, 400)  # 设置窗口居中

        self.rows = 0
        self.columns = 0

        self.correct_count = 0
        self.image_window = None
        self.time_window = None

        self.create_widgets()

    def create_widgets(self):
        self.row_label = tk.Label(self.master, text="Rows:")
        self.row_label.pack()
        self.row_entry = tk.Entry(self.master)
        self.row_entry.pack()
        self.row_entry.insert(0, "50")

        self.column_label = tk.Label(self.master, text="Columns:")
        self.column_label.pack()
        self.column_entry = tk.Entry(self.master)
        self.column_entry.pack()
        self.column_entry.insert(0, "20")         
        
        self.block_size_label = tk.Label(self.master, text="Block Size:")
        self.block_size_label.pack()
        self.block_size_entry = tk.Entry(self.master)
        self.block_size_entry.pack()
        self.block_size_entry.insert(0, "10")        

        self.time_label = tk.Label(self.master, text="Time:")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.master)
        self.time_entry.pack()
        self.time_entry.insert(0, "86400")

        self.start_button = tk.Button(self.master, text="Start Game", command=self.restart_game)
        self.start_button.pack()
        self.master.bind("<Return>", lambda event: self.restart_game())
        self.master.bind("<Escape>", lambda event: self.master.destroy())
        
    def center_window(self, width, height):
        # 获取屏幕宽度和高度
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # 计算窗口的 x 和 y 坐标
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # 设置窗口的大小和位置
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def restart_game(self):
        self.correct_count = 0

        # 传递关闭 image_window 的回调函数
        self.time_window = timeLimit(self, self.master, int(self.time_entry.get()), self.close_image_window)

        self.start_game()

    def close_image_window(self):
        if self.image_window is not None:

            self.image_window.destroy()

    def start_game(self):
        if self.image_window is not None:
            self.image_window.destroy()

        try:
            self.rows = int(self.row_entry.get())
            self.columns = int(self.column_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for rows and columns.")
            return
        
        # timeLimit(self.master, int(self.time_entry.get()), self.image_window)

        self.img1, self.img2, self.target_row, self.target_col = generate_images(self.rows, self.columns, int(self.block_size_entry.get()))

        self.image_window = display_images(self.master, self.img1, self.img2)

        # Create widgets in the image window
        self.correct_label = tk.Label(self.image_window, text=f"Correct: {self.correct_count}")
        self.correct_label.pack()

        self.row_input_label = tk.Label(self.image_window, text="Guess Row:")
        self.row_input_label.pack()
        self.row_input = tk.Entry(self.image_window)
        self.row_input.pack()

        self.column_input_label = tk.Label(self.image_window, text="Guess Column:")
        self.column_input_label.pack()
        self.column_input = tk.Entry(self.image_window)
        self.column_input.pack()
        
        self.occupier_frame = tk.Frame(self.image_window, height=100)
        self.occupier_frame.pack()

        def image_window_esc(self):
            self.image_window.destroy()
            self.time_window.destroy()

        self.image_window.focus_set()
        self.image_window.bind("<space>", lambda event: self.start_game())
        self.image_window.bind("<Escape>", lambda event: image_window_esc(self))
        self.image_window.bind("<Button-1>", lambda event: self.on_image_click(event))

    def on_image_click(self, event):
        # Assuming each cell has a fixed size for simplicity
        cell_width = self.img1.width() // self.columns
        cell_height = self.img1.height() // self.rows

        # Calculate which cell was clicked
        clicked_row_1 = (event.y - 2) // cell_height
        clicked_col_1 = (event.x - 2) // cell_width

        if clicked_col_1 <= int(self.column_entry.get()) and clicked_row_1 <= int(self.row_entry.get()):
            #  and clicked_col_1 > 0 and clicked_row_1 > 0
            self.row_input.delete(0, tk.END)
            self.column_input.delete(0, tk.END)
            self.row_input.insert(0, clicked_row_1)    
            self.column_input.insert(0, clicked_col_1) 
        else:
            return      

        img_click_right = clicked_row_1 == self.target_row and clicked_col_1 == self.target_col

        # Check if clicked position matches target
        if img_click_right:
            self.correct_count += 1
        else:
            return 

        # Optionally restart the game
        self.start_game()

