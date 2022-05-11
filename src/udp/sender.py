'''
udp_sender sends packets with broadcast address to port 37020.
'''
import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(0.2)
server.bind(("", 44444))
MESSAGE = b"your very important message"
while True:
    server.sendto(MESSAGE, ('255.255.255.255', 37020))
    print("message sent, wait for 1 sec!")
    time.sleep(1)
