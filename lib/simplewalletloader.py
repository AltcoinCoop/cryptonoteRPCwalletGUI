import os
import time
import subprocess
from sys import platform


def simplewalletloader(walletname, walletpw, isname):
    """Function to create and/or open wallet in simplewallet rpc mode"""
    # Launch simplewallet in rpc mode if wallet file exists
    if isname == True:
        # os.remove(walletname)
        print "***Opening ___" + walletname + "___ wallet file rpc interface***"
        if platform == 'win32':
            subprocess.Popen(
                "start myntnote-wallet-rpc.exe --wallet-file {0} --password {1} --rpc-bind-port 24000 --set_log 0\r\nnpause".format(
                    walletname, walletpw), shell=True)
        elif platform == 'linux' or platform == 'linux2' or platform == 'darwin':
            subprocess.Popen(
                'xterm -bg black -hold -e "./myntnote-wallet-rpc --wallet-file {0} --password {1} --rpc-bind-port 24000"'.format(
                    walletname, walletpw))

    # Generate and then launch if wallet file doesn't exist
    elif isname == False:
        print "Generating wallet file " + walletname
        if platform == 'win32':
            walletgen = subprocess.Popen(
                "myntnote-wallet-rpc.exe --generate-new-wallet {0} --password {1} --rpc-bind-port 24000 --set_log 0".format(
                    walletname, walletpw), shell=True, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        elif platform == 'linux' or platform == 'linux2' or platform == 'darwin':
            walletgen = subprocess.Popen(
                "./myntnote-wallet-rpc --generate-new-wallet {0} --password {1} --rpc-bind-port 24000 --set_log 0".format(
                walletname, walletpw), shell=True, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print "Wallet gen'ed"
        time.sleep(5)
        #print walletgen.stdout.read()
        #print walletgen.communicate('exit')
        walletgen.terminate()
        if platform == 'win32':
            os.system("taskkill /im simplewallet.exe /f")
        elif platform == 'linux' or platform == 'linux2' or platform == 'darwin':
            p = subprocess.Popen("pgrep simplewallet", shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
            output, errors = p.communicate()
            output = output.split('\n')
            for i in output:
                os.system("kill -9 {0}".format(i))
        # Launch simplewallet in rpc mode now that wallet file exists
        print "***Opening ___" + walletname + "___ wallet file rpc interface***"
        if platform == 'win32':
            subprocess.Popen(
                "start myntnote-wallet-rpc.exe --wallet-file {0} --password {1} --rpc-bind-port 24000 --set_log 0\r\nnpause".format(
                    walletname, walletpw), shell=True)
        elif platform == 'linux' or platform == 'linux2' or platform == 'linux32':
            subprocess.Popen(
                'xterm -bg black -hold -e "./myntnote-wallet-rpc --wallet-file {0} --password {1} --rpc-bind-port 24000 --set_log 0"'.format(
                    walletname, walletpw), shell=True)


    elif isname == None:
        pass
