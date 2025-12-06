import socket
from src.IlyasMessageProtocol import protocol

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_client.connect(('127.0.0.1', 6252))

print(protocol.receive(socket_client))

socket_client.close()
#len(filename)!= 0 and