import socket, threading


def server(conn, addr):
    while True:
        data = conn.recv(1024)
        if data == 'close' or not data:
            break
        conn.send(data)
    conn.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    t = threading.Thread(target=server, args=(conn, addr))
    t.start()

"""Можно сделать через github
В терминале:

> git init

> git remote add origin <git_url.git> https://github.com/Pitkincorp/Learning_Project/blob/c63e1e5c7fd65cc9f78d2f9ac89c2d3d399f5cac/St_14(echo-server_multythreaded).py

> git pull origin master """