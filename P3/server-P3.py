import socket
from Seq import Seq


PORT = 8000
IP = "192.168.56.1"
MAX_OPEN_REQUEST = 5



def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("Message from the client: {}".format(msg))

    if msg == '\n':
        cs.send(str.encode("ALIVE"))
        cs.close()
        return True

    # Split the request into the commands
    split_msg = msg.split()
#    list_oper = split_msg[1:]
    results = []
    bases = 'A', 'C', 'G', 'T'
    valid = str(bases)
    counter = 0
    operations = 'len', 'complement', 'reverse', 'countA', 'countT', 'countG', 'countC', 'percA', 'percT', 'percG', 'percC'

    for i in split_msg[0].upper():
        if i in str(bases):
            counter += 1
    if len(split_msg[0]) == counter:
        results.append("OK")
    else:
        results.append("ERROR")

    if len(split_msg) > 1:
        for element in split_msg[1:]:
            print(element)
            if element == 'len':
                results.append(str(Seq(split_msg[0]).len()))
            elif element == 'complement':
                results.append(Seq(split_msg[0]).complement())
            elif element == 'reverse':
                results.append(Seq(split_msg[0]).reverse())
            elif 'count' in element:
                bases = element[-1]
                if element[-1] in valid:
                    results.append(str(Seq(split_msg[0]).count(bases)))
                else:
                    cs.send(str.encode("ERROR"))
                    cs.close()
                    return True
            elif 'perc' in element:
                bases = element[-1]
                if element[-1] in str(bases):
                    results.append(str(Seq(split_msg[0]).perc(bases)))
                else:
                    cs.send(str.encode("ERROR"))
                    cs.close()
                    return True
            elif element not in operations:
                cs.send(str.encode("ERROR"))
                cs.close()
                return True

    print(results)
    final_result = "\n".join(results)

    # Send  the message back to the client
    cs.send(str.encode(final_result))
    cs.close()
    return True


# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

ready = True
while ready:

    print("Waiting for connections at : {}, {}".format(IP,PORT))
    (clientsocket, address) = serversocket.accept()

    # Process the client request
    print("Attending client: {}".format(address))

    if not process_client(clientsocket):
        ready = False

    # Close the socket
    clientsocket.close()


