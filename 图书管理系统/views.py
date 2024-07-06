import tkinter as tk
from tkinter import ttk
from db import db

class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text="本作品由tkinter制作").pack()
        tk.Label(self, text="作者为2022003102 卢阳").pack()

class ChangeFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.id=tk.StringVar()
        self.bookname=tk.StringVar()
        self.author=tk.StringVar()
        self.press=tk.StringVar()
        self.status =tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0,pady=10)

        tk.Label(self,text="图书号" ).grid(row=1,column=1,pady=10)
        tk.Entry(self,textvariable=self.id).grid(row=1,column=2,pady=10)

        tk.Label(self,text="书名" ).grid(row=2,column=1,pady=10)
        tk.Entry(self,textvariable=self.bookname).grid(row=2,column=2,pady=10)

        tk.Label(self,text="作者" ).grid(row=3,column=1,pady=10)
        tk.Entry(self,textvariable=self.author).grid(row=3,column=2,pady=10)

        tk.Label(self,text="出版社" ).grid(row=4,column=1,pady=10)
        tk.Entry(self,textvariable=self.press).grid(row=4,column=2,pady=10)

        tk.Button(self,text="查询",command=self.search_user).grid(row=5,column=1,pady=10)
        tk.Button(self,text="修改",command=self.change_user).grid(row=5,column=2,pady=10)

        tk.Label(self,textvariable=self.status).grid(row=6,column=2,pady=10,sticky=tk.E)

    def search_user(self):
        flag, info = db.search_by_username(self.bookname.get())
        if flag:
            self.id.set(info["id"])
            self.bookname.set(info["bookname"])
            self.author.set(info["author"])
            self.press.set(info["press"])
            self.status.set("数据查询成功")
        else:
            self.status.set(info)

    def change_user(self):
        bks = {"id": self.id.get(), "bookname": self.bookname.get(), "author": self.author.get(), "press": self.press.get()}
        self.id.set("")
        self.bookname.set("")
        self.author.set("")
        self.press.set("")
        flag, message = db.update(bks)
        self.status.set(message)

class InsertFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.id=tk.StringVar()
        self.bookname=tk.StringVar()
        self.author=tk.StringVar()
        self.press=tk.StringVar()
        self.status =tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0,pady=10)

        tk.Label(self,text="图书号" ).grid(row=1,column=1,pady=10)
        tk.Entry(self,textvariable=self.id).grid(row=1,column=2,pady=10)

        tk.Label(self,text="书名" ).grid(row=2,column=1,pady=10)
        tk.Entry(self,textvariable=self.bookname).grid(row=2,column=2,pady=10)

        tk.Label(self,text="作者" ).grid(row=3,column=1,pady=10)
        tk.Entry(self,textvariable=self.author).grid(row=3,column=2,pady=10)

        tk.Label(self,text="出版社" ).grid(row=4,column=1,pady=10)
        tk.Entry(self,textvariable=self.press).grid(row=4,column=2,pady=10)

        tk.Button(self,text="录入",command=self.recode_infor).grid(row=5,column=2,pady=10)

        tk.Label(self,textvariable=self.status).grid(row=6,column=2,pady=10,sticky=tk.E)

    def recode_infor(self):
        bks = {"id": self.id.get(), "bookname": self.bookname.get(), "author": self.author.get(), "press": self.press.get()}
        self.id.set("")
        self.bookname.set("")
        self.author.set("")
        self.press.set("")
        db.insert(bks)
        self.status.set("插入数据成功")

class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.bookname=tk.StringVar()
        self.status=tk.StringVar()
        tk.Label(self, text="根据书名删除数据").pack()
        tk.Entry(self, textvariable=self.bookname).pack()
        tk.Button(self, text="删除",command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def delete(self):
        bookname = self.bookname.get()
        flag, message = db.delete_by_username(bookname)
        self.status.set(message)

class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.table_view = tk.Frame(self)
        self.table_view.pack()
        self.create_page()

    def create_page(self):
        columns = ("id", "bookname", "author", "press")
        self.tree_view = ttk.Treeview(self, show="headings", columns=columns)
        
        # 定义列
        self.tree_view.column("id", width=80, anchor="center")
        self.tree_view.column("bookname", width=80, anchor="center")
        self.tree_view.column("author", width=80, anchor="center")
        self.tree_view.column("press", width=80, anchor="center")
        
        self.tree_view.heading("id", text="图书号")
        self.tree_view.heading("bookname", text="书名")
        self.tree_view.heading("author", text="作者")
        self.tree_view.heading("press", text="出版社")
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.show_data_frame()

        tk.Button(self,text='刷新数据',command=self.show_data_frame).pack(anchor=tk.E,pady=5)

    def show_data_frame(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass 
        books = db.all()  # 获取所有书籍数据
        index = 0
        for bks in books:
            if isinstance(bks, dict):  # 确保bks是一个字典
                self.tree_view.insert('', index, values=(
                    bks['id'], bks['bookname'], bks['author'], bks['press']
                ))
                index += 1

if __name__ == '__main__':
    root = tk.Tk()
    notebook = ttk.Notebook(root)
    notebook.add(SearchFrame(notebook), text="查询")
    notebook.add(InsertFrame(notebook), text="插入")
    notebook.add(ChangeFrame(notebook), text="修改")
    notebook.add(DeleteFrame(notebook), text="删除")
    notebook.add(AboutFrame(notebook), text="关于")
    notebook.pack(expand=True, fill='both')
    root.mainloop()
