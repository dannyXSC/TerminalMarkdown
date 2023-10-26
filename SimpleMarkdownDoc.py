import abc

from Document import Document


class SimpleMarkdownDoc(Document):
    def __init__(self, name):
        super().__init__(name)
        self._lines = []

    def GetLines(self):
        # 获得所有的行信息
        return self._lines

    def Save(self):
        # 保存文件
        with open(self._name, 'w') as f:
            f.writelines(self._lines)

    def Serialize(self):
        # 序列化文件，即把文件流转成需要的格式
        with open(self._name, 'r') as f:
            self._lines = f.readlines()

    def InsertRow(self, row_num, text):
        # 在某一行插入内容
        length = len(self._lines)
        if row_num < 0 or row_num > length:
            # 错误
            print("Error")
            return
        text = text + '\n'
        self._lines.insert(row_num, text)

    def DeleteRow(self, row_num):
        # 删除某一行的内容
        length = len(self._lines)
        if row_num < 0 or row_num >= length:
            # 错误
            print("Error")
            return
        self._lines = self._lines[:row_num] + self._lines[row_num + 1:]

    def GetRowByContent(self, text):
        # 获得第一个匹配的行号，若不匹配返回-1
        for i, content in enumerate(self._lines):
            if content.find(text) != -1:
                return i
        return -1
