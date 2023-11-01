import time
import abc


class BasicLogger(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    def log(self, content):
        pass

    def get_content(self):
        pass

    def get_time(self):
        return time.strftime('%Y%m%d %H:%M:%S', time.localtime())


class Logger(BasicLogger):
    def __init__(self):
        super().__init__()
        with open(file='log.txt', mode='a+', encoding='utf-8') as f:
            start_content = f'session start at {self.get_time()}\n'
            f.write(start_content)
            f.close()

    def log(self, command):
        content = f'{self.get_time()} {command}\n'
        with open(file='log.txt', mode='a+', encoding='utf-8') as f:
            f.write(content)
            f.close()

    def get_content(self):
        with open(file='log.txt', mode='r', encoding='utf-8') as f:
            content = f.readlines()
            f.close()
        return content



