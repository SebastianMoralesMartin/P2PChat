import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
name = input('Username: ')
while True:
    message = input('Mensaje: ')
    client.send(bytes(message+'\n', 'utf-8'))
    print(name,':', message)
    from_server = client.recv(4096)
client.close()
print(from_server)