import time

from Application import Application
from DerivedCommand import InsertRowCommand, InsertHeadCommand, InsertTailCommand, DeleteRowCommand, DeleteTextCommand, \
    ListCommand, HistoryCommand, ListTreeCommand, DirTreeCommand
from SimpleMarkdownDoc import SimpleMarkdownDoc
from Logger import Logger
from Sessioner import Session


class TerminalApp(Application):
    def __init__(self, cmd_capacity=50):
        super().__init__(cmd_capacity)
        self.logger = Logger()
        self.session = Session()

    def CreateDocument(self, name):
        # 创建本应用支持的文件
        return SimpleMarkdownDoc(name)

    def InsertRow(self, row_num, text):
        self._cmdManager.Execute(InsertRowCommand(self._activateDoc, row_num, text))

    def InsertHead(self, text):
        self._cmdManager.Execute(InsertHeadCommand(self._activateDoc, text))

    def InsertTail(self, text):
        self._cmdManager.Execute(InsertTailCommand(self._activateDoc, text))

    def DeleteRow(self, row_num):
        self._cmdManager.Execute(DeleteRowCommand(self._activateDoc, row_num))

    def DeleteText(self, text):
        self._cmdManager.Execute(DeleteTextCommand(self._activateDoc, text))

    def List(self):
        self._cmdManager.Execute(ListCommand(self._activateDoc))

    def ListTree(self):
        self._cmdManager.Execute(ListTreeCommand(self._activateDoc))

    def DirTree(self, text):
        self._cmdManager.Execute(DirTreeCommand(self._activateDoc, text))

    def History(self, log_list, log_num):
        self._cmdManager.Execute(HistoryCommand(log_list, log_num))

    def Run(self):
        while True:
            user_input = input(r"请输入命令[q\Q退出]: ")
            if user_input == 'q' or user_input == 'Q':
                self.session.quit()
                break
            self.logger.log(user_input)
            input_list = user_input.split()
            command = input_list[0]
            if command == 'load':
                argument = ' '.join(input_list[1:])
                filename = user_input.split(" ")[1]
                self.session.load(filename)
                self.session.current = filename
                self.Open(argument)
            elif command == 'save':
                self.Save()
            elif command == 'insert':
                if input_list[1].isdigit():
                    row_num = int(input_list[1])
                    argument = ' '.join(input_list[2:])
                    self.InsertRow(row_num, argument)
                else:
                    argument = ' '.join(input_list[1:])
                    self.InsertTail(argument)
            elif command == 'append-head':
                argument = ' '.join(input_list[1:])
                self.InsertHead(argument)
            elif command == 'append-tail':
                argument = ' '.join(input_list[1:])
                self.InsertTail(argument)
            elif command == 'delete':
                if input_list[1].isdigit():
                    row_num = int(input_list[1])
                    self.DeleteRow(row_num)
                else:
                    argument = ' '.join(input_list[1:])
                    self.DeleteText(argument)
            elif command == 'undo':
                self.Undo()
            elif command == 'redo':
                self.Redo()
            elif command == 'list':
                self.List()
            elif command == "list-tree":
                self.ListTree()
            elif command == "dir-tree":
                if (len(input_list) == 1):
                    self.DirTree('')
                else:
                    self.DirTree(input_list[1])
            elif command == 'history':
                if user_input == command:
                    self.History(self.logger.get_content(), 0)
                else:
                    self.History(self.logger.get_content(), int(input_list[1]))
            elif command == 'stats':
                command_parts = user_input.split(" ")
                if len(command_parts) == 2:
                    self.session.stats(command_parts[1])
                else:
                    print("Invalid stats command.")

