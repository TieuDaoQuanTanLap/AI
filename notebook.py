import sqlite3
notebook = sqlite3.connect("So_Tay.db")
mouse = notebook.cursor()
mouse.execute("CREATE TABLE IF NOT EXISTS data(title TEXT, content TEXT)")
menu = [
    "Sổ tay",
    "Trợ lý",
    "Đóng",
    "Viết: khi đã mở sổ tay",
    "Đọc: khi đã mở sổ tay",
    "Quay lại"
]
# _________________________________
def huongdan():
    print("_____________________\n")
    for i in menu:
        print("-", i)
    print("_____________________")
# _________________________________
def viet():
    title = input("Tiêu đề: ").lower()
    content = input("Nội dung: ").lower()
    if title == "":
        print("Tiêu đề không được để trống!")
    elif content == "":
        print("Nội dung không được để trống!")
    else:
        mouse.execute("INSERT INTO data VALUES (?, ?)", (title, content))
        notebook.commit()
        print("Lưu thành công!")
# ___________________________________________________________________________
def doc():
    while True:
        search = input("Tìm kiếm: ").lower()
        mouse.execute("SELECT content FROM data WHERE title=?", (search,))
        reply = mouse.fetchone()
        if reply == None:
            print("Không tìm thấy ghi chú nào như vậy?")
            while True:
                computer = input("Bạn muốn viết ghi chú này không: ")
                if computer == "viết":
                    viet()
                else:
                    break
        else:
            print(reply[0])
print("Nhắc nhở: Nhập >>hướng dẫn<< nếu chưa biết cách sử dụng!")
# ___________________________________________________________________________
# ###########################################################################

while True:
    command = input("Bạn cần gì: ").lower()
    if command == "hướng dẫn":
        huongdan()
    elif command == "":
        print("Tôi không hiểu ý bạn?")
    elif command == "sổ tay":
        while True:
            you = input("Bạn: ").lower()
            if you == "hướng dẫn":
                huongdan()
            elif you == "viết":
                viet()
            elif you == "đọc":
                doc()
            elif you == "đóng":
                break
            else:
                print("Sai cú pháp!")
    elif command == "trợ lý":
        # e chưa có kiến thức xịn để viết thêm ạ=))
        pass