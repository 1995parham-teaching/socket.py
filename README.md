# socket.py

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/cng-by-example/socket.py?label=Lecture&logo=github&style=for-the-badge)](https://github.com/1995parham-teaching/socket.py/releases/latest)

## Introduction

Introduction to socket programming with Python, used for hands-on sessions in the Computer Networking course at Amirkabir University of Technology.

This repository provides practical examples of network communication using Python's `socket` module. It covers both **TCP** (connection-oriented) and **UDP** (connectionless) protocols, helping students understand low-level network programming without spending too much time on setup.

The chosen language is Python, which is also used in the textbook [Computer Networking: A Top-Down Approach](https://www.pearson.com/en-us/subject-catalog/p/computer-networking-a-top-down-approach/P200000013385) by Jim Kurose and Keith Ross.

## Prerequisites

- Python 3.8 or higher
- Basic understanding of networking concepts (IP addresses, ports, TCP/UDP)

## Directory Structure

```text
socket.py/
├── README.md
├── LICENSE
├── lecture/
│   └── main.tex          # LaTeX source for lecture notes
└── src/
    ├── tcp/
    │   ├── server.py     # Multi-threaded TCP echo server
    │   └── client.py     # TCP echo client
    └── udp/
        ├── sender.py     # UDP broadcast sender
        └── receiver.py   # UDP broadcast receiver
```

## Quick Start

### TCP Echo Server & Client

The TCP example demonstrates a simple echo server that receives messages and sends them back to the client.

**Terminal 1 - Start the server:**

```bash
python src/tcp/server.py
```

**Terminal 2 - Run the client:**

```bash
python src/tcp/client.py
```

The client sends a message to the server, and the server echoes it back.

### UDP Broadcast

The UDP example demonstrates broadcasting messages across a network.

**Terminal 1 - Start the receiver:**

```bash
python src/udp/receiver.py
```

**Terminal 2 - Start the sender:**

```bash
python src/udp/sender.py
```

The sender broadcasts messages every second, which are received by the receiver.

## What You'll Learn

| Topic             | Description                                                              |
| ----------------- | ------------------------------------------------------------------------ |
| Socket Creation   | Using `socket.socket()` with different address families and socket types |
| TCP Server        | Binding, listening, accepting connections, and handling clients          |
| TCP Client        | Connecting to servers and exchanging data                                |
| Multi-threading   | Handling multiple clients concurrently using `threading`                 |
| UDP Communication | Connectionless data transfer and broadcasting                            |
| Socket Options    | Configuring sockets with `setsockopt()` (e.g., `SO_BROADCAST`)           |

## Key Concepts

### Address Families

- `AF_INET` - IPv4 addresses
- `AF_INET6` - IPv6 addresses

### Socket Types

- `SOCK_STREAM` - TCP (reliable, connection-oriented)
- `SOCK_DGRAM` - UDP (unreliable, connectionless)

### TCP vs UDP

| Feature     | TCP                 | UDP               |
| ----------- | ------------------- | ----------------- |
| Connection  | Required            | Not required      |
| Reliability | Guaranteed delivery | Best effort       |
| Order       | Preserved           | Not guaranteed    |
| Use case    | Web, file transfer  | Streaming, gaming |

## Resources

- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- [Computer Networks course materials](https://github.com/1995parham-teaching/computer-networks)
- [Computer Networking: A Top-Down Approach](https://www.pearson.com/en-us/subject-catalog/p/computer-networking-a-top-down-approach/P200000013385)

## Releases

The built version of the lecture can be accessed from the [releases](https://github.com/1995parham-teaching/socket.py/releases) section. Each release belongs to a specific semester.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
