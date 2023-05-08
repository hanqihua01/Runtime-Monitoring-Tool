#!/bin/bash

# 新建10个终端，分别执行10条命令
# gnome-terminal --tab --title="python3 ./addData/commonWhile.py" -- "python3 ./addData/commonWhile.py" &
# gnome-terminal --tab --title="python3 ./addData/activeTCP.py" -- "python3 ./addData/activeTCP.py" &
# gnome-terminal --tab --title="python3 ./addData/passiveTCP.py" -- "python3 ./addData/passiveTCP.py" &
# gnome-terminal --tab --title="python3 ./addData/threadSnoop.py" -- "python3 ./addData/threadSnoop.py" &
# gnome-terminal --tab --title="python3 ./addData/tcpClose.py" -- "python3 ./addData/tcpClose.py" &
# gnome-terminal --tab --title="python3 ./addData/tcpConnLat.py" -- "python3 ./addData/tcpConnLat.py" &
# gnome-terminal --tab --title="python3 ./addData/tcpLife.py" -- "python3 ./addData/tcpLife.py" &
# gnome-terminal --tab --title="python3 ./addData/runQSlower.py" -- "python3 ./addData/runQSlower.py" &
# gnome-terminal --tab --title="python3 ./addData/pidPerSec.py" -- "python3 ./addData/pidPerSec.py" &
# gnome-terminal --tab --title="python3 ./addData/openSnoop.py" -- "python3 ./addData/openSnoop.py" &

# 在后台新建10个进程，分别执行10条命令
nohup python3 ./addData/commonWhile.py > /dev/null 2>&1 &
nohup python3 ./addData/activeTCP.py > /dev/null 2>&1 &
nohup python3 ./addData/passiveTCP.py > /dev/null 2>&1 &
nohup python3 ./addData/threadSnoop.py > /dev/null 2>&1 &
nohup python3 ./addData/tcpClose.py > /dev/null 2>&1 &
nohup python3 ./addData/tcpConnLat.py > /dev/null 2>&1 &
nohup python3 ./addData/tcpLife.py > /dev/null 2>&1 &
nohup python3 ./addData/runQSlower.py > /dev/null 2>&1 &
nohup python3 ./addData/pidPerSec.py > /dev/null 2>&1 &
nohup python3 ./addData/openSnoop.py > /dev/null 2>&1 &

# python3 ./addData/commonWhile.py
# python3 ./addData/activeTCP.py
# python3 ./addData/passiveTCP.py
# python3 ./addData/threadSnoop.py
# python3 ./addData/tcpClose.py 
# python3 ./addData/tcpConnLat.py
# python3 ./addData/tcpLife.py
# python3 ./addData/runQSlower.py
# python3 ./addData/pidPerSec.py
# python3 ./addData/openSnoop.py