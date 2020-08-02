# echo_server.py
# https://www.bogotobogo.com/python/python_network_programming_server_client.php
#
# author    Raul Aguilar
# date      July 19, 2020
#
# CS 138 Homework 13 Project 2: Server
# Modify the server to send back the string in reverse order.
#
# Algorithm:
# 1. Create address and port
# 2. Create (server) socket and assign address and port to it
# 3. Listen for connection from client. Store new client socket and
# client address (hostaddr, port). Display connected message
# 4. While there is data (sentence) to recieve, store data, reverse it,
# send it back to client, display data that was recieved
# 5. Close the connection
#
import socket

host = ''
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    reverseMessage = data[::-1]
    if not data:
        break
    conn.sendall(reverseMessage)
    print('Received', repr(data))

conn.close()