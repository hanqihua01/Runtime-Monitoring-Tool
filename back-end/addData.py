import os
import time
import pymysql
import subprocess

class MyHandler():
    '''
    FIXME 定时执行Nagios和eBPF命令并将得到的系统数据存入数据库
    '''
    def __init__(self) -> None:
        self.db = pymysql.connect(host='localhost', user='root', password='123', database='graduate-design')
        self.cursor = self.db.cursor()
    def __del__(self) -> None:
        self.cursor.close()
        self.db.close()

    # 进程计数
    def processCount(self):
        cmdStr = "/usr/local/nagios/libexec/check_procs -w 250 -c 400"
        processNum = subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True).stdout.readline().split()[2].decode()
        curTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(curTime + ": Executing processCount(): ", end='')
        # 将获得的数据插入数据库
        sqlStr = "INSERT INTO processCount (processNum, curTime) VALUES (%s, %s);"
        data = (processNum, curTime)
        self.cursor.execute(sqlStr, data)
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")
        
    # cpu负载
    def cpuPercentage(self):
        cmdStr = "/usr/local/nagios/libexec/check_procs -w 250 -c 400 -m CPU"
        percentageNum = str(float(subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True).stdout.readline().decode().split('=')[4][:-2]) / 10)
        curTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(curTime + ": Executing cpuPercentage(): ", end='')
        # 将获得的数据插入数据库
        sqlStr = "INSERT INTO cpuPercentage (percentageNum, curTime) VALUES (%s, %s);"
        data = (percentageNum, curTime)
        self.cursor.execute(sqlStr, data)
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")

    # 常驻存储大小
    def residentMemorySize(self):
        cmdStr = "/usr/local/nagios/libexec/check_procs -w 250 -c 400 -m RSS"
        sizeNum = subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True).stdout.readline().decode().split('=')[4][:-2]
        curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(curTime + ": Executing residentMemorySize(): ", end='')
        sqlStr = "INSERT INTO residentMemorySize (sizeNum, curTime) VALUES (%s, %s);"
        data = (sizeNum, curTime)
        self.cursor.execute(sqlStr, data)
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")

    # 虚拟内存大小
    def virtualMemorySize(self):
        cmdStr = "/usr/local/nagios/libexec/check_procs -w 250 -c 400 -m VSZ"
        sizeNum = subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True).stdout.readline().decode().split('=')[4][:-2]
        curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(curTime + ": Executing virtualMemorySize(): ", end='')
        sqlStr = "INSERT INTO virtualMemorySize (sizeNum, curTime) VALUES (%s, %s);"
        data = (sizeNum, curTime)
        self.cursor.execute(sqlStr, data)
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")

    # James状态
    def jamesStatus(self):
        cmdStr = '/home/hanqihua/james-server-app-3.6.2-app/james-server-app-3.6.2/bin/james status'
        stdout = subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True).stdout.readline().decode()
        status = stdout.split()[7]
        port = stdout.split()[8][1:-2]
        if (status == 'not'):
            port = '-1'
        curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(curTime + ": Executing jamesStatus(): ", end='')
        sqlStr = "INSERT INTO jamesStatus (status, port, curTime) VALUES (%s, %s, %s);"
        data = (status, port, curTime)
        self.cursor.execute(sqlStr, data)
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")

    # SMTP状态
    def smtpStatus(self):
        cmdStr = '/usr/local/nagios/libexec/check_smtp -H localhost -p 25'
        stdout = subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True).stdout.readline().decode()
        status = stdout.split()[1]
        resTime = stdout.split()[3]
        if (status != 'OK'):
            status = 'CRITICAL'
            resTime = '0.000'
        curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(curTime + ": Executing smtpStatus(): ", end='')
        sqlStr = "INSERT INTO smtpStatus (status, resTime, curTime) VALUES (%s, %s, %s);"
        data = (status, resTime, curTime)
        self.cursor.execute(sqlStr, data)
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")

    # POP状态
    def popStatus(self):
        cmdStr = '/usr/local/nagios/libexec/check_pop -H localhost -p 110'
        stdout = subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True).stdout.readline().decode()
        status = stdout.split()[1]
        resTime = stdout.split()[3]
        if (status != 'OK'):
            status = 'CRITICAL'
            resTime = '0.000'
        curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(curTime + ": Executing popStatus(): ", end='')
        sqlStr = "INSERT INTO popStatus (status, resTime, curTime) VALUES (%s, %s, %s);"
        data = (status, resTime, curTime)
        self.cursor.execute(sqlStr, data)
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")

    # IMAP状态
    def imapStatus(self):
        cmdStr = '/usr/local/nagios/libexec/check_imap -H localhost -p 143'
        stdout = subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True).stdout.readline().decode()
        status = stdout.split()[1]
        resTime = stdout.split()[3]
        if (status != 'OK'):
            status = 'CRITICAL'
            resTime = '0.000'
        curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(curTime + ": Executing imapStatus(): ", end='')
        sqlStr = "INSERT INTO imapStatus (status, resTime, curTime) VALUES (%s, %s, %s);"
        data = (status, resTime, curTime)
        self.cursor.execute(sqlStr, data)
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")

if __name__ == '__main__':
    os.setuid(0)
    myHandler = MyHandler()
    while(True):
        myHandler.processCount()
        myHandler.cpuPercentage()
        myHandler.residentMemorySize()
        myHandler.virtualMemorySize()
        myHandler.jamesStatus()
        myHandler.smtpStatus()
        myHandler.popStatus()
        myHandler.imapStatus()
        time.sleep(5)
        