import os
import pty
import time
import pymysql
import subprocess

os.setuid(0)

db = pymysql.connect(
    host='localhost', user='root', password='123', database='graduate-design')
cursor = db.cursor()

cmd = 'python3 /home/hanqihua/bcc/tools/runqslower.py'
master, slave = pty.openpty()
p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                        stdout=slave, stderr=subprocess.STDOUT)
while True:
    output = os.read(master, 1024).decode('utf-8')
    if output == '':
        break
    outputList = output[:-2].split()
    if (0 < len(outputList) and 2 < len(outputList[0]) and outputList[0][2] == ':'):
        curTime = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime())
        comm = outputList[1]
        tid = outputList[2]
        lat = outputList[3]
        data = (curTime, comm, tid, lat)
        sqlStr = "INSERT INTO runQSlower (time, comm, tid, lat) VALUES (%s, %s, %s, %s);"
        cursor.execute(sqlStr, data)
        db.commit()

cursor.close()
db.close()