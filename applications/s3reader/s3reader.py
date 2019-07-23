import os

import boto3
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ForkingMixIn


class Handlr(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            try:
                s3 = boto3.resource('s3')
                obj = s3.Object(os.environ['bucket'], "{}.json".format(os.environ['SANDBOX_ID']))
                body = obj.get()['Body'].read().decode("UTF-8").strip()

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                self.wfile.write(body.encode())
                return
            except Exception as ex:
                self.send_error(500, str(ex))
                return
        else:
            self.send_error(404)
            return


class ForkingHTTPServer(ForkingMixIn, HTTPServer):
    def finish_request(self, request, client_address):
        request.settimeout(30)
        HTTPServer.finish_request(self, request, client_address)

    def handle_error(self, request, client_address):
        pass


if __name__ == '__main__':
    print("Server started")
    server = ForkingHTTPServer(('0.0.0.0', 3000), Handlr)
    try:
        server.serve_forever()
    except:
        server.socket.close()
