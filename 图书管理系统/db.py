import json

class MysqlDatabases:
    def __init__(self):
        with open("users.json", mode="r", encoding="utf-8") as user_file:
            self.users = json.load(user_file)
        with open("books.json", mode="r", encoding="utf-8") as book_file:
            self.books = json.load(book_file)
        
    def check_login(self, username, password):
        if self.users["username"] == username and self.users["password"] == password:
            return True, "登录成功"
        else:
            return False, "登录失败，用户名或密码错误"
        
    def all(self):
        return self.books
    
    def insert(self, book):
        self.books.append(book)
        self._save_books()

    def delete_by_username(self, bookname):
        for book in self.books:
            if book["bookname"] == bookname:
                self.books.remove(book)
                self._save_books()
                return True, "删除成功"
        return False, "书籍不存在"

    def search_by_username(self, bookname):
        for book in self.books:
            if book["bookname"] == bookname:
                return True, book
        return False, f"{bookname}书籍不存在"
    
    def update(self, bks):
        for book in self.books:
            if book["id"] == bks["id"]:
                book.update(bks)
                self._save_books()
                return True, f"{bks['id']} 书籍数据修改成功"
        return False, f"{bks['id']}书籍不存在"
    
    def _save_books(self):
        with open("books.json", mode="w", encoding="utf-8") as book_file:
            json.dump(self.books, book_file, ensure_ascii=False, indent=4)

db = MysqlDatabases()

if __name__ == "__main__":
    print(db.search_by_username("正心"))
