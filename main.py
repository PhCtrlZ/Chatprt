from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from QtGui import Ui_MainWindow
from tkinter import messagebox
import sys
import socket 
import threading

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        #start
        #self.uic.startbutton.clicked.connect(self.shows)
    #def shows(self):
        #self.uic.Screen.setText('Tool đã được khởi động')
        self.uic.english.clicked.connect(self.english)
        self.uic.vietnam.clicked.connect(self.vietnam)
        self.uic.start.clicked.connect(self.start)
        self.uic.stop.clicked.connect(self.stop)
    def english(self):
        self.uic.label_1.setText('Your ID')
        self.uic.label_2.setText('Your Pot')
        self.uic.label_3.setText('Your Name')
        self.uic.label_6.setText('Notice')
        self.uic.label_4.setText('Chat Middle')
        self.uic.Chat.setText('Convert language English succesfully!!!')
    def vietnam(self):
        self.uic.label_1.setText('ID riêng của bạn')
        self.uic.label_2.setText('Pot riêng của bạn')
        self.uic.label_3.setText('Tên của bạn')
        self.uic.label_6.setText('Bảng thông báo')
        self.uic.label_4.setText('Bảng nhắn tin trung tâm')
        self.uic.Chat.setText('Đã chuyển qua ngôn ngữ tiếng việt')
    def start(self):
        messagebox.showinfo("Thông Báo","Setting success!!!")
        copy=self.uic.ID.toPlainText()
        copy1=self.uic.Pot.toPlainText()
        copy2=self.uic.Name.toPlainText()
        copy3=self.uic.Chat.toPlainText()
        class ClientNode:
            def __init__(self):
                self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                port_and_ip = (copy, copy1)
                self.node.connect(port_and_ip)
            def send_sms(self, SMS):
                self.node.send(SMS.encode())
            def receive_sms(self):
                while True:       
                    data = self.node.recv(1024).decode()
                    print(data)
            def main(self):
                while True:
                    message = copy3
                    self.send_sms(copy2+":"+message)
        Client = ClientNode()
        always_receive = threading.Thread(target=Client.receive_sms)
        always_receive.daemon = True
        always_receive.start()
        Client.main()
    def stop(self):
        messagebox.showerror("Thông báo","The tool have been stoping!")
        sys.exit()
    def show(self):
        self.main_win.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
