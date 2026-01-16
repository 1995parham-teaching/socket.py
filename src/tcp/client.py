"""
TCP Echo Client - Connects to a server and sends/receives a message.

This client demonstrates:
- Socket creation and connection
- Proper error handling for connection failures
- String encoding/decoding for network transmission
"""

import socket

# Configuration constants
HOST: str = "127.0.0.1"  # The server's hostname or IP address
PORT: int = 1234  # The port used by the server
BUFFER_SIZE: int = 1024  # Maximum bytes to receive at once
MESSAGE: str = "Hello, World!"  # Message to send


def main() -> None:
    """Connect to server and exchange a message."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"Connecting to {HOST}:{PORT}...")
            s.connect((HOST, PORT))
            print("Connected!")

            # Send the message (encode string to bytes)
            s.sendall(MESSAGE.encode("utf-8"))
            print(f"Sent: {MESSAGE}")

            # Receive the echo response
            data = s.recv(BUFFER_SIZE)
            response = data.decode("utf-8")
            print(f"Received: {response}")

    except ConnectionRefusedError:
        print(f"Connection refused - is the server running on {HOST}:{PORT}?")
    except socket.timeout:
        print("Connection timed out")
    except OSError as e:
        print(f"Socket error: {e}")


if __name__ == "__main__":
    main()
