# Programming our first client
import socket

# Create a socket  for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

PORT = 8080
IP = "212.128.253.85"

s.connect((IP, PORT))

s.send(str.encode("Hello from my client"))

msg = s.recv(2048).decode("utf-8")
# Máximo de caracteres que puedes recivir del sevidor: 2048

print("Message from the server:")
print(msg)

s.close()

print("The end")

