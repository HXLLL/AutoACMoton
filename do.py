import sys
import getopt
import time

import auto_ACmoton

try:
    options,args = getopt.getopt(sys.argv[1:], 'hs:t:', ['help', 'start=', 'interval='])
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
    code = a.solve(pid)
    if code != 0:
        print "cant solve problem %d, ErrorCode: %d" % (pid, code)
        pid = pid + 1
        continue
    pid = pid + 1
    for i in range(interval):
        a.sendheartbeat()
        time.sleep(60)
