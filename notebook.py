import sqlite3
import nltk
import numpy as np
import sklearn
import tensorflow as tf
import keras
from flask import Flask
import django
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
    "Quay lại"
]
    print("_____________________\n")
    for i in feature:
        print("-", i)
    print("_____________________")
# Phần viêt ghi chú
def viet():
    title = input("Tiêu đề: ").lower()
    content = input("Nội dung: ").lower()
    if title == "":
        print("Tiêu đề không được để trống!")
    elif content == "":
        print("Nội dung không được để trống!")
    else:
        mousebook.execute("INSERT INTO data VALUES (?, ?)", (title, content))
        notebook.commit()
        print("Lưu thành công!")
# Phần đọc ghi chú
def doc():
    while True:
        search = input("Tìm kiếm: ").lower()
        mousebook.execute("SELECT content FROM data WHERE title=?", (search,))
        reply = mousebook.fetchone()
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