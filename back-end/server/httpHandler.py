import os
import mtl
import json
import pymysql
from http.server import BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    # 处理跨域问题
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.end_headers()

    def do_GET(self):
        db = pymysql.connect(host="localhost", user="root", password="123", database="graduate-design")
        cursor = db.cursor()

        # CPU负载，无历史信息
        if self.path == '/CpuLoad':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            cmdStr = '/usr/local/nagios/libexec/check_load -w 0.3,0.5,0.7 -c 0.5,0.7,0.9'
            output = os.popen(cmdStr).read()[:-2]
            output = output.split('|')[0].split(':')[-1]
            self.wfile.write(output.encode())
            self.wfile.flush()

        # 进程计数
        elif self.path == '/ProcessCount':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT processNum, curTime FROM processCount ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # cpu负载
        elif self.path == '/cpuPercentage':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT percentageNum, curTime FROM cpuPercentage ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # 常驻内存大小
        elif self.path == '/ResidentMemorySize':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT sizeNum, curTime FROM residentMemorySize ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # 虚拟内存大小
        elif self.path == '/VirtualMemorySize':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT sizeNum, curTime FROM virtualMemorySize ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # James状态
        elif self.path == '/jamesStatus':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT status, port, curTime FROM jamesStatus ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # SMTP状态
        elif self.path == '/smtpStatus':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT status, resTime, curTime FROM smtpStatus ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # POP状态
        elif self.path == '/popStatus':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT status, resTime, curTime FROM popStatus ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # IMAP状态
        elif self.path == '/imapStatus':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT status, resTime, curTime FROM imapStatus ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # 系统信息
        elif self.path == '/systemInfo':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cmdStr = 'neofetch'
            ret = os.popen(cmdStr)
            retList = ret.readlines()
            ret.close()
            output = ""
            for i in range(22, 26):
                tempList = retList[i].split()[1:-1]
                tempList.append(retList[i].split()[-1][0:-4])
                tempStr = ' '.join(tempList)
                output += tempStr + '|'
            for i in range(29, 32):
                tempList = retList[i].split()[1:-1]
                tempList.append(retList[i].split()[-1][0:-4])
                tempStr = ' '.join(tempList)
                output += tempStr + '|'
            self.wfile.write(output.encode())
            self.wfile.flush()
        
        # 磁盘使用
        elif self.path == '/diskUsage':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cmdStr = 'df -h'
            ret = os.popen(cmdStr)
            retList = ret.readlines()
            ret.close()
            output = ""
            for i in range(1, len(retList)):
                output += retList[i][0:-1] + '|'
            self.wfile.write(output.encode())
            self.wfile.flush()

        # 主动TCP连接
        elif self.path == '/activeTCP':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT curTime, pid, comm, ip, saddr, daddr, port FROM activeTCP ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # 被动TCP连接
        elif self.path == '/passiveTCP':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT curTime, pid, comm, ip, raddr, rport, laddr, lport FROM passiveTCP ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # TCP断开连接
        elif self.path == '/tcpClose':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT curTime, pid, comm, ip, saddr, daddr, sport, dport FROM tcpClose ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # 线程创建
        elif self.path == '/threadSnoop':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT curTime, pid, comm, func FROM threadSnoop ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # TCP连接延迟
        elif self.path == '/tcpConnLat':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT curTime, pid, comm, ip, saddr, daddr, dport, lat FROM tcpConnLat ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # TCP传输数据大小建立连接时长
        elif self.path == '/tcpLife':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT curTime, pid, comm, laddr, lport, raddr, rport, tx, rx, ms FROM tcpLife ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # CPU调度延迟
        elif self.path == '/runQSlower':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            cursor.execute("SELECT time, comm, tid, lat FROM runQSlower ORDER BY time DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # 每秒新创建进程
        elif self.path == '/pidPerSec':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            cursor.execute("SELECT time, num FROM pidPerSec ORDER BY time DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        # 打开的文件
        elif self.path == '/openSnoop':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            cursor.execute("SELECT curTime, pid, comm, fd, err, path FROM openSnoop ORDER BY curTime DESC LIMIT 10;")
            data = cursor.fetchall()
            self.wfile.write(json.dumps(data).encode())
            self.wfile.flush()

        cursor.close()
        db.close()

    def do_POST(self):
        db = pymysql.connect(host="localhost", user="root", password="123", database="graduate-design")
        cursor = db.cursor()

        if self.path == '/mtlPidPerSec':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            mtlSpecific = json.loads(post_data)["mtl"]

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            cursor.execute("SELECT num FROM pidPerSec ORDER BY time DESC LIMIT 10;")
            numList = list(cursor.fetchall())[::-1]
            aList = []
            for i in range(len(numList)):
                if (int(numList[i][0]) > 5): # 每秒新建进程数量大于5为True
                    aList.append((i, True))
                else:
                    aList.append((i, False))
            data = {
                'newProcs': aList,
            }
            # 在整个时间轴上，如果某个时刻新建进程数量大于5，那么在接下来的2个时间点，新建进程数量不能都大于5
            try:
                phi = mtl.parse(mtlSpecific)
                data = str(phi(data, quantitative=False))
            except:
                data = "Wrong"
            self.wfile.write(data.encode())
            self.wfile.flush()

        if self.path == '/mtlCpuPercentage':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            mtlSpecific = json.loads(post_data)["mtl"]

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            cursor.execute("SELECT percentageNum FROM cpuPercentage ORDER BY curTime DESC LIMIT 10;")
            numList = list(cursor.fetchall())[::-1] # 按时间正序排列
            aList = []
            for i in range(len(numList)):
                if (float(numList[i][0]) > 0.6):
                    aList.append((i, True))
                else:
                    aList.append((i, False))
            data = {
                'cpuLoad': aList,
            }
            try:
                phi = mtl.parse(mtlSpecific)
                data = str(phi(data, quantitative=False))
            except:
                data = "Wrong"
            self.wfile.write(data.encode())
            self.wfile.flush()

        cursor.close()
        db.close()