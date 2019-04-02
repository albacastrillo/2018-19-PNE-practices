import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8009


def doing(msg):
    operations = {}
    msg = msg.split("&")
    seq = msg.pop(0).split("=")[-1].upper()
    bases = 'A', 'C', 'T', 'G'

    # Check if the characters of the sequence are bases
    for base in seq:
        if base not in bases:
            operations = "ERROR"
        return operations

    seq = Seq(seq)

    operations.update({"Sequence": seq.strbase})

    # The function makes all the computations
    base = ""
    for request in msg:
        if "base" in request:
            base += request[-1]
        elif "count" in request:
            operations.update("Number of {}'s: {}".format(base, seq.count(base)))
        elif "perc" in request:
            operations.update("Percentage of {}'s: {}".format(base, seq.perc(base)))
        elif request == "chk=on":
            operations.update("Len: " + seq.len())

    return operations


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # -- printing the request line
        termcolor.cprint(self.requestline, "green")
        request = self.requestline.split()[1]
        process = request.split("?")[-1]

        if self.path.startswith("/seq"):
            test = doing(process)
            if test == "ERROR":
                f = open("error-P6.html", 'r')
                contents = f.read()
                f.close()
            else:
                results = ""
                for key, value in test.items():
                    results += "<p>" + key + " : " + str(value) + "</p>"

                contents = """<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>Obtained results</title>
                            </head>
                            <body>
                             <h1>Results</h1>
                              {}
                              <a href="/">[Main page]</a>
                            </body>
                            </html>""".format(results)

        elif self.path == "/":
            f = open("main-P6.html", 'r')
            contents = f.read()
            f.close()

        else:
            f = open("error-P6.html", 'r')
            contents = f.read()
            f.close()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))


# -- Main programme
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {} ".format(PORT))
    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
