#!/usr/bin/python3 

# ---------------------------------------------------------------------
# GPPing - Graphical Port Ping
# Autor: Roland Ortner
# Date:  2024-10-10
# ---------------------------------------------------------------------

import socket
import time
from datetime import datetime

ip = "192.168.178.99"
port = 80 # port e.g. 80, 3232, 6053
naptime = 1 # timeout in sec

class colors:
    OPEN = '\033[92m'
    CLOSED = '\033[91m'
    ENDC = '\033[0m'

# SparkBraille ⣠⣸⣰⣄⣷⣿⣾⣰⣀⣄⣶⣧⣰⣧⣷⣀⣾⣷⣀⣆
class chars:
    OPEN = '⣿' # '█' 
    CLOSED = '⣀' # '_'

# Counters
i = 0
open = 0
closed = 0

print(f"Pinging {ip}:{port} with timeout {naptime} sec...")
print(f"HH:MM\tConnection Status{' '*39}Availability")
now = datetime.now()
print(now.strftime("%H:%M\t"), end='', flush = True)

while(True):
    i += 1

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(naptime)
    sock.settimeout(naptime)
    
    if sock.connect_ex((ip, port)) == 0:
        sock.close()
        print(colors.OPEN + chars.OPEN + colors.ENDC, end='', flush=True)
        open += 1
    else:
        print(colors.CLOSED + chars.CLOSED + colors.ENDC, end='', flush=True)
        closed += 1
    if (i >= 60):
        now = datetime.now()
        availibility = round(100 * open / (open + closed))
        
        print(f"\t"+'{:>3}%'.format(availibility) + "\n" + now.strftime(f"%H:%M\t"), end='', flush = True)
        i = 0
        open = 0
        closed = 0
            
    time.sleep(naptime)
    