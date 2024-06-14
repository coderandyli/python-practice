# 29 | 巧用上下文管理器和With语句精简代码
'''
    - 上下文管理器，能够帮助你自动分配并且释放资源，其中最典型的应用便是 with 语句
    - 有两种上下文管理器，1. 基于类的上下文管理器更加 flexible，适用于大型的系统开发；2. 而基于生成器的上下文管理器更加方便、简洁，适用于中小型程序。
'''


# 基于类的上下文管理器
class FileManager:
    def __init__(self, name, mode):
        print("__init__")
        self.name = name
        self.mode = mode

    def __enter__(self):
        print("enter")
        self.file = open(self.name, self.mode)
        return self.file

    # 方法“__exit__()”中的参数“exc_type, exc_val, exc_tb”，分别表示 exception_type、exception_value 和 traceback。当我们执行含有上下文管理器的 with 语句时，如果有异常抛出，异常的信息就会包含在这三个变量中，传入方法“__exit__()”。
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        if self.file:
            self.file.close()


from contextlib import contextmanager


@contextmanager
def file_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()





if __name__ == "__main__":
    # for i in range(10000):
    #     with open("test.txt", "w") as f:
    #         f.write("hello")

    with FileManager("text.txt", "w") as f:
        print("准备写文件")
        f.write("hello 2")

    with file_manager('test1.txt', 'w') as f:
        f.write('hello world')


''' 数据库连接-上下文管理器
class DBConnectionManager: 
    def __init__(self, hostname, port): 
        self.hostname = hostname 
        self.port = port 
        self.connection = None
  
    def __enter__(self): 
        self.connection = DBClient(self.hostname, self.port) 
        return self
  
    def __exit__(self, exc_type, exc_val, exc_tb): 
        self.connection.close() 
  
with DBConnectionManager('localhost', '8080') as db_client: 
'''