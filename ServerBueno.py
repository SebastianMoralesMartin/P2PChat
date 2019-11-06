from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

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

def accept_incoming_connections():

    while True:
        client, client_address = SERVER.accept()
        connected = ("%s:%s has connected." % client_address)
        connected = encryptMsg(connected)
        print(connected)
        typeName = "Type your name and press enter"
        typeName = encryptMsg(typeName)
        client.send(bytes(typeName, "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    welcome = encryptMsg(welcome)
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    msg = encryptMsg(msg)
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + ": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}

HOST = '192.168.56.1'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()