#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
#
def receive():
    while True:
        try:
            msg = client.recv(BUFSIZ).decode("utf8")
            desencryptedMsg = encryptMsg(msg)
            chat_box.insert(tkinter.END, desencryptedMsg)
            #print(desencryptedMsg + "\n")
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
    msg = sent_msg.get()
    criptedMsg = encryptMsg(msg)
    sent_msg.set("")
    client.send(bytes(criptedMsg, "utf8"))
    if msg == "{quit}":
        client.close()
        exit()

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    sent_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chat")

frame = tkinter.Frame(top)
scroll = tkinter.Scrollbar(frame)
chat_box = tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scroll.set)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
chat_box.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
chat_box.pack()
frame.pack()
sent_msg = tkinter.StringVar()  # For the messages to be sent.
sent_msg.set("")
input_field = tkinter.Entry(top, textvariable=sent_msg)
input_field.bind("<Return>", send)
input_field.pack()
sendButton = tkinter.Button(top, text='Enviar', command=send)
sendButton.pack()


top.protocol("WM_DELETE_WINDOW", on_closing)




HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)


client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
