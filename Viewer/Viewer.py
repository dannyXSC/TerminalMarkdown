import abc

from Document.Document import Document


class BaseViewer(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def Update(self, doc: Document):
        pass
