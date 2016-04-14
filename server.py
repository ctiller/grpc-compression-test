import BaseHTTPServer

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-Type', 'text/html')
    self.send_header('Content-Encoding', 'gzip')
    self.end_headers()
    with open('test.gz') as inp:
      self.wfile.write(inp.read())

BaseHTTPServer.HTTPServer(('localhost', 8080), Handler).serve_forever()

