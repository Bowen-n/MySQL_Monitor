import configparser
import os
import re
import subprocess
import sys
import time

import pymysql

from monitor import logMonitor
from utils import execSQL, getConfig


def main():
    # global db
    db = getConfig()
    data = execSQL(db, "SELECT VERSION()")
    print(time.strftime('[%H:%M:%S]') + "当前数据库版本为: %s " % data)
    time.sleep(1)
    data = execSQL(db, "show variables like '%general_log%';")[1]
    print(time.strftime('[%H:%M:%S]') + '日志状态为:' + data)
    if data == "OFF":
        try:
            print(time.strftime('[%H:%M:%S]') + '正在尝试开启日志模式...')
            time.sleep(1)
            try:
                # logPath = r'D:\\github\\MySQL_Monitor\\'
                logPath = os.getcwd()
                #print(logPath)
                global log
                logName = str(time.strftime('[%Y_%m_%d]')) + "_log.txt"
                log = logPath + "/" + logName
                log = log.replace("\\", "/")  # for windows not support to use \ in log file path
                data = execSQL(db, "set global general_log_file='" + log + "';")
            except:
                pass

            data = execSQL(db, "set global general_log=on;")
            data = execSQL(db, "show variables like '%general_log%';")[1]
            if data == "ON":
                print(time.strftime('[%H:%M:%S]') + '日志模式已开启...')
                print(time.strftime('[%H:%M:%S]') + '日志监听中...')
                log = str(execSQL(db, "show variables like 'general_log_file';")[-1])
                logMonitor(log)
        except:
            print(time.strftime('[%H:%M:%S]') + '日志模式开启失败...')
            print(time.strftime('[%H:%M:%S]' + '未知错误 请联系https://github.com/TheKingOfDuck/MySQLMonitor/issues反馈问题...:'))
            exit()
    else:
        print(time.strftime('[%H:%M:%S]') + '日志监听中...')
    log = str(execSQL(db, "show variables like 'general_log_file';")[-1])
    db.close()
    logMonitor(log)


if __name__ == '__main__':
    main()
