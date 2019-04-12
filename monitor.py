import time
import os
import re
import subprocess

prefix = ''


def logMonitor(log, db):

    command = 'tail -f ' + log
    # print("command: {}".format(command))
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    status_monitor = statusMonitor(db)
    try:
        while True:
            
            line = popen.stdout.readline().strip()
            encodeStr = bytes.decode(line)
            pattern_query = re.findall('Query\s*(.*)', encodeStr, re.S)
            if len(pattern_query) != 0:
                select_query = pattern_query[0]
                select_query = 'operation: ' + select_query

                pattern_id = re.findall('Z\s*(\d*)', encodeStr, re.S)
                select_id = pattern_id[0]
                select_id = 'id: ' + select_id

                joinTime = time.strftime("[%H:%M:%S]", time.localtime())

                print(joinTime + '   ' + select_id + '     ' + select_query)

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
        print('-' * 110)
        print('%-6s%-20s%-20s%-20s%-12s%-10s%-20s' % ('|Id', '|User', '|Host', '|Database', '|Command', '|Time', '|Info'))
        print('-' * 110)
        for user in data:
            print('%-6s' % ('|' + str(user[0])), end='')
            print('%-20s' % ('|' + str(user[1])), end='')
            print('%-20s' % ('|' + str(user[2])), end='')
            print('%-20s' % ('|' + str(user[3])), end='')
            print('%-12s' % ('|' + str(user[4])), end='')
            print('%-10s' % ('|' + str(user[5])), end='')
            print('%-20s' % ('|' + str(user[6])), end='')
            print()
        print('-' * 110)

