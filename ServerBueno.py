from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
#sent

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
        connected = client_address + ' se ha conectado.'
        connected = encryptMsg(connected)
        print(connected)
        typeName = "Ingresa tu Nickname y hax click en Enviar"
        typeName = encryptMsg(typeName)
        client.send(bytes(typeName, "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Bienvenido! Cuando desees desconectarte, teclea {quit} para salir.'
    welcome = encryptMsg(welcome)
    client.send(bytes(welcome, "utf8"))
    msg = "%s se unio al chat! :-)" % name
    msg = encryptMsg(msg)
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            added=encryptMsg(": ")
            print(added)
            broadcast(msg, name + added)
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s ha salido del chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}

HOST = '10.48.102.143'#input('direccion del host: ')
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(10)
    print("Esperando conexiones con clientes...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()