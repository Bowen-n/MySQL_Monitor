import time
import os
import re
import subprocess

prefix = ''


def logMonitor(log):
    '''
    try:
        print(time.strftime('[%H:%M:%S]') + '为兼容MySQL 8.0.X 监控需使用root权限...')
        command = 'sudo tail -f ' + log
        popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    except:
        # command = 'tail -f D:\github\MySQLMonitor\[2019_04_11]_log.txt'
        command = 'tail -f ' + log  #for windows
        print("{}".format(log))
        popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    '''

    print(time.strftime('[%H:%M:%S]') + '为兼容MySQL 8.0.X 监控需使用root权限...')
    command = 'tail -f ' + log
    print("command: {}".format(command))
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    try:
        while True:
            line = popen.stdout.readline().strip()
            encodeStr = bytes.decode(line)
            pattern = re.findall('Query\s*(.*)', encodeStr, re.S)
            if len(pattern) != 0:
                selectStr = pattern[0]
                if selectStr != "COMMIT":
                    joinTime = time.strftime("[%H:%M:%S]", time.localtime())
                    if prefix != "":
                        reg = re.findall(r'\b' + prefix + '\w*', encodeStr, re.S)
                        if len(reg) != 0:
                            table = '操作的表:' + reg[0]
                            joinTime += table
                    print(joinTime + selectStr)

    except KeyboardInterrupt:
        pass