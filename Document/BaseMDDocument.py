import abc
from Document.Document import Document
from typing import List

from Markdown.Item import Item


class BaseMDDocument(Document):
    def __init__(self, name):
        super(BaseMDDocument, self).__init__(name)

    @abc.abstractmethod
    def GetMDItems(self):
        pass

    def NewRow(self):

    @abc.abstractmethod
    def Save(self):
        pass

    @abc.abstractmethod
    def Serialize(self):
        # 解析文件
        # 文件的解析工作由子类完成
        pass
