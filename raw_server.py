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
    
    request_data = client_socket.recv(1024).decode("utf-8")
    
    request_line = request_data.split("\r\n")[0]

    method, path, _ = request_line.split(" ")
    
    if method == "GET" and path == "/posts":
        body = '[{"id": 1, "body": "hello from chirper!"}]'
        status = "200 OK"
    elif method == "GET" and path == "/health":
        body = '{"status": "ok"}'
        status = "200 OK"
    else:
        body = '{"error": "not found"}'
        status = "404 Not Found"
    
    response = (
        f"HTTP/1.1 {status}\r\n"
        f"Content-Type: application/json\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"\r\n"
        f"{body}"
    )

    client_socket.sendall(response.encode("utf-8"))
    client_socket.close()

    
    

