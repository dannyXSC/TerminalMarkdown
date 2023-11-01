from Command import Command
from SimpleMarkdownDoc import SimpleMarkdownDoc

def print_array_as_tree(arr):
    stack = []
    last_star_level = None  # 用于记录最后一个*项的层级

    for item in arr:
        # 动态计算层级
        level = 0
        while item.startswith('#'):
            level += 1
            item = item[1:]

        item = item.strip()

        if level == 0 and item.startswith('* '):
            if last_star_level is not None:
                level = last_star_level  # 如果之前已经有*项，使用同一层级
            else:
                level = (stack[-1] + 1) if stack else 1  # 否则，设置为最后一个#项的子项

            last_star_level = level  # 记录这个*项的层级
            item = item[2:]
        else:
            last_star_level = None  # 如果不是*项，重置最后一个*项的层级

        if level == 0:
            continue  # 如果层级仍为0，则跳过这一项

        # 保持当前层级的元素
        stack = stack[:level]

        # 计算缩进
        indent = '    ' * (level - 1)

        # 判断是否是新的层级还是同一层级的另一个元素
        if stack and stack[-1] == level:
            print(indent + '├── ' + item)
        else:
            print(indent + '└── ' + item)
        stack.append(level)  # 只有当level不为0时，才添加到stack里


class ListTreeCommand(Command):
    def __init__(self, doc: SimpleMarkdownDoc):
        super().__init__()
        self._doc = doc

    def Execute(self):
        lines = self._doc.GetLines()
        new_lines = []
        for line in lines:
            new_line = line[:-1]
            new_lines.append(new_line)
        print(new_lines)
        print_array_as_tree(new_lines)

    def Undo(self):
        raise Exception
        pass


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


class DeleteRowCommand(Command):
    def __init__(self, doc: SimpleMarkdownDoc, row_num):
        super().__init__()
        self._doc = doc
        self._row_num = row_num
        self._text = doc.GetLines()[row_num-1]

    def Execute(self):
        self._doc.DeleteRow(self._row_num - 1)

    def Undo(self):
        self._doc.InsertRow(self._row_num - 1, self._text)


class DeleteTextCommand(Command):
    def __init__(self, doc: SimpleMarkdownDoc, text):
        super().__init__()
        self._doc = doc
        self._row_num = doc.GetRowByContent(text) + 1
        self._text = text

    def Execute(self):
        self._doc.DeleteRow(self._row_num - 1)

    def Undo(self):
        self._doc.InsertRow(self._row_num - 1, self._text)


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


class HistoryCommand(Command):
    def __init__(self, log_list, log_num):
        super().__init__()
        self.log_list = log_list[-log_num:]
        self.log_num = log_num

    def Execute(self):
        for log in self.log_list:
            print(log, end="")

    def Undo(self):
        pass

    def Undoable(self):
        return False

    def Skipable(self):
        return True
