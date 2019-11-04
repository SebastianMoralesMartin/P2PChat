import socket
import threading

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(1)
while True:
    conn, addr = serv.accept()
    from_client1 = []
    while True:
        data = conn.recv(4096)
        if not data:
            break
        from_client1.append(str(data))
        print(conn.getsockname() ,from_client1[-1])
        #serv.send(bytes("I am SERVER\n", 'utf-8'))
    conn.close()
    print('client disconnected')