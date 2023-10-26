import abc


class Command(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def Execute(self):
        pass

    @abc.abstractmethod
    def Undo(self):
        pass

    def Undoable(self):
        return True

    def Skipable(self):
        return False
