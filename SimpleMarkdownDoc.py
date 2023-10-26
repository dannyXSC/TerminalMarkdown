import abc

from Document import Document


class SimpleMarkdownDoc(Document):
    def __init__(self, name):
        super().__init__(name)
        self._lines = []

    def GetLines(self):
        return self._lines

    def Save(self):
        with open(self._name, 'w') as f:
            f.writelines(self._lines)

    def Serialize(self):
        with open(self._name, 'r') as f:
            self._lines = f.readlines()

    def InsertRow(self, row_num, text):
        length = len(self._lines)
        if row_num < 0 or row_num > length:
            # 错误
            print("Error")
            return
        text = text + '\n'
        self._lines.insert(row_num, text)

    def DeleteRow(self, row_num):
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
