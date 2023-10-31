import abc


class BaseInterpreter(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def Interpret(self, text: str):
        pass
