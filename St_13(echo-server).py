import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 2222))
sock.listen(10)
while True:
    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data or data == 'close':
            conn.close()
            break
        conn.send(data)
