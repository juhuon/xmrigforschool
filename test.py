import tkinter as tk
import os
# 显示安装完成窗口
def finishclass():
    # 创建窗口对象
    window = tk.Tk()
    window.title("安装完成")  # 设置窗口标题
    window.geometry("500x200")  # 设置窗口大小
    window.resizable(False, False)  # 设置窗口不可调整大小

    text = tk.Text(window, wrap=tk.WORD, height=3)  #组件的wrap属性为tk.WORD，即按单词换行
    text.insert(tk.END, "安装完成，为保证程序正常运行，我们强烈建议（要求）您将此程序添加到反病毒软件的信任、排除列表。360等第三方鸡肋软件自行启动添加。")
    text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    # 重启电脑
    def restart():
        os.system("shutdown -r -t 0")

    # 运行程序，但不重启
    def run():
        os.system("C:\\1.exe")

    # 帮助运行程序
    def help():
        os.system("dist\\1.exe")

    button1 = tk.Button(window, text="完成并重启计算机", command=restart)
    button1.grid(row=1, column=0, padx=10, pady=10)

    button2 = tk.Button(window, text="运行程序，但不重启", command=run)
    button2.grid(row=1, column=1, padx=10, pady=10)

    button3 = tk.Button(window, text="使用工具 添加Defender排除项", command=help)
    button3.grid(row=1, column=2, padx=10, pady=10)

    # 设置窗口置顶并居中显示
    window.attributes('-topmost', True)
    window.update_idletasks()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry("+%d+%d" % (x, y))

    window.mainloop()
finishclass()