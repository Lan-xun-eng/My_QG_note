from datetime import date
import json
import os
DATA_FILE = "E:\\pycharm项目\\QG\\data\\library_data.json"

# 数据结构
class Book:
    def __init__(self, title, author, isbn, available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["author"],
            data["isbn"],
            data["available"]
        )

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        self.borrowed_books = []

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["username"],
            data["password"],
            data["role"]
        )

class BorrowRecord:
    def __init__(self, username, isbn, borrow_date = None, return_date = None, returned = False):
        self.username = username
        self.isbn = isbn
        self.borrow_date = borrow_date if borrow_date is not None else date.today().isoformat()
        self.return_date = return_date
        self.returned = returned

    def to_dict(self):
        return {
            "username": self.username,
            "isbn": self.isbn,
            "borrow_date": self.borrow_date,
            "return_date": self.return_date,
            "returned": self.returned
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["username"],
            data["isbn"],
            data["borrow_date"],
            data["return_date"],
            data["returned"]
        )

# 导入文件
def load_data():
    global books, users, records

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        books = [Book.from_dict(b) for b in data.get("books", [])]
        users = [User.from_dict(u) for u in data.get("users", [])]
        records = [BorrowRecord.from_dict(r) for r in data.get("records", [])]

        print("图书管理系统数据加载成功！")

    except FileNotFoundError:
        print("未找到数据文件，将使用默认数据")

