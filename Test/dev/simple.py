# encoding=utf-8
import SimpleHTTPServer
import SocketServer

PORT = 7780

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()