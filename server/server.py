import sqlite3
import socket
import struct
import threading

class Server():
    def __init__(self, port = 9090, maxcon = 1):
        self.sock = socket.socket()
        self.conn = None
        self.addr = None

        self.sock.bind(('', port))
        self.sock.listen(maxcon)

    def _user_start(self):
        pass

    def work(self):
        # ждем, пока к нам кто-то подключится
        self.conn, self.addr = self.sock.accept()
        # когда к нам кто-то подключился - печатаем его адрес
        size = struct.unpack('<I', self.conn.recv(4))[0]
        message = self.conn.recv(size)
        print('Connected: ', self.addr, 'Размер: ', size, "Сообщение: ", message)
        # тут будет передача данных
        mwd = message.split("|")
        print(mwd)
        # в конце - закрываем соединение
        self.conn.close()

server = Server()
while True:
    server.work()