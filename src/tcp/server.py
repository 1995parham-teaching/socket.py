"""
TCP Echo Server - A multi-threaded server that echoes back received messages.

This server demonstrates:
- Socket creation and binding
- Multi-threaded client handling
- Proper resource cleanup with context managers
"""

import socket
import threading
from typing import Tuple

# Configuration constants
HOST: str = "0.0.0.0"  # Listen on all interfaces
PORT: int = 1234  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE: int = 1024  # Maximum bytes to receive at once


class Handler(threading.Thread):
    """Thread handler for individual client connections."""

    def __init__(self, conn: socket.socket, addr: Tuple[str, int]) -> None:
        self.conn = conn
        self.addr = addr
        super().__init__(name=f"client-{addr[0]}:{addr[1]}")

    def run(self) -> None:
        """Handle client communication in a separate thread."""
        with self.conn:
            print(f"Connected by {self.addr}")
            try:
                while True:
                    data = self.conn.recv(BUFFER_SIZE)
                    if not data:
                        break
                    print(f"Received from {self.addr}: {data.decode()}")
                    self.conn.sendall(data)
            except ConnectionResetError:
                print(f"Connection reset by {self.addr}")
            except OSError as e:
                print(f"Socket error with {self.addr}: {e}")
            finally:
                print(f"Disconnected: {self.addr}")


def main() -> None:
    """Start the TCP echo server."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Allow address reuse to avoid "Address already in use" errors
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen()
            print(f"Server listening on {HOST}:{PORT}")

            while True:
                conn, addr = s.accept()
                Handler(conn, addr).start()
    except OSError as e:
        print(f"Server error: {e}")
    except KeyboardInterrupt:
        print("\nServer shutting down...")


if __name__ == "__main__":
    main()
