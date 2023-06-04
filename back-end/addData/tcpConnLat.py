import os
import pty
import time
import pymysql
import subprocess

os.setuid(0)

db = pymysql.connect(
    host='localhost', user='root', password='123', database='graduate-design')
cursor = db.cursor()

# TCP连接延迟
cmd = 'python3 /home/hanqihua/bcc/tools/tcpconnlat.py'
master, slave = pty.openpty()
p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                        stdout=slave, stderr=subprocess.STDOUT)
while True:
    output = os.read(master, 1024).decode('utf-8')
    if output == '':
        break
    outputList = output[:-2].split()
    if (0 < len(outputList) and outputList[0].isdigit()):
        curTime = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime())
        pid = outputList[0]
        commList = outputList[1:-5]
        if len(commList) <= 2:
            comm = ' '.join(commList)
        else:
            comm = ' '.join(commList[0:2])
        ip = outputList[-5]
        saddr = outputList[-4]
        daddr = outputList[-3]
        dport = outputList[-2]
        lat = outputList[-1]
        data = (curTime, pid, comm, ip, saddr, daddr, dport, lat)
        sqlStr = "INSERT INTO tcpConnLat (curTime, pid, comm, ip, saddr, daddr, dport, lat) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        try:
            cursor.execute(sqlStr, data)
            db.commit()
        except:
            continue

cursor.close()
db.close()