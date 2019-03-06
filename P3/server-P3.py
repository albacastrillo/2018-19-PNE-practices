import socket
from Seq import Seq

PORT = 8000
IP = "212.128.253.87"
MAX_OPEN_REQUEST = 5


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("Message from the client: {}".format(msg))

    # Split the request into the commands
    cmsg = msg.split('\n')

    if cmsg[0] == '':
        cs.send(str.encode("ALIVE"))
        cs.close()

    # Sending the  message back to the client (because we are a server)

    cs.close()


    list_msg = msg[1:]
    results = []
    bases = 'A', 'C', 'G', 'T'
    counter = 0
    errorcounter = 0

    for i in msg[0].upper():
        if i in str(bases):
            counter += 1
        elif i not in str(bases):
            errorcounter += 1

    if len(msg[0].upper()) == counter:
        results.append("OK")

    else:
        results.append("ERROR")

    if len(msg) > 1:
        for element in list_msg:
            print(element)
            if element == 'len':
                results.append(str(seq.len()))
            elif element == 'complement':
                results.append(seq.complement().strbase)
            elif element == 'reverse':
                results.append(seq.reverse(strbase))

            elif 'count' in element:
                bases = element[-1].upper()
                if element[-1].upper() in str(bases):
                    results.append(str(seq.count(bases)))
                else:
                    cs.send(str.encode("ERROR"))
                    cs.close()
                    return True

            elif 'percentage' in element:
                bases = element[-1].upper()
                if element[-1].upper in str(bases):
                    results.append(str(seq.percentage(bases)))
                else:
                    cs.send(str.encode("ERROR"))
                    cs.close()
                    return True

            elif element != Seq:
                cs.send(str.encode("ERROR"))
                cs.close()
                return True

    elif len(msg) == 1:
        if seq.strbase == 'EXIT' or seq.strbase == 'exit':
            print('Closed')
            cs.send(str.encode("Server closed"))
            cs.close()
            return False

    results = "\n".join(results)

    # Send  the message back to the client
    cs.send(str.encode(results))
    cs.close()
    return True


# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting for connections at : {}, {}".format(IP,PORT))
    (clientsocket, address) = serversocket.accept()

    # -- Process the client request
    print("Attending client; {}".format(address))

    if not process_client(clientsocket):
        ready = False

#    process_client(clientsocket)

    # Close the socket
    clientsocket.close()
