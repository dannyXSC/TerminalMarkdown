import abc

from Command import Command
from CommandManager import CommandManager
from DerivedCommand import OpenCommand, SaveCommand
from Document import Document


class Application(metaclass=abc.ABCMeta):
    # 应用
    def __init__(self, cmd_capacity=50):
        # 文档 list
        self._docList = []
        self._activateDoc = None
        # command管理器
        self._cmdManager = CommandManager(cmd_capacity)

    def AddDocument(self, doc):
        self._docList.append(doc)

    def GetDoc(self, name):
        for doc in self._docList:
            if doc.GetName() == name:
                return doc
        return None

    def ActivateDoc(self, doc):
        for d in self._docList:
            if d.GetName() == doc.GetName():
                self._activateDoc = doc

    def GetCurrentDoc(self) -> Document:
        # 获得当前的文档
        return self._activateDoc

    def Open(self, name):
        self._cmdManager.Execute(OpenCommand(self, name))

    def Save(self):
        self._cmdManager.Execute(SaveCommand(self))

    def Undo(self):
        self._cmdManager.Undo()

    def Redo(self):
        self._cmdManager.Redo()

    @abc.abstractmethod
    def CreateDocument(self, name) -> Document:
        # 创建具体文件的工作由子类完成
        pass
