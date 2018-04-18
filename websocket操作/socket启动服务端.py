import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(("127.0.0.1",8001))
sock.listen(5)
#等待用户连接
conn,address = sock.accept()
data = conn.recv(1024)
print(data)

conn.send("hello world!")
