import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 1234))
    s.sendall('سلام دنیا'.encode())
    b = s.recv(1024)
    print(f"{b.decode()}")
