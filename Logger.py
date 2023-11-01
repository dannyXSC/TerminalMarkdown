import time
import abc


class BasicLogger(metaclass=abc.ABCMeta):
    def __int__(self):
        pass

    def log(self, content):
        pass

    def get_content(self):
        pass

    def get_time(self):
        return time.strftime('%Y%m%d %H:%M:%S', time.localtime())

    def close(self):
        pass


class Logger(BasicLogger):
    def __int__(self):
        self.f = open(file='log.txt', mode='a+', encoding='utf-8')
        start_content = f'session start at {self.get_time()}\n'
        self.f.write(start_content)

    def log(self, command):
        content = f'{self.get_time()} {command}\n'
        self.f.write(content)

    def get_content(self):
        content = self.f.readlines()
        return content

    def close(self):
        self.f.close()
