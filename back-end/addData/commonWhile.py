import os
import time
import pymysql

os.setuid(0)

db = pymysql.connect(
    host='localhost', user='root', password='123', database='graduate-design')
cursor = db.cursor()

# 进程计数
def processCount():
    cmdStr = "/usr/local/nagios/libexec/check_procs -w 250 -c 400"
    processNum = os.popen(cmdStr).readline().split()[2]
    curTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    sqlStr = "INSERT INTO processCount (processNum, curTime) VALUES (%s, %s);"
    data = (processNum, curTime)
    cursor.execute(sqlStr, data)
    db.commit()

# cpu负载
def cpuPercentage():
    cmdStr = "/usr/local/nagios/libexec/check_procs -w 250 -c 400 -m CPU"
    percentageNum = str(float(os.popen(cmdStr).readline().split('=')[4][:-2]) / 10)
    curTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    sqlStr = "INSERT INTO cpuPercentage (percentageNum, curTime) VALUES (%s, %s);"
    data = (percentageNum, curTime)
    cursor.execute(sqlStr, data)
    db.commit()

# 常驻存储大小
def residentMemorySize():
    cmdStr = "/usr/local/nagios/libexec/check_procs -w 250 -c 400 -m RSS"
    sizeNum = os.popen(cmdStr).readline().split('=')[4][:-2]
    curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    sqlStr = "INSERT INTO residentMemorySize (sizeNum, curTime) VALUES (%s, %s);"
    data = (sizeNum, curTime)
    cursor.execute(sqlStr, data)
    db.commit()

# 虚拟内存大小
def virtualMemorySize():
    cmdStr = "/usr/local/nagios/libexec/check_procs -w 250 -c 400 -m VSZ"
    sizeNum = os.popen(cmdStr).readline().split('=')[4][:-2]
    curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    sqlStr = "INSERT INTO virtualMemorySize (sizeNum, curTime) VALUES (%s, %s);"
    data = (sizeNum, curTime)
    cursor.execute(sqlStr, data)
    db.commit()

# James状态
def jamesStatus():
    cmdStr = '/home/hanqihua/james-server-app-3.6.2-app/james-server-app-3.6.2/bin/james status'
    stdout = os.popen(cmdStr).readline()
    status = stdout.split()[7]
    port = stdout.split()[8][1:-2]
    if (status == 'not'):
        port = '-1'
    curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    sqlStr = "INSERT INTO jamesStatus (status, port, curTime) VALUES (%s, %s, %s);"
    data = (status, port, curTime)
    cursor.execute(sqlStr, data)
    db.commit()

# SMTP状态
def smtpStatus():
    cmdStr = '/usr/local/nagios/libexec/check_smtp -H localhost -p 25'
    stdout = os.popen(cmdStr).readline()
    status = stdout.split()[1]
    resTime = stdout.split()[3]
    if (status != 'OK'):
        status = 'CRITICAL'
        resTime = '0.000'
    curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    sqlStr = "INSERT INTO smtpStatus (status, resTime, curTime) VALUES (%s, %s, %s);"
    data = (status, resTime, curTime)
    cursor.execute(sqlStr, data)
    db.commit()

# POP状态
def popStatus():
    cmdStr = '/usr/local/nagios/libexec/check_pop -H localhost -p 110'
    stdout = os.popen(cmdStr).readline()
    status = stdout.split()[1]
    resTime = stdout.split()[3]
    if (status != 'OK'):
        status = 'CRITICAL'
        resTime = '0.000'
    curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    sqlStr = "INSERT INTO popStatus (status, resTime, curTime) VALUES (%s, %s, %s);"
    data = (status, resTime, curTime)
    cursor.execute(sqlStr, data)
    db.commit()

# IMAP状态
def imapStatus():
    cmdStr = '/usr/local/nagios/libexec/check_imap -H localhost -p 143'
    stdout = os.popen(cmdStr).readline()
    status = stdout.split()[1]
    resTime = stdout.split()[3]
    if (status != 'OK'):
        status = 'CRITICAL'
        resTime = '0.000'
    curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    sqlStr = "INSERT INTO imapStatus (status, resTime, curTime) VALUES (%s, %s, %s);"
    data = (status, resTime, curTime)
    cursor.execute(sqlStr, data)
    db.commit()


while (True):
    processCount()
    cpuPercentage()
    residentMemorySize()
    virtualMemorySize()
    jamesStatus()
    smtpStatus()
    popStatus()
    imapStatus()
    time.sleep(60)

cursor.close()
db.close()