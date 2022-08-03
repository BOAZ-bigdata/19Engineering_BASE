class MultiClient(object):
    def __init__(self, username):
        self.username = username

import socket
from _thread import *

ADDR = "0.0.0.0"
PORT = 9080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((ADDR, PORT))

    def receive_data(client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                print(str(data.decode()))
            except ConnectionResetError as e:
                print("서버와의 연결이 끊겼습니다.")
                break


    start_new_thread(receive_data, (client_socket,))

    name = input("Enter Your Name: ")
    user = MultiClient(name)
    client_socket.send(name.encode())

    while True:
        message = input()

        if message == 'quit':
            break

        client_socket.send(message.encode())

    client_socket.close()
    
except ConnectionRefusedError as e:
    print("서버가 닫혀있습니다.")