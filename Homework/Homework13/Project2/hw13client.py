# echo_client.py
# https://www.bogotobogo.com/python/python_network_programming_server_client.php
#
# author    Raul Aguilar
# date      July 19, 2020
#
# CS 138 Homework 13 Project 2: Server
# Modify the server to send back the string in reverse order.
#
# Algorithm:
# 1. Get server info
# 2. Create client socket and connect to server
# 3. Get user input
# 4. Decode string into bytes and send data to server
# 5. Get data (reversed string) from server
# 6. Close the connection and display the data received
#
import socket

# Server info
host = socket.gethostname()
port = 12345

# connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# get user string
message = input("Send a sentence to the server: ")
s.sendall(message.encode('UTF-8'))

data = s.recv(1024)
s.close()
print('Received', repr(data))