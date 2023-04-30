import os
import time
import pymysql
import subprocess

os.setuid(0)

db = pymysql.connect(
    host='localhost', user='root', password='123', database='graduate-design')
cursor = db.cursor()

# 被动TCP连接
command = 'python3 /home/hanqihua/bcc/tools/tcpaccept.py'
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
while True:
    output = process.stdout.readline().decode()
    if output == '' and process.poll() is not None:
        break
    if output:
        output = output[:-2]
        outputList = output.split()
        if (outputList[0].isdigit()):
            curTime = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime())
            pid = outputList[0]
            comm = ' '.join(outputList[1:-5])
            ip = outputList[-5]
            raddr = outputList[-4]
            rport = outputList[-3]
            laddr = outputList[-2]
            lport = outputList[-1]
            sqlStr = "INSERT INTO passiveTCP (curTime, pid, comm, ip, raddr, rport, laddr, lport) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            data = (curTime, pid, comm, ip, raddr, rport, laddr, lport)
            cursor.execute(sqlStr, data)
            db.commit()

cursor.close()
db.close()