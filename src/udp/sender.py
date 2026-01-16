"""
UDP Broadcast Sender - Sends broadcast messages over UDP.

This sender demonstrates:
- UDP socket creation (SOCK_DGRAM)
- Broadcast socket options
- Connectionless message sending
"""

import socket
import time

# Configuration constants
BIND_HOST: str = ""  # Bind to all interfaces
BIND_PORT: int = 44444  # Local port to bind
BROADCAST_ADDR: str = "255.255.255.255"  # Broadcast address
TARGET_PORT: int = 37020  # Port to send to
MESSAGE: bytes = b"your very important message"
SEND_INTERVAL: float = 1.0  # Seconds between messages
TIMEOUT: float = 0.2  # Socket timeout in seconds


def main() -> None:
    """Send broadcast messages in a loop."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Enable broadcast mode
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.settimeout(TIMEOUT)
            s.bind((BIND_HOST, BIND_PORT))

            print(f"UDP sender started on port {BIND_PORT}")
            print(f"Broadcasting to {BROADCAST_ADDR}:{TARGET_PORT}")

            while True:
                s.sendto(MESSAGE, (BROADCAST_ADDR, TARGET_PORT))
                print(f"Sent: {MESSAGE!r}")
                time.sleep(SEND_INTERVAL)

    except OSError as e:
        print(f"Socket error: {e}")
    except KeyboardInterrupt:
        print("\nSender stopped.")


if __name__ == "__main__":
    main()
