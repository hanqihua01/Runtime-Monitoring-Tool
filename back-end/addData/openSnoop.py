import os
import pty
import time
import pymysql
import subprocess

db = pymysql.connect(
    host='localhost', user='root', password='123', database='graduate-design')
cursor = db.cursor()

# 打开的文件
cmd = 'python3 /home/hanqihua/bcc/tools/opensnoop.py'
master, slave = pty.openpty()
p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                        stdout=slave, stderr=subprocess.STDOUT)
while True:
    output = os.read(master, 1024).decode('utf-8')
    if output == '':
        break
    outputList = output[:-2].split()
    if (len(outputList) == 5 and outputList[0].isdigit()):
        curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        pid = outputList[0]
        commList = outputList[1:-3]
        comm = ' '.join(commList)
        fd = outputList[-3]
        err = outputList[-2]
        path = outputList[-1]
        data = (curTime, pid, comm, fd, err, path)
        sqlStr = "INSERT INTO openSnoop (curTime, pid, comm, fd, err, path) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(sqlStr, data)
        db.commit()

cursor.close()
db.close()