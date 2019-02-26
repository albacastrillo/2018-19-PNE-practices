import socket
from Seq import Seq

while True:

    # SERVER IP, PORT
    IP = "212.128.253.108"
    PORT = 8089

    # The client is not blocking the server anymore
    sequence = input("Introduce a sequence: ")
    seq1 = Seq(sequence)
    seq2 = Seq(seq1.complement())
    seq3 = Seq(seq2.reverse())

    bases = "A", "C", "G", "T"
    sequences = seq1, seq2, seq3
    num_seq = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode("The complement reverse of the sequence {} is: {}".format(seq1.strbase, seq3.strbase)))

    # Receive the servers response
    response = s.recv(2048).decode("utf-8")

    # Print the server's response
    print("Message from the server: {}".format(response))

    s.close()
