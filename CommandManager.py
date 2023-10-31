from typing import List
from Command.Command import Command


class CommandManager(object):
    def __init__(self, capacity):
        self.__cmd_list: List[Command] = []
        # pos 指向已经最后一个执行完的命令
        self.__pos = -1
        # 最多可以存储多少个命令
        self.__capacity = capacity

    def __AddCommand(self, cmd: Command):
        # 假如做了undo，那么执行 Command 之前要把 undo 掉的删了
        self.__cmd_list = self.__cmd_list[:self.__pos + 1]
        self.__cmd_list.append(cmd)
        # 如果超出了容量，就要删除前面的历史
        self.__cmd_list = self.__cmd_list[-self.__capacity:]
        self.__pos = min(self.__pos + 1, self.__capacity - 1)

    def Execute(self, cmd: Command):
        if not cmd.Skipable():
            # 如果可以不可跳过，才记录这个command
            self.__AddCommand(cmd)
        cmd.Execute()

    def Undo(self):
        if self.__pos < 0:
            # 如果没有执行过命令或者已经 undo 到最初的命令，就什么都不执行
            return
        cur_cmd = self.__cmd_list[self.__pos]
        if not cur_cmd.Undoable():
            # 如果不可undo就退出
            return
        # 此时pos 指向的是可以 undo 的命令
        cur_cmd.Undo()
        # pos指向前一个命令
        self.__pos -= 1

    def Redo(self):
        if self.__pos >= len(self.__cmd_list) - 1:
            # 如果 pos 指向最后一个命令，那就没法执行 redo
            return
        self.__pos += 1
        self.__cmd_list[self.__pos].Execute()
