import socket
from Seq import Seq

while True:

    # SERVER IP, PORT
    IP = "212.128.253.88"
    PORT = 8080

    # The client is not blocking the server anymore
    sequence = input("Introduce a sequence: ")
    msg = Seq(sequence).reverse().complement()
    #message = msg.str

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print("The complement of the sequence is: {}".format(response))

    s.close()
