import http.server
import ssl

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = http.server.HTTPServer(('localhost', PORT), Handler)

# 使用自定义的证书和密钥文件
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='server.pem', server_side=True)

print(f"Serving HTTPS on port {PORT}")
httpd.serve_forever()
