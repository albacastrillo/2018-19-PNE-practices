import socket

while True:
    # Create a socket  for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # SERVER IP, PORT
    PORT = 8089
    IP = "212.128.253.108"

    # The client is not blocking the server anymore
    sequence = input("Introduce a sequence: ")

    # Establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(sequence))

    # Receive the servers response
    msg = s.recv(2048).decode("utf-8")

    # Print the server's response
    print("Message from the server: {}".format(msg))

    s.close()
