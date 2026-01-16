"""
UDP Broadcast Receiver - Listens for UDP broadcast messages.

This receiver demonstrates:
- UDP socket creation (SOCK_DGRAM)
- Broadcast socket options
- Connectionless message receiving
- Important: UDP data exceeding buffer size is lost
"""

import socket
from typing import Tuple

# Configuration constants
BIND_HOST: str = ""  # Bind to all interfaces
BIND_PORT: int = 37020  # Port to listen on
BUFFER_SIZE: int = 1024  # Maximum bytes to receive (excess data is lost!)


def main() -> None:
    """Listen for and display broadcast messages."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Enable broadcast mode
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.bind((BIND_HOST, BIND_PORT))

            print(f"UDP receiver listening on port {BIND_PORT}")
            print(f"Buffer size: {BUFFER_SIZE} bytes")

            while True:
                data, addr = s.recvfrom(BUFFER_SIZE)
                print(f"Received from {addr}: {data!r}")

    except OSError as e:
        print(f"Socket error: {e}")
    except KeyboardInterrupt:
        print("\nReceiver stopped.")


if __name__ == "__main__":
    main()
