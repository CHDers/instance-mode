'''
🚀🚀🚀🚀🚀🚀: 
Descripttion: Yanjun Hao的代码
version: 1.0.0
Author: Yanjun Hao
Date: 2023-11-26 12:04:46
LastEditors: Yanjun Hao
LastEditTime: 2023-11-26 12:15:30
'''

# LINKING: https://mp.weixin.qq.com/s/3lKL8lO_7sqXImfDWxjSPg


# %%
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
# %%
def my_decorator(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            print("Creating instance of decorated class")
            super().__init__(*args, **kwargs)
    return NewClass
# %%
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class MyClass:
    pass
# %%
import threading

def singleton_threadsafe(cls):
    instances = {}
    lock = threading.Lock()
    
    def get_instance(*args, **kwargs):
        with lock:
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]
    return get_instance
# %%
@singleton
class DatabaseConnection:
    def __init__(self, db_url):
        # 连接到数据库的操作
        self.connection = connect(db_url)

    def query(self, sql):
        # 执行数据库查询的操作
        return self.connection.execute(sql)

# 使用
db_instance = DatabaseConnection('mysql://user:password@localhost/mydatabase')
result = db_instance.query('SELECT * FROM mytable')

# %%
@singleton
class Logger:
    def __init__(self, log_file):
        # 初始化日志记录器的操作
        self.log_file = open(log_file, 'w')

    def log(self, message):
        # 记录日志的操作
        self.log_file.write(message + '\n')

    def close(self):
        # 关闭日志文件的操作
        self.log_file.close()

# 使用
logger_instance = Logger('app_log.txt')
logger_instance.log('An important log message')
logger_instance.close()