import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is waiting for a connection...")

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

# Receive and respond
data = conn.recv(1024).decode()
print(f"Client: {data}")
conn.send("Hello from Server!".encode())

conn.close()
server_socket.close()
