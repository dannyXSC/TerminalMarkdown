from TerminalApp import TerminalApp
import time

app = TerminalApp(2)
app2 = TerminalApp(2)

print("自动化测试脚本......")
# load
print("load test.md")
app.session.load("test.md")
app.session.current = "test.md"
app.Open("test.md")
time.sleep(0.5)
print("load test2.md")
app2.session.load("test2.md")
app2.session.current = "test2.md"
app2.Open("test2.md")
time.sleep(0.5)
# save
print("save test.md")
app.Save()
time.sleep(0.5)
# insert 3
print("insert 3 ad+ test2.md")
app2.InsertRow(3,"ad+")
time.sleep(0.5)
# append-head
print("append-head head test.md")
app.InsertHead("head")
time.sleep(0.5)
# append-tail
print("append-tail tail test2.md")
app2.InsertTail("tail")
time.sleep(0.5)
# delete Java从入门到入土
print("delete Java从入门到入土 test.md")
app.DeleteText("Java从入门到入土")
time.sleep(0.5)
# undo
print("undo")
app.Undo()
time.sleep(0.5)
# redo
print("redo")
app.Redo()
time.sleep(0.5)
# list
print("list")
app.List()
time.sleep(0.5)
# list-tree
print("list-tree")
app.ListTree()
time.sleep(0.5)
# dir-tree
print("dir-tree")
app.DirTree('')
time.sleep(0.5)
# history 4
print("history 4")
app.History(app.logger.get_content(), 4)
time.sleep(0.5)
# stats all
print("stats all")
app.session.stats("all")
time.sleep(0.5)
# quit
print("quit test.md")
app.session.quit()
time.sleep(0.5)
print("quit test2.md")
app2.session.quit()

