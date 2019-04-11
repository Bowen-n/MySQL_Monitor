import configparser
import time
import pymysql


def execSQL(db, sql):
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return data
    print(time.strftime('[%H:%M:%S]:  ') + str(data ))


def getConfig():
    conf = configparser.ConfigParser()
    try:
        conf.read("config.ini")
        host = conf.get("dbconf", "host")
        port = int(conf.get("dbconf", "port"))
        user = conf.get("dbconf", "user")
        password = conf.get("dbconf", "password")
        db_name = conf.get("dbconf", "db_name")
        charset = conf.get("dbconf", "charset")
        print(time.strftime('[%H:%M:%S]') + "配置解析成功...")
    except:
        print(time.strftime('[%H:%M:%S]') + "配置解析失败 请检查格式是否正确...")

    try:
        # global db
        db = pymysql.connect(host,user,password,db_name,port=port,charset=charset)
        print(time.strftime('[%H:%M:%S]') + '数据库连接成功...')
        return db

    except:
        print(time.strftime('[%H:%M:%S]') + '数据库连接失败...')
