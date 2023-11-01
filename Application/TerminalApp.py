import abc

from Application.Application import Application
from Command.DerivedCommand import InsertRowCommand, InsertHeadCommand, InsertTailCommand, ListCommand
from Document.SimpleMarkdownDoc import SimpleMarkdownDoc
from Viewer.PygameViewer import PygameViewer
from Viewer.TerminalViewer import TerminalViewer


class TerminalApp(Application):
    def __init__(self, cmd_capacity=50):
        super().__init__(cmd_capacity)

    def CreateDocument(self, name):
        # 创建本应用支持的文件
        doc = SimpleMarkdownDoc(name)
        doc.AttachViewer(PygameViewer(name))
        doc.AttachViewer(TerminalViewer(name))
        return doc

    def InsertRow(self, row_num, text):
        self._cmdManager.Execute(InsertRowCommand(self._activateDoc, row_num, text))

    def InsertHead(self, text):
        self._cmdManager.Execute(InsertHeadCommand(self._activateDoc, text))

    def InsertTail(self, text):
        self._cmdManager.Execute(InsertTailCommand(self._activateDoc, text))

    def List(self):
        self._cmdManager.Execute(ListCommand(self._activateDoc))

    def Run(self):
        while True:
            user_input = input(r"请输入命令[q\Q退出]: ")
            if user_input == 'q' or user_input == 'Q':
                break
            handler = LoadHandler()
            handler = SaveHandler(handler)
            handler = InsertHandler(handler)
            handler = AppendHeadHandler(handler)
            handler = AppendTailHandler(handler)
            handler = UndoHandler(handler)
            handler = RedoHandler(handler)
            handler = ListHandler(handler)
            state = handler.HandleRequest(user_input, self)
            if state:
                self._activateDoc.Notify()


class BaseHandler(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self._successor: BaseHandler = successor

    @abc.abstractmethod
    def HandleRequest(self, user_input, context: TerminalApp) -> bool:
        pass


class LoadHandler(BaseHandler):
    def HandleRequest(self, user_input, context: TerminalApp) -> bool:
        input_list = user_input.split()
        command = input_list[0]
        if command == 'load':
            argument = ' '.join(input_list[1:])
            context.Open(argument)
            return True
        elif self._successor:
            return self._successor.HandleRequest(user_input, context)
        else:
            return False


class SaveHandler(BaseHandler):
    def HandleRequest(self, user_input, context: TerminalApp) -> bool:
        input_list = user_input.split()
        command = input_list[0]
        if command == 'save':
            context.Save()
            return True
        elif self._successor:
            return self._successor.HandleRequest(user_input, context)
        else:
            return False


class InsertHandler(BaseHandler):
    def HandleRequest(self, user_input, context: TerminalApp) -> bool:
        input_list = user_input.split()
        command = input_list[0]
        if command == 'insert':
            if input_list[1].isdigit():
                row_num = int(input_list[1])
                argument = ' '.join(input_list[2:])
                context.InsertRow(row_num, argument)
            else:
                argument = ' '.join(input_list[1:])
                context.InsertTail(argument)
            return True
        elif self._successor:
            return self._successor.HandleRequest(user_input, context)
        else:
            return False


class AppendHeadHandler(BaseHandler):
    def HandleRequest(self, user_input, context: TerminalApp) -> bool:
        input_list = user_input.split()
        command = input_list[0]
        if command == 'append-head':
            argument = ' '.join(input_list[1:])
            context.InsertHead(argument)
            return True
        elif self._successor:
            return self._successor.HandleRequest(user_input, context)
        else:
            return False


class AppendTailHandler(BaseHandler):
    def HandleRequest(self, user_input, context: TerminalApp) -> bool:
        input_list = user_input.split()
        command = input_list[0]
        if command == 'append-tail':
            argument = ' '.join(input_list[1:])
            context.InsertTail(argument)
            return True
        elif self._successor:
            return self._successor.HandleRequest(user_input, context)
        else:
            return False


class UndoHandler(BaseHandler):
    def HandleRequest(self, user_input, context: TerminalApp) -> bool:
        input_list = user_input.split()
        command = input_list[0]
        if command == 'undo':
            context.Undo()
            return True
        elif self._successor:
            return self._successor.HandleRequest(user_input, context)
        else:
            return False


class RedoHandler(BaseHandler):
    def HandleRequest(self, user_input, context: TerminalApp) -> bool:
        input_list = user_input.split()
        command = input_list[0]
        if command == 'redo':
            context.Redo()
            return True
        elif self._successor:
            return self._successor.HandleRequest(user_input, context)
        else:
            return False


class ListHandler(BaseHandler):
    def HandleRequest(self, user_input, context: TerminalApp) -> bool:
        input_list = user_input.split()
        command = input_list[0]
        if command == 'list':
            context.List()
            return True
        elif self._successor:
            return self._successor.HandleRequest(user_input, context)
        else:
            return False
