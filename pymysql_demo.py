import pymysql

db = pymysql.connect('127.0.0.1',      # host
                        'root',        # user
                        '20170612',    # passward
                        'sql_project', # database name
                         port=3306,  
                         charset='utf8')
cursor = db.cursor()

sql_command = 'SELECT * FROM city'
cursor.execute(sql_command)
data = cursor.fetchall()

print('{}'.format(data))


