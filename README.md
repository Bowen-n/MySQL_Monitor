# MySQL Monitor in Python

:smile:This is my project for ***IS214:Database Theory*** in SJTU. I develop a **log monitor** and **status monitor** for **MySQL** Database with python. For log monitor, I referred to repo [MySQLMonitor](https://github.com/TheKingOfDuck/MySQLMonitor). Based on that, I added a status monitor to this project.

## Preparation
1. Install [MySQL](https://www.mysql.com/). A guideline for installing can be found [here](http://www.runoob.com/mysql/mysql-install.html?tdsourcetag=s_pctim_aiomsg).

2. Install PyMySQL using <code>pip install pymysql</code> in your terminal. If you install pymysql successfully, you can run *pymysql_demo.py* to take a peek of pymysql. Don't forget to change the parameters in line 3 and SQL command in line 11.


## How to Use
1. Open file *config.ini* . Usually you only need to change **passward** and **db_name** to your own in this file.

2. Run *main_logmonitor.py* to start **Log Monitor**. It can monitor the commands used by all users of the database in real time. The output is shown as follow:

![log monitor](/screenshots/log_monitor.jpg)


3. Run *main_statusmonitor.py* to start **Status Monitor**. It can monitor the status like using tables, threads, connection list of the database in real time. The output is shown as follow:

![status monitor](/screenshots/status_monitor.jpg)

## TODO
:triangular_flag_on_post: I'll add the structure of my code later 


### Hope you have fun :relaxed:
