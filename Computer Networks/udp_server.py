import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("UDP Server is ready...")

# Receive and respond
data, addr = server_socket.recvfrom(1024)
print(f"Client: {data.decode()}")
server_socket.sendto("Hello from Server!".encode(), addr)
