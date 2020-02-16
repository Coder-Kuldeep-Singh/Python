"""
1. Create a socket
2. Bind the socket to a particular port number
3. Listen for client
4. Accept the connection
5. communicate
6. Close the active connection
7.Close the server socket
"""
# import the socket module
import socket
server_socket = socket.socket()
port_number = 1234
server_socket.bind(("", port_number))
print("Server is bound to port number", port_number)

server_socket.listen()
print("Server is Listening for clients")

conn, addr = server_socket.accept()
print("Hey got a client from address", addr)
data = conn.recv(1000)
print(data.decode())
conn.sendall("Hey from server".encode())
conn.close()
server_socket.close()
