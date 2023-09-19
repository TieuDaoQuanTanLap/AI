import sqlite3

notebook = sqlite3.connect("So_Tay.db")
mousebook = notebook.cursor()
mousebook.execute("CREATE TABLE IF NOT EXISTS noteter(title TEXT, content TEXT)")

# Phần lệnh hướng dẫn
def huongdan():
    feature = [
        "Sổ tay",
        "Trợ lý",
        "Đóng",
        "Viết: khi đã mở sổ tay",
        "Đọc: khi đã mở sổ tay",
        "Xóa: khi đã mở sổ tay",
        "Xóa hết: khi đã mở sổ tay",
        "Hiển thị: khi đã mở sổ tay",
        "Quay lại"
    ]
    print("_____________________")
    for i in feature:
        print("-", i)
    print("_____________________")

# Phần viết ghi chú
def viet():
    title = input("Tiêu đề: ").lower()
    content = input("Nội dung: ").lower()
    if title == "":
        print("Tiêu đề không được để trống!")
    elif content == "":
        print("Nội dung không được để trống!")
    else:
        mousebook.execute("INSERT INTO noteter VALUES (?, ?)", (title, content))
        notebook.commit()
        print("Lưu thành công!")

# Phần đọc ghi chú
def doc():
    while True:
        search = input("Tìm kiếm: ").lower()
        mousebook.execute("SELECT content FROM noteter WHERE title=?", (search,))
        reply = mousebook.fetchone()
        if reply is None:
            print("Không tìm thấy ghi chú nào như vậy?")
            while True:
                computer = input("Bạn muốn viết ghi chú này không: ")
                if computer == "viết":
                    viet()
                else:
                    break
        else:
            print(reply[0])

# Phần xóa dữ liệu trong bảng
def xoa():
    title = input("Nhập tiêu đề ghi chú cần xóa: ").lower()
    mousebook.execute("DELETE FROM noteter WHERE title=?", (title,))
    notebook.commit()
    print("Xóa thành công!")

# Phần xóa hết dữ liệu trong bảng
def xoa_het():
    confirm = input("Bạn có chắc chắn muốn xóa hết dữ liệu không? (yes/no): ").lower()
    if confirm == "yes":
        mousebook.execute("DELETE FROM noteter")
        notebook.commit()
        print("Xóa hết thành công!")
    else:
        print("Hủy xóa hết dữ liệu.")

# Phần hiển thị tất cả dữ liệu trong noter
def hien_thi():
    mousebook.execute("SELECT * FROM noteter")
    data = mousebook.fetchall()
    if len(data) == 0:
        print("Không có dữ liệu nào trong sổ tay.")
    else:
        for row in data:
            print("Tiêu đề:", row[0])
            print("Nội dung:", row[1])
            print("----------------------------")

print("Nhắc nhở: Nhập 'hướng dẫn' nếu chưa biết cách sử dụng!")
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
            elif you == "xóa":
                xoa()
            elif you == "xóa hết":
                xoa_het()
            elif you == "hiển thị":
                hien_thi()
            elif you == "đóng":
                break
            else:
                print("Sai cú pháp!")