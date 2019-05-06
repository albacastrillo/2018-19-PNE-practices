import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8000


def operations(msg):
    msg = msg.split("&")
    seq = Seq(msg.pop(0).split("=")[-1].upper())
    actions = {}
    bases = "ACTG"

    # Check if the bases are correct
    if not all(base in bases for base in seq.strbase):
        actions = "ERROR"
        return actions

    actions.update({"Sequence": seq.strbase})

    # Doing all the operations
    base = ""
    for request in msg:
        print(request)
        if "base" in request:
            base += request[-1]
        elif "count" in request:
            action = seq.count(base)
            actions.update({"Number of " + base + " ": action})
        elif "perc" in request:
            action = seq.perc(base)
            actions.update({"Percentage of " + base + " ": action})
        elif request == "chk=on":
            action = seq.len()
            actions.update({"Length": action})
    return actions


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # -- printing the request  line
        termcolor.cprint(self.requestline, "green")
        demand = self.requestline.split()[1]
        print(demand)
        progresses = demand.split("?")[-1]
        print(progresses)

        if self.path.startswith("/seq"):
            test = operations(progresses)
            if test == "ERROR":
                f = open("error-P6.html", 'r')
                contents = f.read()
                f.close()
            else:
                result = ""
                for key, value in test.items():
                    result += "<p>" + key + " : " + str(value) + "</p>"

                contents = """<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>Results obtained</title>
                            </head>
                            <body>
                             <h1>Result of operations</h1>
                              {}
                              <a href="/">Main page</a>
                            </body>
                            </html>""".format(result)

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
        self.wfile.write(str.encode(contents))


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {} ".format(PORT))
    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.server_close()

print("Server stopped")
