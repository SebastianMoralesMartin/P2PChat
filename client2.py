import socket
import json

HOST = '127.0.0.1'
PORT = 8080

my_dict = {"Name":"RicoVEVO"}
jsn = json.dumps(my_dict)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall((jsn).encode())
    data = s.recv(1024)
    print(data)
