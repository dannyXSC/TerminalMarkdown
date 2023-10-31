import abc
from Document.Document import Document
from typing import List

from Markdown.Item import Item
from Viewer.Viewer import BaseViewer


class BaseMDDocument(Document):
    def __init__(self, name):
        super(BaseMDDocument, self).__init__(name)
        self.interpreter = self.CreateInterpreter()
        self.viewer_list: List[BaseViewer] = []

    def AttachViewer(self, viewer):
        self.viewer_list.append(viewer)

    def DetachViewer(self, viewer):
        idx = None
        for index, v in enumerate(self.viewer_list):
            if v == viewer:
                idx = index
        if idx is not None:
            self.viewer_list = self.viewer_list[:idx] + self.viewer_list[idx + 1:]

    def Notify(self):
        for viewer in self.viewer_list:
            viewer.Update(self)

    @abc.abstractmethod
    def CreateInterpreter(self):
        pass

    @abc.abstractmethod
    def GetRawStr(self) -> str:
        pass

    @abc.abstractmethod
    def GetLines(self) -> List[str]:
        pass

    @abc.abstractmethod
    def NewRow(self, row_num):
        pass

    @abc.abstractmethod
    def UpdateRow(self, row_num, text):
        pass

    @abc.abstractmethod
    def DeleteRow(self, row_num):
        pass

    @abc.abstractmethod
    def GetRowByContent(self, text):
        pass

    @abc.abstractmethod
    def Save(self):
        pass

    @abc.abstractmethod
    def Serialize(self):
        # 解析文件
        # 文件的解析工作由子类完成
        pass
