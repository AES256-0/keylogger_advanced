import socket



sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("127.0.0.1",8090))
sock.listen(1)
while True:
    client_sock,addr=sock.accept()
    data=client_sock.recv(1024)
    fd=open("recv_file","a")
    fd.write(data.decode())
    fd.close()
