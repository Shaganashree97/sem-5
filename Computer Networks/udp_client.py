import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)

# Send and receive
client_socket.sendto("Hello from Client!".encode(), server_address)
data, _ = client_socket.recvfrom(1024)
print(f"Server: {data.decode()}")

client_socket.close()
