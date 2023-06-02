# cliente.py
import socket
import json
from app import App

# create a socket object
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get a local machine name
# IP server
host = '127.0.0.1'
# Server PORT
port = 9999

# connection to hostname on the port
cliente_socket.connect((host, port))

# create a App object
client_app = App()

# collecting user data
values = client_app.collect_user_data()

# processing user data
list_data = client_app.validate_data(values)
final_data = client_app.generate_dict(list_data)

# serialising data
# pass the data to json
data = json.dumps(final_data)

# pass to bytes
data = data.encode("ascii")

# send data to server
cliente_socket.send(data)

# recive no more than 1024 bytes
# pass to json
response = cliente_socket.recv(1024).decode()

# pass to dict
response = json.loads(response)

# menu
client_app.menu(response)

# close connection
cliente_socket.close()
