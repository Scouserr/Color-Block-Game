import tkinter as tk
from game.game import ColorBlockGame
from PIL import Image, ImageTk


if __name__ == "__main__":
    root = tk.Tk()

    # 设置窗口图标
    icon_path = r".\\icon_transparentbg.png"
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon_photo)


    game = ColorBlockGame(root)
    root.mainloop()
