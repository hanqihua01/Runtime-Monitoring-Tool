import os
from http.server import HTTPServer
from httpHandler import MyHandler

if __name__ == '__main__':
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Starting server on port 3000...')
    # 以 root 用户身份运行服务器
    os.setuid(0)
    httpd.serve_forever()
