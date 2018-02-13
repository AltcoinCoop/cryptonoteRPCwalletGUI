import subprocess
from sys import platform
import os

def bitmonerodloader():
    """Start bitmonerod and/or simplewallet and collect wallet name and address"""
    print "Start daemon button pressed..."
    #Start bitmonerod daemon if not running
    if platform == 'win32':
        daemonproc = subprocess.Popen("start myntd.exe --log-level 0",
                                      shell=True)
    elif platform == 'linux' or platform == 'linux2' or platform == 'linux32':
        # print "linux!"
        daemonproc = subprocess.Popen('xterm -bg black -e "./myntd --log-level 0"',
                                      shell=True)

