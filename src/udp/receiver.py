'''
udp_receiver listens on port 37020 to read data packets.
'''
import socket

# create udp socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# set socket options for broadcasting
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# bind on 37020 to receive packets
client.bind(("", 37020))
while True:
    # read packets with maximum size of 1024
    data, addr = client.recvfrom(1024)
    print(f"received message from {addr}: {data!r}")
