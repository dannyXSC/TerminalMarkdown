from Command.Command import Command
from Document.SimpleMarkdownDoc import SimpleMarkdownDoc


class OpenCommand(Command):
    def __init__(self, app, name):
        super().__init__()
        self._app = app
        self._name = name

    def Execute(self):
        doc = self._app.GetDoc(self._name)
        if doc is None:
            doc = self._app.CreateDocument(self._name)
            self._app.AddDocument(doc)
            doc.Open()
        self._app.ActivateDoc(doc)

    def Undo(self):
        raise Exception
        pass

    def Undoable(self):
        return False

    def Skipable(self):
        return False


class SaveCommand(Command):
    def __init__(self, app):
        super().__init__()
        self._app = app

    def Execute(self):
        doc = self._app.GetCurrentDoc()
        doc.Save()

    def Undo(self):
        raise Exception
        pass

    def Undoable(self):
        return False

    def Skipable(self):
        return False


class InsertRowCommand(Command):
    def __init__(self, doc: SimpleMarkdownDoc, row_num, text):
        super().__init__()
        self._doc = doc
        self._row_num = row_num
        self._text = text

    def Execute(self):
        self._doc.InsertRow(self._row_num - 1, self._text)

    def Undo(self):
        self._doc.DeleteRow(self._row_num - 1)


class InsertHeadCommand(Command):
    def __init__(self, doc: SimpleMarkdownDoc, text):
        super().__init__()
        self._doc = doc
        self._text = text

    def Execute(self):
        self._doc.InsertRow(0, self._text)

    def Undo(self):
        self._doc.DeleteRow(0)


class InsertTailCommand(Command):
    def __init__(self, doc: SimpleMarkdownDoc, text):
        super().__init__()
        self._doc = doc
        self._text = text

    def Execute(self):
        self._doc.InsertRow(len(self._doc.GetLines()), self._text)

    def Undo(self):
        self._doc.DeleteRow(len(self._doc.GetLines()) - 1)


class ListCommand(Command):
    def __init__(self, doc: SimpleMarkdownDoc):
        super().__init__()
        self._doc = doc

    def Execute(self):
        lines = self._doc.GetLines()
        for line in lines:
            print(line, end="")

    def Undo(self):
        pass

    def Undoable(self):
        return False

    def Skipable(self):
        return True
