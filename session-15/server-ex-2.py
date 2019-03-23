import http.server
import socketserver
import termcolor

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- Printing the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/" or self.path == "/echo":
            f = open("main-ex-2.html", 'r')
            contents = f.read()

        else:
            file = open("error-ex-1.html", 'r')
            contents = file.read()

        if self.path.find("=") != -1:
            if self.path.find("&") != -1:
                i2 = self.path.find("&")
                msg = self.path[self.path.find("=") + 1:i2]
                msg = msg.replace("+", " ")
                msg = msg.upper()
            else:
                msg = self.path[self.path.find("=") + 1:]

            file = open("msg-ex-2.html", "r")
            contents = file.read()
            contents = contents.replace('msg', msg)

        # 200 means that everything is okay
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
