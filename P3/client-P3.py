import socket

# SERVER PORT, IP
PORT = 8000
IP = "192.168.56.1"

# Message from the client
msg = """ACTG
len
"""

# Create a socket  for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish the connection to the server
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode(msg))

# Receive the servers response
response = s.recv(2048).decode("utf-8")
print("Message from the server:")
print(response)

s.close()

