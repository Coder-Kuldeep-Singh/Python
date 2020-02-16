"""
1. Create a socket (which consists of both ip address and port number)
2. Connect the socket to a server socket
3. Communicate
4. Close the socket
"""
# import the socket module
import socket
client_socket = socket.socket()
port_number = 1234
client_socket.connect(("", port_number))
client_socket.sendall("Hi server. I am a client".encode())
data = client_socket.recv(1000)
print(data.decode())
client_socket.close()
