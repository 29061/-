import tkinter as tk
from views import AboutFrame,ChangeFrame,InsertFrame,DeleteFrame,SearchFrame

class MainPage :
    def __init__(self,master:tk.Tk):
        self.root=master
        self.root.title("图书信息界面")
        self.root.geometry('600x400')
        self.create_page() 


    def create_page(self):
        self.about_frame=AboutFrame(self.root)
        self.insert_frame=InsertFrame(self.root)
        self.change_frame=ChangeFrame(self.root)
        self.delete_frame=DeleteFrame(self.root)
        self.search_frame=SearchFrame(self.root)
        #tk.Label(self.change_frame,text="修改界面").pack()  ##之后再操作




        menu_bar=tk.Menu(self.root)
        menu_bar.add_command(label='录入',command=self.show_insert)
        menu_bar.add_command(label='查询',command=self.show_search)
        menu_bar.add_command(label='删除',command=self.show_delete)
        menu_bar.add_command(label='修改',command=self.show_change)
        menu_bar.add_command(label='关于',command=self.show_about)
        
        self.root.config(menu=menu_bar)


    def show_about(self):
        self.change_frame.pack_forget() 
        self.insert_frame.pack_forget() 
        self.about_frame.pack()
        self.delete_frame.pack_forget() 
        self.search_frame.pack_forget() 

    def show_insert(self):
        self.change_frame.pack_forget() 
        self.insert_frame.pack()
        self.about_frame.pack_forget() 
        self.delete_frame.pack_forget() 
        self.search_frame.pack_forget() 

    def show_delete(self):
        self.change_frame.pack_forget() 
        self.insert_frame.pack_forget() 
        self.about_frame.pack_forget() 
        self.delete_frame.pack()
        self.search_frame.pack_forget() 
        
    def show_change(self):
        self.change_frame.pack()
        self.insert_frame.pack_forget() 
        self.about_frame.pack_forget() 
        self.delete_frame.pack_forget() 
        self.search_frame.pack_forget() 

    def show_search(self):
        self.change_frame.pack_forget() 
        self.insert_frame.pack_forget() 
        self.about_frame.pack_forget() 
        self.delete_frame.pack_forget() 
        self.search_frame.pack()




 
if __name__ =='__main__':
    root =tk.Tk()
    MainPage(root)
    root.mainloop()
        