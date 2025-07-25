# server.py
import socket
import threading

from globals import Globals
from jsonGen import jsonGen
from util.singelton import SingletonMeta


class Server(metaclass=SingletonMeta):
    host = "10.10.0.41"
    port = 65432
    reset_flag = False
    def __init__(self, host=None, port=None):
        if host:
            self.host = host
        if port:
            self.port = port
    def sendDataToClient(self, server_socket):
        print("Sending data to client")
        while Globals.run and not self.reset_flag:
            try:
                data = jsonGen().getJson()
                print("sending data to client:", data)
                server_socket.sendall(data.encode())
            except socket.error as e:
                print(f"Socket error: {e}")
                self.reset_flag = True
    def recvDataFromClient(self, server_socket):
        print("Receiving data from client")
        while Globals.run and not self.reset_flag:
            try:
                data = server_socket.recv(8096)
                if not data:
                    print("No data received from client, resetting connection.")
                    self.reset_flag = True
                    return
                jsonGen().updateClasses(data.decode())
                print("Received from client:", data.decode())
            except socket.error as e:
                print(f"Socket error: {e}")
                self.reset_flag = True
    def run(self):
        while Globals.run:
            Globals.run = True
            self.reset_flag = False
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.bind((self.host, self.port))
                server_socket.listen()

                print(f"Server listening on {self.host}:{self.port}...")
                conn, addr = server_socket.accept()
                print(f"Connected by {addr}")

                threading.Thread(target=lambda: self.sendDataToClient(conn), daemon=True).start()
                threading.Thread(target=lambda: self.recvDataFromClient(conn), daemon=True).start()
                # conn.sendall(jsonGen().getJson().encode())  # Echo back to client
                while Globals.run and not self.reset_flag:
                    pass
                # while True:
                    # try:
                    #     # data = conn.recv(1024)
                    #     # jsonGen().updateClasses(data.decode())
                    #     # print("Received from client:", data.decode())
                    #     # conn.sendall(jsonGen().getJson().encode())  # Echo back to client
                    # except Exception as e:
                    #     print("Error receiving data:", e)
                    #     break
            print(Globals.run, self.reset_flag)
            print(f"Error starting server on {self.host}:{self.port}, retrying...")


