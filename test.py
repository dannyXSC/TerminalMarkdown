from TerminalApp import TerminalApp
import time
app = TerminalApp(2)
command_List = ["load test.md",
                        "history 4",
                        "list",
                        "save",
                        "list-tree",
                        "dir-tree",
                        "insert 3","list","save",
                        "append-head","list",
                        "append-tail","list",
                        "delete Java从入门到入土","list",
                        "undo","list",
                        "redo", "list",
                        "stats all",
                        "Q"
                ]
print("自动化测试脚本......")
for user_input in command_List:
    # 打开 txt 文件，并以读取模式打开
    time.sleep(1)
    print("-------------------")
    print("请输入命令[q\Q退出]: ", user_input)
    print("-------------------")
    # user_input = input(r"请输入命令[q\Q退出]: ")
    if user_input == 'q' or user_input == 'Q':
        app.session.quit()
        break
    app.logger.log(user_input)
    input_list = user_input.split()
    command = input_list[0]
    if command == 'load':
        argument = ' '.join(input_list[1:])
        filename = user_input.split(" ")[1]
        app.session.load(filename)
        app.session.current = filename
        app.Open(argument)
    elif command == 'save':
        app.Save()
    elif command == 'insert':
        if input_list[1].isdigit():
            row_num = int(input_list[1])
            argument = ' '.join(input_list[2:])
            app.InsertRow(row_num, argument)
        else:
            argument = ' '.join(input_list[1:])
            app.InsertTail(argument)
    elif command == 'append-head':
        argument = ' '.join(input_list[1:])
        app.InsertHead(argument)
    elif command == 'append-tail':
        argument = ' '.join(input_list[1:])
        app.InsertTail(argument)
    elif command == 'delete':
        if input_list[1].isdigit():
            row_num = int(input_list[1])
            app.DeleteRow(row_num)
        else:
            argument = ' '.join(input_list[1:])
            app.DeleteText(argument)
    elif command == 'undo':
        app.Undo()
    elif command == 'redo':
        app.Redo()
    elif command == 'list':
        app.List()
    elif command == "list-tree":
        app.ListTree()
    elif command == "dir-tree":
        if (len(input_list) == 1):
            app.DirTree('')
        else:
            app.DirTree(input_list[1])
    elif command == 'history':
        if user_input == command:
            app.History(app.logger.get_content(), 0)
        else:
            app.History(app.logger.get_content(), int(input_list[1]))
    elif command == 'stats':
        command_parts = user_input.split(" ")
        if len(command_parts) == 2:
            app.session.stats(command_parts[1])
        else:
            print("Invalid stats command.")


