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
        # ???
        # Hint) 소켓의 데이터를 무한 루프로 받아와야할지도?
        return 

    start_new_thread(receive_data, (client_socket,))

    name = input("Enter Your Name: ")
    client_socket.send(name.encode())

    while True:
        message = input()

        if message == 'quit':
            break

        client_socket.send(message.encode())

    client_socket.close()
    
except ConnectionRefusedError as e:
    print("서버가 닫혀있습니다.")