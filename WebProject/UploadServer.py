import http.server
import socketserver
import os
import cgi

PORT = 8000

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        if self.path == '/upload':
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            if ctype == 'multipart/form-data':
                fs = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST'})
                fileitem = fs['file']
                if fileitem.file:
                    filename = os.path.join(os.getcwd(), fileitem.filename)
                    with open(filename, 'wb') as f:
                        while True:
                            chunk = fileitem.file.read(100000)
                            if not chunk:
                                break
                            f.write(chunk)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'File uploaded successfully')
                    return

        # If not a POST request to /upload, serve the form instead
        self.send_response(200)
        self.end_headers()
        html = '''
        <html>
            <head>
                <title>File Upload</title>
            </head>
            <body>
                <h1>File Upload</h1>
                <form method="post" action="/upload" enctype="multipart/form-data">
                    <label for="file">Select a file to upload:</label>
                    <input type="file" name="file" id="file">
                    <br>
                    <button type="submit">Upload</button>
                </form>
            </body>
        </html>
        '''
        self.wfile.write(html.encode('utf-8'))

handler = MyRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)

print(f"Serving at http://localhost:{PORT}")
httpd.serve_forever()
