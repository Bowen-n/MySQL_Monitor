import time
import os
import re
import subprocess

prefix = ''


def logMonitor(log, db):

    command = 'tail -f ' + log
    print("command: {}".format(command))
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    status_monitor = statusMonitor(db)
    try:
        while True:
            
            '''
            status_monitor.show_open_table()
            status_monitor.show_thread()
            status_monitor.show_all_connections()
            '''
            
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


class statusMonitor():

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

        self.staMonitor_SQLdict = {
            'open table': "show global status like 'open%tables%'",
            'thread': "show global status like 'Thread%'",
            'all connections': "show processlist",
            # threads_connected 当前建立的连接
        }


    def show_open_table(self):
        # cursor = self.db.cursor()
        self.db.ping(reconnect=True)
        self.cursor.execute(self.staMonitor_SQLdict['open table'])
        data = self.cursor.fetchall()
        open_tables = data[0][1]
        opened_tables = data[1][1]
        print('Open tables: {}'.format(open_tables))
        print('Opened tables: {}'.format(opened_tables))

    
    def show_thread(self):
        # cursor = self.db.cursor()
        self.db.ping(reconnect=True)
        self.cursor.execute(self.staMonitor_SQLdict['thread'])
        data = self.cursor.fetchall()
        threads_connected = data[1][1]
        threads_running = data[3][1]
        print('Threads connected: {}'.format(threads_connected))
        print('Threads running: {}'.format(threads_running))


    def show_all_connections(self):
        # cursor = self.db.cursor()
        self.db.ping(reconnect=True)
        self.cursor.execute(self.staMonitor_SQLdict['all connections'])
        data = self.cursor.fetchall()
        print('Id       User       Host        Database        Command       Time     Info')
        for user in data:
            for _ in range(8):
                if _ != 6: # don't print State
                    print(str(user[_]) + '    ')