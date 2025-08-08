import numpy as np
from PIL import Image, ImageTk
import random
import tkinter as tk
from tkinter import font

def generate_images(rows, columns, block_size=10):
    img1_array = np.random.randint(0, 256, (rows, columns, 3), dtype=np.uint8)
    img2_array = img1_array.copy()

    target_row = random.randint(0, rows - 1)
    target_col = random.randint(0, columns - 1)

    # 将选择的像素转换为更大的整数类型，进行加法操作后再转换回来
    for i in range(3):
        new_value = int(img2_array[target_row][target_col][i]) + 128
        img2_array[target_row][target_col][i] = np.clip(new_value, 0, 255).astype(np.uint8)

    # 扩展每个色块的大小
    expanded_image_1_array = np.repeat(np.repeat(img1_array, block_size, axis=0), block_size, axis=1)
    expanded_image_2_array = np.repeat(np.repeat(img2_array, block_size, axis=0), block_size, axis=1)

    # 将 NumPy 数组转换为 PIL 图像
    img_1 = ImageTk.PhotoImage(Image.fromarray(expanded_image_1_array))
    img_2 = ImageTk.PhotoImage(Image.fromarray(expanded_image_2_array))
    return img_1, img_2, target_row, target_col



def display_images(master, img1, img2):
    image_window = tk.Toplevel(master)
    image_window.title("Images")

    # 创建一个字体对象，指定字体名称和大小
    title_font = font.Font(family="Helvetica", size=30)
    usage_font = font.Font(family="Helvetica", size=15)

    image_window.title_label = tk.Label(image_window,font=title_font, text=f"Find the different color block")
    image_window.title_label.pack()    
    image_window.usage_label = tk.Label(image_window,font=usage_font, text=f"Click the left mouse button to guess, press the spacebar to regenerate the image, and press Esc to close the window.")
    image_window.usage_label.pack()

    # 设置窗口的位置和大小
    image_window.attributes('-fullscreen', True)

    # 创建一个容器框架用于居中图像
    frame = tk.Frame(image_window)
    frame.pack(expand=True)

    # 使用 Label 小部件来显示图像
    label1 = tk.Label(frame, image=img1)
    label1.pack(side=tk.LEFT, padx=1, pady=1)  # 左边放置，减少间距

    label2 = tk.Label(frame, image=img2)
    label2.pack(side=tk.LEFT, padx=1, pady=1)  # 紧挨着左边放置，减少间距

    # 保持对图像对象的引用，以防止它们被垃圾回收
    label1.image = img1
    label2.image = img2

    return image_window



