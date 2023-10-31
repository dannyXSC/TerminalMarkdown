import abc


class Item(object):
    def __init__(self, text, type):
        self.text = text
        self.type = type
