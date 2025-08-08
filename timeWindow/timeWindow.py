import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk

def custom_messagebox(parent, title, message, icon_path):
    # 创建一个新的顶层窗口
    message_window = Toplevel(parent)
    message_window.title(title)
    message_window.attributes('-topmost', True)  # 窗口固定在顶层

    # 设置窗口图标
    try:
        icon = Image.open(icon_path)
        icon = ImageTk.PhotoImage(icon)
        message_window.iconphoto(False, icon)
    except Exception as e:
        print(f"Error loading icon: {e}")

    # 添加标签显示消息
    label = tk.Label(message_window, text=message, font=("Helvetica", 12))
    label.pack(pady=20, padx=20)

    # 添加一个按钮以关闭消息框
    ok_button = tk.Button(message_window, text="OK", command=message_window.destroy, width=20)
    ok_button.pack(pady=10)

    # 设置窗口大小和位置
    message_window.geometry("500x150+{}+{}".format(
        parent.winfo_rootx() + parent.winfo_width() // 2 - 250,
        parent.winfo_rooty() + parent.winfo_height() // 2 - 75
    ))

def timeLimit(self, master, time_seconds, timeout_callback=None):
    def countdown(count):
        if count > 0:
            time_label.config(text=f"Time remaining: {count} seconds")
            master.after(1000, countdown, count-1)
        else:
            if timeout_callback:
                if self.correct_count == 0:
                    message_str = "Uh-oh~Try again next time!!"
                elif self.correct_count == 1:
                    message_str = "Congratulations!! You've made " + str(self.correct_count) + " correct guess!"
                else:
                    message_str = "Congratulations!! You've made " + str(self.correct_count) + " correct guesses!"
                time_window.destroy()
                custom_messagebox(master, "Time's Up", message_str, ".//icon_transparentbg.png")
                timeout_callback()

    time_window = tk.Toplevel(master)
    time_window.title("Time Limit")
    time_window.attributes('-topmost', True)

    # 设置窗口图标
    try:
        icon = Image.open(".//icon_transparentbg.png")
        icon = ImageTk.PhotoImage(icon)
        time_window.iconphoto(False, icon)
    except Exception as e:
        print(f"Error loading icon: {e}")

    time_label = tk.Label(time_window, text="", font=("Helvetica", 16))
    time_label.pack(pady=20)
    countdown(time_seconds)

    return time_window
