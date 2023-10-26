from Application import Application
from DerivedCommand import InsertRowCommand, InsertHeadCommand, InsertTailCommand, ListCommand
from SimpleMarkdownDoc import SimpleMarkdownDoc


class TerminalApp(Application):
    def __init__(self, cmd_capacity=50):
        super().__init__(cmd_capacity)

    def CreateDocument(self, name):
        # 创建本应用支持的文件
        return SimpleMarkdownDoc(name)

    def InsertRow(self, row_num, text):
        self._cmdManager.Execute(InsertRowCommand(self._activateDoc, row_num, text))

    def InsertHead(self, text):
        self._cmdManager.Execute(InsertHeadCommand(self._activateDoc, text))

    def InsertTail(self,text):
        self._cmdManager.Execute(InsertTailCommand(self._activateDoc, text))

    def List(self):
        self._cmdManager.Execute(ListCommand(self._activateDoc))
