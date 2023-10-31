from Document.BaseMDDocument import BaseMDDocument
from Viewer.Viewer import BaseViewer


class TerminalViewer(BaseViewer):
    def __init__(self, name, width=400, height=600):
        super(TerminalViewer, self).__init__(name)

    def Update(self, doc: BaseMDDocument):
        lines = doc.GetLines()
        for line in lines:
            print(line, end="")
