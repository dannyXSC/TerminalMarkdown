from Document.BaseMDDocument import BaseMDDocument
from Document.Document import Document
from Markdown.PygameTextTool import PygameTextTool
from Viewer.Viewer import BaseViewer


class PygameViewer(BaseViewer):
    def __init__(self, name, width=400, height=600):
        super(PygameViewer, self).__init__(name)
        self.tool = PygameTextTool(name, width, height)

    def Update(self, doc: BaseMDDocument):
        item_list = doc.interpreter.Interpret(doc.GetRawStr())
        self.tool.WriteLines(item_list)
