import sys
import getopt
import time

import auto_ACmoton

start_pid = 1000
interval = 30*60

try:
    options,args = getopt.getopt(sys.argv[1:], 's:t:', ['start=', 'interval='])
except getopt.GetoptError:
    sys.exit()

for option,value in options:
    if option in ('-s', '--start'):
        start_pid = int(value)
    if option in ('-t', '--interval'):
        interval = int(value)

a = auto_ACmoton.AutoACMoton()

pid = start_pid

while True:
    print '==========solving problem %d==========' % pid
    a.solve(pid)
    pid = pid + 1
    time.sleep(interval)
