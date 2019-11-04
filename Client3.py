import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.2', 8080))
name = input('Username: ')
while True:
    message = input('Mensaje: ')
    client.send(bytes(message+'\n', 'utf-8'))
    print(name,':', message)
client.close()
print(from_server)