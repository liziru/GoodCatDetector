from http.server import BaseHTTPRequestHandler
from urllib import parse
import sys
import os
import time
import picamera

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        with picamera.PiCamera() as camera:
            camera.resolution = (1920, 1080)
            camera.start_preview()
            time.sleep(2)
            camera.capture("foo.jpg")

        full_path = os.getcwd() + "/foo.jpg"
        img = open(full_path, "rb")

        content = img.read()

        self.send_response(200)
        self.send_header('Content-Type', 'image/jpeg')
        self.send_header('Content-Disposition', 'attachment; filename="foo.jpg"')
        self.end_headers()
        self.wfile.write(content)


if __name__ == '__main__':
    from http.server import HTTPServer

    port = 80
    server = HTTPServer(('0.0.0.0', port), GetHandler)
    print("listen on " + str(port))
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
