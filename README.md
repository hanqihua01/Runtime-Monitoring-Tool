# Runtime Monitoring Tool
This is a runtime-monitoring tool for distributed systems, using eBPF (especially BCC) and Nagios to collect data, and MTL to conduct runtime verification.

### I need your help! This tool still has some imperfections! Something sometimes goes wrong when executing backend.

# Run backend
1. Open `back-end` folder.
2. Run `sudo python3 server/server.py` to activate the backend server.
3. Run `sudo ./run.sh` to activate data-collecting program, which will create several processes in the background, collecting system data, and store it in MySQL. Just check `ps` to see these processes.

# Run frontend
1. Run `npm run serve` to enter develop mode.
2. Run `npm run build` to build the project.
