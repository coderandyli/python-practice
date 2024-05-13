# 面向对象
import abc


# 类
class Document():

    # 构造函数：会被自动调用
    def __init__(self, title, author, context):
        print("初始化函数")
        self.title = title
        self.author = author
        self.__context = context  # 私有属性，__表示私有属性

    # 内容长度
    def get_context_length(self):
        return len(self.__context)

    # 内容截取
    def intercept_contex(self, length):
        self.__context = self.__context[0:length]
        return self.__context

# 类2
class Document2():
    WELCOME_STR = "欢迎，本书的内容为{}."

    def __init__(self, title, author, context):
        print("调用初始函数!")
        self.title = title
        self.author = author
        self.__context = context  # 私有属性

    # 类函数:实现不同的 init 构造函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context="nothing")

    # 成员函数
    def get_context_length(self):
        return len(self.__context)

    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document2.WELCOME_STR.format(context)


# 类的继承
class Entity():
    def __init__(self, object_type):
        print("父类构造函数")
        self.object_type = object_type

    def get_contex_length(self):
        raise Exception("没有定义get_context_length")

    def print_title(self):
        print(self.title)

class Document3():
    def __init__(self, title, author, context):
        Entity.__init__(self, "document")
        print("调用初始函数!")
        self.title = title
        self.author = author
        self.__context = context  # 私有属性

    def get_context_length(self):
        return len(self.__context)


class Video(Entity):
    def __init__(self, title, author, video_length):
        Entity.__init__(self, "video")
        print("video调用初始函数!")
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length


# 抽象函数和抽象类
from abc import abstractmethod, ABCMeta

class Entity2(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self):
        pass

class Document4(Entity2):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title





if __name__ =="__main__":
    d1 = Document("Python是世界上最好的语言", "lzz", "Python是世界上最好的语言, 不接受任何辩驳。Python是世界上最好的语言, 不接受任何辩驳。Python是世界上最好的语言, 不接受任何辩驳。Python是世界上最好的语言, 不接受任何辩驳。Python是世界上最好的语言, 不接受任何辩驳。")
    print(d1.title)
    print(d1.author)
    print(d1.get_context_length())
    print(d1.intercept_contex(20))

    empty_book = Document2.create_empty_book("aaaaa", "bbbbb")
    print(empty_book.get_context_length())
    print(empty_book.get_welcome("indeed nothing"))

    # 类继承
    hp_book = Document3("a", "aa", "aaa")
    hp_movie = Video("b", "bb", 30)

    print(hp_book.object_type)
    print(hp_movie.object_type)

    print(hp_book.get_context_length())
    print(hp_movie.get_context_length())

    # 抽象类
    document = Document4()
    document.set_title("hp")
    print(document.get_title())

