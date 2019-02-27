import socket
import termcolor

PORT = 8080
IP = "212.128.253.89"
MAX_OPEN_REQUEST = 5


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("Message from the client: ")
    termcolor.cprint(msg, 'blue')

    if msg == "EXIT":
        cs.close()
        return False

    else:
        # Sending the  message back to the client (because we are a server)
        cs.send(str.encode(msg))
        cs.close()
        return True


# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

variable = True

while variable:

    print("Waiting for connections at : {}, {}".format(IP,PORT))
    (clientsocket, address) = serversocket.accept()

    # -- Process the client request
    print("Attending client; {}".format(address))

    if not process_client(clientsocket):
        variable = False

    # Close the socket
    clientsocket.close()
