import socket
import threading

class Handler(threading.Thread):
    def __init__(self, conn):
        self.conn = conn
        super().__init__()

    def run(self):
        with self.conn:
            while True:
                b = self.conn.recv(1024)
                if not b:
                    break
                print(f"{b.decode()}")
                self.conn.sendall(b)
        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 1234))
    s.listen()
    while True:
        conn, addr = s.accept()
        Handler(conn).start()