# 导出函数
def save_data():
    data = {
        "books": [b.to_dict() for b in books],
        "users": [u.to_dict() for u in users],
        "records": [r.to_dict() for r in records]
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("图书管理系统数据已保存成功！")

# 登陆
def login(users):
    username = input("请输入用户名： ").strip()
    if not username:
        print("用户名不能为空。")
        return None

    password = input("请输入密码：").strip()
    if not password:
        print("密码不能为空。")
        return None

    for user in users:
        if user.username == username and user.password == password:
            print(f"登陆成功！"
                  f"您的身份：{user.role}")
            return user

    print("登陆失败！请重新登陆。")
    return None

# 注册
def register(users):
    username = input("请输入用户名：").strip()
    if not username:
        print("用户名不能为空")
        return None

    for u in users:
        if u.username == username:
            print("该用户名已存在，请选择其它用户名")
            return None

    password = input("请输入密码：").strip()
    if not password:
        print("密码不能为空")
        return None

    password_confirm = input("请再次输入密码以确认：").strip()
    if password != password_confirm:
        print("两次输入的密码不一致，请退出重试！")
        return None

    while True:
        role_input = input("请选择身份（读者 reader / 管理员 admin）：").strip().lower()
        if role_input in ("reader", "读者"):
            role = "reader"
            break
        elif role_input in ("admin", "管理员"):
            role = "admin"
            break
        else:
            print("无效的身份!请输入 'reader' 或 'admin'")

    new_user = User(username, password, role)
    users.append(new_user)

    print("注册成功！")

    islogin = input("您现在是是否登陆? (y/n)").strip().lower()
    if islogin == "y":
        user = login(users)
        return user
    elif islogin == "n":
        print("即将退出系统，期待您后续登陆！！！")
    return None


# 查询图书
def query_book(user, books):
    query_title = input("查询书籍的书名（可留空）： ").strip()
    query_isbn = input("查询书籍的isbn码（可留空）：").strip()

    found_books = []
    for book in books:
        if query_title and book.title != query_title:
            continue
        if query_isbn and book.isbn != query_isbn:
            continue
        found_books.append(book)

    if not found_books:
        print("没有找到符合条件的图书，请仔细检查一下，重新输入吧~~")
    else:
        print(f"报告！共找到{len(found_books)}本图书：\n")
        for found_book in found_books:
            print(f"书名：{found_book.title}\n"
                  f"作者：{found_book.author}\n"
                  f"isbn：{found_book.isbn}\n"
                  f"是否可借：{found_book.available}")
            print()
    return None

# 借阅图书
def borrow_book(books, records, user):
    borrow_title = input("借阅书籍的书名（可留空）： ").strip()
    borrow_isbn = input("借阅书籍的isbn（可留空）： ").strip()

    if not borrow_title and not borrow_isbn:
        print("书名和isbn不能同时为空！")
        return None

    isfound = False
    for book in books:
        if (not borrow_title or book.title == borrow_title) and (not borrow_isbn or book.isbn == borrow_isbn):
            isfound = True
            if not book.available:
                print("该书已被借出，无法借阅。")
                return None

            book.available = False

            new_record = BorrowRecord(user.username, book.isbn)
            records.append(new_record)

            user.borrowed_books.append(new_record)

            print("借阅成功！")
            print("借阅记录已生成并录入。")
            break
    if not isfound:
        print("图书馆暂无该图书，我们正在拼命扩展藏书量ing~~")
    return None

# 归还图书
def return_book(books, records, user):
    return_isbn = input("归还书籍的isbn码：").strip()

    target_record = None
    for record in records:
        if record.username == user.username and not record.returned:
            if record.isbn == return_isbn:
                target_record = record
                break

    if not target_record:
        print("未找到您的未归还记录，请核对信息。")
        return None

    target_record.return_date = date.today().isoformat()
    target_record.returned = True

    if target_record in user.borrowed_books:
        user.borrowed_books.remove(target_record)

    for book in books:
        if book.isbn == target_record.isbn:
            book.available = True
            break

    print("归还成功！")
    return None

# 查阅借阅历史
def search_borrowed_history(user, records):
    target_history = []
    for record in records:
        if record.username == user.username:
            target_history.append(record)

    if not target_history:
        print("暂无借阅历史。")
        return None

    print("您的借阅历史：")
    for i, record in enumerate(target_history):
        status = "已归还" if record.returned else "借阅中"
        title = get_book_title(record.isbn)
        print(f"{i+1}. 书名：{title}   ISBN：{record.isbn}   借阅时间：{record.borrow_date}   状态：{status}")

    return None

def get_book_title(isbn):
    for book in books:
        if book.isbn == isbn:
            return book.title
    return "未知书名"


# 添加图书
def add_book(user, books):
    new_book_title = input("添加书籍的书名：")
    new_book_author = input("添加书籍的作者：")
    new_book_isbn = input("添加书籍的isbn码：")

    if not (new_book_title and new_book_author and new_book_isbn):
        print("添加失败，书名、作者、isbn都不能为空！")
        return None

    for book in books:
        if book.isbn == new_book_isbn:
            print("添加失败，该isbn已存在！")
            return None

    if new_book_title and new_book_author and new_book_isbn:
        new_book = Book(new_book_title, new_book_author, new_book_isbn)
        books.append(new_book)
        print("添加成功！")
        print(f"当前图书馆内共有藏书：{len(books)} 本")
    else:
        print("添加失败，请重新核对并添加信息。")
    return None


# 删除图书
def drop_book(user, books):
    drop_book_title = input("删除书籍的书名：")
    drop_book_isbn = input("删除书籍的isbn码：")

    if not (drop_book_title and drop_book_isbn):
        print("书名和isbn不能为空！")
        return None

    if drop_book_title and drop_book_isbn:
        for book in books:
            if book.title == drop_book_title and book.isbn == drop_book_isbn:
                books.remove(book)
                print("删除成功！")
                print(f"当前图书馆内共有藏书：{len(books)} 本")
                return None
        print("未找到该图书，请核对后重新输入。")
    else:
        print("删除失败，请重新核对并删除书籍。")
    return None


# 修改图书信息
def change_book_info(user, books):
    book_title  = input("修改书籍的书名：")

    if not book_title:
        print("书名不能为空！请重新输入喔~~")
        return None

    isfound = False
    for book in books:
        if book.title == book_title:
            isfound = True

            print(f"找到图书：{book.title}"
                  f"当前信息：作者 = {book.author}，isbn = {book.isbn}，是否可借 = {book.available}")

            new_isbn = input("修改书籍的isbn码（留空则不修改）：")
            new_author = input("修改书籍的作者（留空则不修改）：")
            new_available = bool(input("修改书籍的状态（输入True/False,留空则不修改）："))

            if new_isbn:
                book.isbn = new_isbn
            if new_author:
                book.author = new_author
            if new_available:
                book.available = new_available

    if not isfound:
        print("未找到该图书，请核查后重新输入喔~~")
    return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    os.system("pause")

# 菜单显示
def show_menu(user):
    if user.role == 'reader':
        print("读者菜单：")
        print("0. 退出")
        print("1. 查询图书")
        print("2. 借阅图书")
        print("3. 归还图书")
        print("4. 查看我的借阅历史")
    elif user.role == 'admin':
        print("管理员菜单：")
        print("0. 退出")
        print("1. 添加图书")
        print("2. 删除图书")
        print("3. 查询图书")
        print("4. 修改图书信息")


# 用户选择
def choose_menu(user):
    if user.role == 'reader':
        while True:
            clear_screen()
            show_menu(user)
            menu_choice = input("读者您好！您的选择：").strip()

            if menu_choice == '0':
                print("感谢使用GDUT图书管理系统，再见！！！")
                break
            elif menu_choice == '1':
                query_book(user, books)
                pause()
            elif menu_choice == '2':
                borrow_book(books, records, user)
                pause()
            elif menu_choice == '3':
                return_book(books, records, user)
                pause()
            elif menu_choice == '4':
                search_borrowed_history(user, records)
                pause()
            else:
                print("无效输入！请重新输入您的选择。")
    elif user.role == 'admin':
        while True:
            clear_screen()
            show_menu(user)
            menu_choice = input("管理员您好！您的选择：").strip()

            if menu_choice == '0':
                print("感谢使用GDUT图书管理系统，再见！！！")
                break
            elif menu_choice == '1':
                add_book(user, books)
                pause()
            elif menu_choice == '2':
                drop_book(user, books)
                pause()
            elif menu_choice == '3':
                query_book(user, books)
                pause()
            elif menu_choice == '4':
                change_book_info(user, books)
                pause()
            else:
                print("无效输入！请重新输入您的选择。")


# 主函数流程
def main():
    load_data()
    while True:
        choice = input("请选择（login/register/exit）：").strip().lower()
        if choice == 'login':
            user = login(users)
            if user:
                choose_menu(user)
        elif choice == 'register':
            user = register(users)
            # 如果注册后直接登录 register 已处理
            if user:
                choose_menu(user)
        elif choice == 'exit':
            save_data()
            print("已退出图书管理系统，期待您的下次光临喔~~")
            break
        else:
            print("输入无效！请选择所需的方式")

if __name__ == '__main__':
    main()