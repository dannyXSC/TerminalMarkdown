import abc

from Document import Document


class SimpleMarkdownDoc(Document):
    def __init__(self, name):
        super().__init__(name)
        self._lines = []
        self.current_line = -1 # 默认操作最后一行

    def GetLines(self):
        # 获得所有的行信息
        return self._lines

    def Save(self):
        # 保存文件
        with open(self._name, 'w',encoding='utf-8') as f:
            f.writelines(self._lines)

    def Serialize(self):
        # 序列化文件，即把文件流转成需要的格式
        with open(self._name, 'r',encoding='utf-8') as f:
            self._lines = f.readlines()

    def InsertRow(self, row_num, text):
        # 在某一行插入内容
        length = len(self._lines)
        # 如果row num大于length 则要插入到最后一行
        row_num = min(row_num, length)
        if row_num < 0:
            # 错误
            print("Error")
            return
        text = text + '\n'
        self.current_line = min(row_num,length) # 记录操作行为插入的行
        self._lines.insert(row_num, text)
        

    def DeleteRow(self, row_num):
        # 删除某一行的内容
        length = len(self._lines)
        if row_num < 0 or row_num >= length:
            # 错误
            print("Error")
            return
        self.current_line = row_num-1 # 记录操作行为删除行的前一行
        self._lines = self._lines[:row_num] + self._lines[row_num + 1:]
        
        
    def GetRowByContent(self, text):
        # 获得第一个匹配的行号，若不匹配返回-1
        for i, content in enumerate(self._lines):
            if content.find(text) != -1:
                return i
        return -1


class ProxyDoc(SimpleMarkdownDoc):
    def __init__(self, name):
        super().__init__(name)
        self.is_change = False

    def InsertRow(self, row_num, text):
        super().InsertRow(row_num,text)
        self.is_change = True

    def Save(self):
        super().Save()
        self.is_change = False