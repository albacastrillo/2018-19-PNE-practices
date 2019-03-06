import socket

# SERVER PORT, IP
PORT = 8000
IP = "212.128.253.87"

# Message from the client
msg = """ACGT
countG
countT
percentageA
reverse
complement
"""

# Create a socket  for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish the connection to the server
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode("msg"))

# Receive the servers response
response = s.recv(2048).decode("utf-8")
print("Message from the server:")
print(response)

s.close()

