import http.server
import socketserver
import termcolor

PORT = 8009


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- Printing the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/" or self.path == "/echo":
            f = open("main-ex-1.html", 'r')
            contents = f.read()

        else:
            file = open("error-ex-1.html", 'r')
            contents = file.read()

        path = self.path
        i = path.find('=')
        if i != -1:
            msg = path[i+1:]
            file = open("msg-ex-1.html")
            contents = file.read()
            contents = contents.replace("msg", msg)

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
