# server.py
import socket

from jsonGen import jsonGen


class Server:
    host = "10.10.0.41"
    port = 65432
    def __init__(self, host=None, port=None):
        if host:
            self.host = host
        if port:
            self.port = port
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()

            print(f"Server listening on {self.host}:{self.port}...")
            conn, addr = server_socket.accept()
            conn.sendall(jsonGen().getJson().encode())  # Echo back to client
            with conn:
                try:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024)
                        print("Received from client:", data.decode())
                        conn.sendall(jsonGen().getJson().encode())  # Echo back to client
                except Exception as e:
                    self.run()

