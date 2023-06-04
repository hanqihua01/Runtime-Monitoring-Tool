import os
import pty
import time
import pymysql
import subprocess

os.setuid(0)

db = pymysql.connect(
    host='localhost', user='root', password='123', database='graduate-design')
cursor = db.cursor()

# 线程创建
cmd = 'python3 /home/hanqihua/bcc/tools/threadsnoop.py'
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
        pid = outputList[1]
        comm = outputList[2]
        func = outputList[3]
        sqlStr = "INSERT INTO threadSnoop (curTime, pid, comm, func) VALUES (%s, %s, %s, %s);"
        data = (curTime, pid, comm, func)
        cursor.execute(sqlStr, data)
        db.commit()
        time.sleep(5)

cursor.close()
db.close()
