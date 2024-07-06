import tkinter as tk  
from tkinter import messagebox  
from db import db  # 假设您的db模块已经正确导入了check_login函数  
from MainPage import MainPage
  
class LoginPage:  
    def __init__(self, master):  
        self.root = master  
        self.root.geometry('300x150')  
        self.root.title('登录页')  
  
        self.username = tk.StringVar()  
        self.password = tk.StringVar()  
  
        self.page = tk.Frame(self.root)  
        self.page.pack()  
  
        tk.Label(self.page, text="账户").grid(row=1, column=1, pady=10)  
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=2)  
  
        tk.Label(self.page, text="密码").grid(row=2, column=1, pady=10)  
        tk.Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=2)  
  
        tk.Button(self.page, text="登录", command=self.login).grid(row=3, column=1, pady=10)  
        tk.Button(self.page, text="退出", command=self.quit).grid(row=3, column=2, pady=10)  
  
    def login(self):  
        name = self.username.get()  
        pwd = self.password.get()  
        flag, message = db.check_login(name, pwd)  
        print(name, pwd)  
        if flag:  
            self.page.destroy()
            MainPage(self.root)     
        else:  
            messagebox.showwarning(title="警告", message=message)  
  
    def quit(self):  
        self.root.destroy()  # 实现退出功能  
  
if __name__ == '__main__':  
    root = tk.Tk()  
    LoginPage(master=root)  
    root.mainloop()