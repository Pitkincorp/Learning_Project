import socket, threading


def server(conn, addr):
    data = conn.recv(1024)
    if not data or data == 'close':
        conn.close()
    conn.send(data)
    conn.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 2222))
sock.listen(10)
while True:
    conn, addr = sock.accept()
    print("Connection", addr)
    t = threading.Thread(target=server, args=(conn,addr))
    t.start()
