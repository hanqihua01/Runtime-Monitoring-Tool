import os
import json
import pymysql
import subprocess
from http.server import BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 连接数据库
        db = pymysql.connect(host="localhost", user="root", password="123", database="graduate-design")
        cursor = db.cursor()

        # CPU负载，无历史信息
        if self.path == '/CpuLoad':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                cmdStr = '/usr/local/nagios/libexec/check_load -w 0.3,0.5,0.7 -c 0.5,0.7,0.9'
                p = subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                output = p.stdout.readline().decode()
                output = output.split('|')[0].split(':')[-1]
                self.wfile.write(output.encode())
                self.wfile.flush()

            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # 进程计数
        elif self.path == '/ProcessCount':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT processNum, curTime FROM processCount ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # cpu负载
        elif self.path == '/cpuPercentage':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT percentageNum, curTime FROM cpuPercentage ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # 常驻内存大小
        elif self.path == '/ResidentMemorySize':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT sizeNum, curTime FROM residentMemorySize ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # 虚拟内存大小
        elif self.path == '/VirtualMemorySize':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT sizeNum, curTime FROM virtualMemorySize ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # James状态
        elif self.path == '/jamesStatus':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT status, port, curTime FROM jamesStatus ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # SMTP状态
        elif self.path == '/smtpStatus':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT status, resTime, curTime FROM smtpStatus ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # POP状态
        elif self.path == '/popStatus':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT status, resTime, curTime FROM popStatus ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # IMAP状态
        elif self.path == '/imapStatus':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT status, resTime, curTime FROM imapStatus ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # 系统信息
        elif self.path == '/systemInfo':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                cmdStr = 'neofetch'
                ret = os.popen(cmdStr)
                retList = ret.readlines()
                ret.close()
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
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
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))
        
        # 磁盘使用
        elif self.path == '/diskUsage':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                cmdStr = 'df -h'
                ret = os.popen(cmdStr)
                retList = ret.readlines()
                ret.close()
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                output = ""
                for i in range(1, len(retList)):
                    output += retList[i][0:-1] + '|'
                self.wfile.write(output.encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # 主动TCP连接
        elif self.path == '/activeTCP':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT curTime, pid, comm, ip, saddr, daddr, port FROM activeTCP ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # 被动TCP连接
        elif self.path == '/passiveTCP':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT curTime, pid, comm, ip, raddr, rport, laddr, lport FROM passiveTCP ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # TCP断开连接
        elif self.path == '/tcpClose':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT curTime, pid, comm, ip, saddr, daddr, sport, dport FROM tcpClose ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # 线程创建
        elif self.path == '/threadSnoop':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT curTime, pid, comm, func FROM threadSnoop ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # TCP连接延迟
        elif self.path == '/tcpConnLat':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT curTime, pid, comm, ip, saddr, daddr, dport, lat FROM tcpConnLat ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # TCP传输数据大小建立连接时长
        elif self.path == '/tcpLife':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT curTime, pid, comm, laddr, lport, raddr, rport, tx, rx, ms FROM tcpLife ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # CPU调度延迟
        elif self.path == '/runQSlower':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT time, comm, tid, lat FROM runQSlower ORDER BY time DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # 每秒新创建进程
        elif self.path == '/pidPerSec':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT time, num FROM pidPerSec ORDER BY time DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        # 打开的文件
        elif self.path == '/openSnoop':
            if os.getuid() != 0:
                self.send_error(401, message='Permission denied')
                return
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                cursor.execute("SELECT curTime, pid, comm, fd, err, path FROM openSnoop ORDER BY curTime DESC LIMIT 20;")
                data = cursor.fetchall()
                self.wfile.write(json.dumps(data).encode())
                self.wfile.flush()
            except subprocess.CalledProcessError as e:
                self.send_error(500, message=str(e))

        cursor.close()
        db.close()
