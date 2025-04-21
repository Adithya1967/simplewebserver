from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
    <head>
        <title>TCP/IP Protocol Suite</title>
    </head>
    <body>
        <center>
            <table border="1" cellpadding="10" bgcolor="lightblue">
                <caption><h2>Protocol List</h2></caption>
                <tr>
                    <th>S.No</th><th>Layer</th><th>Protocols</th>
                </tr>
                <tr>
                    <td>1</td><td>Application Layer</td><td>HTTP, FTP, SSH, TELNET, DNS</td>
                </tr>
                <tr>
                    <td>2</td><td>Transport Layer</td><td>TCP, UDP</td>
                </tr>
                <tr>
                    <td>3</td><td>Internet Layer</td><td>IP, ICMP</td>
                </tr>
                <tr>
                    <td>4</td><td>Link Layer</td><td>MAC, Wi-Fi</td>
                </tr>
            </table>
        </center>
    </body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running on http://localhost:8000 ...")
httpd.serve_forever()