import os
import pty
import time
import threading
import subprocess
import multiprocessing

cmd = 'python3 /home/hanqihua/bcc/tools/opensnoop.py'
master, slave = pty.openpty()
p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                        stdout=slave, stderr=subprocess.STDOUT)
while True:
    output = os.read(master, 128).decode('utf-8')
    if output == '':
        break
    outputList = output[:-2].split()
    if (len(outputList) == 5 and outputList[0].isdigit()):
        temp = ' '.join(outputList)
        print(temp)
        time.sleep(2)