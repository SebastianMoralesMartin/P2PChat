import socket
import json

HOST = '0.0.0.0'
PORT = 8080


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()

    with conn:
        while True:
            data = conn.recv(1024)
            new_data = data.decode()
            new_data = json.loads(data)
            print(new_data["Name"],"has connected from",addr)
            message = ("Hello %s welcome to the chat server" % new_data["Name"]).encode()
            conn.sendall(message)
            if not data:
                conn.sendall(data)
