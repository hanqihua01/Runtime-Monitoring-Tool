#!/bin/bash

# gnome-terminal --command="python3 ./server.py" &
# gnome-terminal --command="python3 ./addData/commonWhile.py" &
# gnome-terminal --command="python3 ./addData/activeTCP.py" &
# gnome-terminal --command="python3 ./addData/passiveTCP.py" &
# gnome-terminal --command="python3 ./addData/threadSnoop.py" &
# gnome-terminal --command="python3 ./addData/tcpClose.py" &
# gnome-terminal --command="python3 ./addData/tcpConnLat.py" &
# gnome-terminal --command="python3 ./addData/tcpLife.py" &
# gnome-terminal --command="python3 ./addData/runQSlower.py" &
# gnome-terminal --command="python3 ./addData/pidPerSec.py" &
# gnome-terminal --command="python3 ./addData/openSnoop.py" &

gnome-terminal --tab --title="python3 ./server.py" -e "python3 ./server.py" &
gnome-terminal --tab --title="python3 ./addData/commonWhile.py" -e "python3 ./addData/commonWhile.py" &
gnome-terminal --tab --title="python3 ./addData/activeTCP.py" -e "python3 ./addData/activeTCP.py" &
gnome-terminal --tab --title="python3 ./addData/passiveTCP.py" -e "python3 ./addData/passiveTCP.py" &
gnome-terminal --tab --title="python3 ./addData/threadSnoop.py" -e "python3 ./addData/threadSnoop.py" &
gnome-terminal --tab --title="python3 ./addData/tcpClose.py" -e "python3 ./addData/tcpClose.py" &
gnome-terminal --tab --title="python3 ./addData/tcpConnLat.py" -e "python3 ./addData/tcpConnLat.py" &
gnome-terminal --tab --title="python3 ./addData/tcpLife.py" -e "python3 ./addData/tcpLife.py" &
gnome-terminal --tab --title="python3 ./addData/runQSlower.py" -e "python3 ./addData/runQSlower.py" &
gnome-terminal --tab --title="python3 ./addData/pidPerSec.py" -e "python3 ./addData/pidPerSec.py" &
gnome-terminal --tab --title="python3 ./addData/openSnoop.py" -e "python3 ./addData/openSnoop.py" &