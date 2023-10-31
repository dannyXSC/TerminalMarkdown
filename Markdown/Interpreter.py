import abc
import re

from Markdown.Item import Item


class BaseInterpreter(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def Interpret(self, text: str):
        pass


class ItemInterpreter(BaseInterpreter):
    def __init__(self):
        super(ItemInterpreter, self).__init__()
        self.common_size = 10

    def Interpret(self, text: str):
        lines = text.split('\n')
        result = []
        for line in lines:
            match_result = re.search(r'^(#*|[\*-]) ', line)
            if match_result is None:
                result.append(Item(line, 'common', self.common_size))
            elif match_result.group(1)[0] == '#':
                length = len(match_result.group(1))
                result.append(Item(line[length + 1:], f'h{length}', max((6 - length), 1) * self.common_size))
            elif match_result.group(1) == '*' or match_result.group(1) == '-':
                result.append(Item("l " + line[2:], 'list', self.common_size))
        return result
