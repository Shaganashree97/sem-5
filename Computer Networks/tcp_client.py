import socket

# Create a TCP socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Send and receive
client_socket.send("Hello from Client!".encode())
data = client_socket.recv(1024).decode()
print(f"Server: {data}")

client_socket.close()
