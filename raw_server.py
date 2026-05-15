import socket

HOST = "127.0.0.1"
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"listening on http://{HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    request_data = client_socket.recv(1024).decode("utf-8")
    print(request_data)

