import os, http.server, socketserver
"""
Creates HTTP server on the local computer.
The HTTP server contains the Pictures directory and its sub-directories.
"""

class PictureHTTPServer:
    #initializing the class
    #os.path.join(os.path.expanduser("~"), "Pictures") return the picture directory of the logged user on all OS
    def __init__(self, port=8888):
        self.directory = os.path.join(os.path.expanduser("~"), "Pictures")
        self.port = port
        self.http_server_handler = http.server.SimpleHTTPRequestHandler

    def get_directory(self):
        return self.directory
    def get_port(self):
        return self.port


    def start_server(self):
        """
        Starts the HTTP server on the local computer.
        """
        try:
            # changing the directory to Pictures
            os.chdir(self.directory)
            # starts the server
            with socketserver.TCPServer(("", self.port), self.http_server_handler) as HTTPServer:
                HTTPServer.serve_forever()
        except Exception as e:
            raise RuntimeError(f"HTTP Server failed: {e}")
