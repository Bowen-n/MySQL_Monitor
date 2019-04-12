import configparser
import os
import re
import subprocess
import sys
import time
from tkinter import *

import pymysql

from monitor import statusMonitor
from utils import execSQL, getConfig


def main():
    # global db
    db = getConfig()

    data = execSQL(db, "SELECT VERSION()") 
    print(time.strftime('[%H:%M:%S]') + "The version of database: %s " % data)
    time.sleep(1)
    
    st_m = statusMonitor(db)

    while True:
        print('TABLES')
        print('-' * 20)
        st_m.show_open_table()
        print('\n\nTHREADS')
        print('-' * 20)
        st_m.show_thread()
        print('\n\nCONNECTIONS')
        st_m.show_all_connections()
        time.sleep(1)
        os.system('cls')


if __name__ == '__main__':
    main()
