import socket

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)  # Use the IP and port you want
server_socket.bind(server_address)
server_socket.listen(1)  # Listen for one incoming connection

print("Server is waiting for a connection...")
client_socket, client_address = server_socket.accept()
print("Client connected from:", client_address)

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("Received:", data.decode())
    # Here, you can process the data and send back a "pong" response
    response = "pong"
    client_socket.send(response.encode())

client_socket.close()
server_socket.close()