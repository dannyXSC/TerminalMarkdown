from TerminalApp import TerminalApp


def main():
    app = TerminalApp()
    while True:
        user_input = input(r"请输入命令[q\Q退出]: ")
        if user_input == 'q' or user_input == 'Q':
            break
        input_list = user_input.split()
        command = input_list[0]
        if command == 'load':
            argument = ' '.join(input_list[1:])
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
        elif command == 'undo':
            app.Undo()
        elif command == 'redo':
            app.Redo()
        elif command == 'list':
            app.List()


if __name__ == '__main__':
    """
    TODO:
    1. delete
    2. list-tree
    3. dir-tree
    4. 日志模块
    5. 统计模块
    """
    main()
