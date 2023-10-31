import abc
import os


class Document(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self._name = name

    def GetName(self):
        return self._name

    def Open(self):
        # 进行打开一切文件都需要做的操作
        # 检查是否存在，不存在创建
        if not os.path.isfile(self._name):
            # 创建
            with open(self._name, 'w') as f:
                # 假如需要预处理文件，则还需要设置一个 Template method
                pass
        self.Serialize()

    @abc.abstractmethod
    def Save(self):
        pass

    @abc.abstractmethod
    def Serialize(self):
        # 解析文件
        # 文件的解析工作由子类完成
        pass
