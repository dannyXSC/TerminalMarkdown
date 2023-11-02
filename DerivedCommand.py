from Command import Command
from SimpleMarkdownDoc import SimpleMarkdownDoc
import re


# 返回层级，标题的level为'#'的数量，文本的level为0
def getLevel(text):
    pattern = r'^(#+)( +)(\S+)'
    # 正则表达匹配标题 一个以上# + 一个以上空格 + 一个以上非空白字符
    result  = re.search( pattern, text, re.M|re.I)
    
    level = 0
    if result: 
        # 说明是标题
        for index in range(len(text)):
            if text[index]=='#':
                level+=1
            else:
                break

    return level

def print_array_as_tree(arr,curDirIndex=None):
    # curDirIndex表示当前目录的index
    # 为None表示打印全部
    
    last_dirLevel = 0  # 用于记录上一个标题的层级
    last_prinIndentNum = 0 # 记录上一个item的层级
    
    beginIndex = 0
    if curDirIndex is not None:
        curDirIndex = min(curDirIndex,len(arr)-1)
        beginIndex = curDirIndex
        curDirLevel = getLevel(arr[curDirIndex])
        
    
    for index in range(beginIndex,len(arr)):
        item = arr[index]
        
        if(len(item)==0 or item.isspace()): # 只含空字符串跳过
            continue
        
        # 计算层级
        level = getLevel(item)
        if level>0:
            item = item[level:].strip() # 标题去除开头的'#'
            last_dirLevel = level
            printIndentNum = level - 1 
        else: 
            # 说明是正文 
            printIndentNum = last_dirLevel 
        
        if curDirIndex is not None:
            if index!=curDirIndex and level>0 and level<=curDirLevel:
                # 打印当前目录时，遇到小于等于curDirLevel的标题停止打印
                return 
       
        # 计算缩进
        if(curDirIndex is not None):
            # 打印当前目录时，从顶格开始打印
            indent = '    ' * (printIndentNum-curDirLevel+1)
        else:
            indent = '    ' * printIndentNum

    
        if last_prinIndentNum != printIndentNum:
            print(indent + '├── ' + item)
        else:
            print(indent + '└── ' + item)
        last_prinIndentNum = printIndentNum


class ListTreeCommand(Command):
    def __init__(self, doc: SimpleMarkdownDoc):
        super().__init__()
        self._doc = doc

    def Execute(self):
        lines = self._doc.GetLines()
        new_lines = []
        for line in lines:
            new_line = line[:-1] # 去除回车
            new_lines.append(new_line)
        # print(new_lines)
        print_array_as_tree(new_lines)

    def Undo(self):
        raise Exception
        pass
    
    def Undoable(self):
        return False

    def Skipable(self):
        return True


class DirTreeCommand(Command):
    def __init__(self, doc: SimpleMarkdownDoc,text:str):
        super().__init__()
        self._doc = doc
        self._text = text

    def Execute(self):
        
        lines = self._doc.GetLines()
        new_lines = []
        for line in lines:
            new_line = line[:-1] # 去除回车
            new_lines.append(new_line)
        
        title = self._text.strip()
        if len(title)==0 or title.isspace():  
            # title为空字符串则根据打印当前工作目录
            curLine = self._doc.current_line
            if(curLine==-1): # 为-1说明尚未修改文档，则打印全部
                print_array_as_tree(new_lines)
                return 
            level = 0 
            for index in range(curLine,-1,-1): 
                # curLine从后往前找到的第一个dir就是当前目录
                level = getLevel(new_lines[index])
                if(level>0):    
                    print_array_as_tree(new_lines,index)
                    break
            if(level==0):
                print_array_as_tree(new_lines) # 如果找不到dir，那就打印全部
        
        else:
            # title不为空
            level = 0 
            for index in range(0,len(new_lines)): 
                level = getLevel(new_lines[index])
                if(level>0): 
                    item = new_lines[index][level:].strip() # 去除前面的'#'
                    if(item==title):
                        print_array_as_tree(new_lines,index)
                        break
        
        
    def Undo(self):
        raise Exception
        pass
    
    def Undoable(self):
        return False

    def Skipable(self):
        return True

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
