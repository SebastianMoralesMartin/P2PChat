import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
while True:
    message = input('Mensaje: ')
    client.send(bytes(message+'\n', 'utf-8'))
    print('You:', message)
    from_server = client.recv(4096)
client.close()
print(from_server)