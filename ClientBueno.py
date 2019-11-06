#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def receive():
    while True:
        try:
            msg = client.recv(BUFSIZ).decode("utf8")
            desencryptedMsg = encryptMsg(msg)
            print(desencryptedMsg)
        except OSError:
            break


def encryptMsg(msg):
    b = bytearray(msg, "utf-8")
    criptedStr = ""
    for byt in b:
        t = int(byt)
        key = int(bin(127), 2)
        cripted = bin(t ^ key)
        strCrypt = chr(int(cripted, 2))
        criptedStr += strCrypt
    return criptedStr


def send():
    msg = input("")
    criptedMsg = encryptMsg(msg)
    client.send(bytes(criptedMsg, "utf8"))
    if msg == "{quit}":
        client.close()
        exit()


HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

contador = 0

client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

while True:
    send()
