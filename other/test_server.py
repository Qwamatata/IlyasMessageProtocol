import socket
from src.IlyasMessageProtocol import protocol

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind(('127.0.0.1', 6252))

socket_server.listen()

client = socket_server.accept()

client_socket = client[0]
client_address = client[1]

picture = open('C:\\Users\\User\\PycharmProjects\\space_cat\\pill_red.png', 'rb')
data = picture.read()

protocol.send(client_socket, data, 'PIC', filename='pill_red.png')

client_socket.close()
socket_server.close()
