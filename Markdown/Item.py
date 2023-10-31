import abc


class Item(object):
    def __init__(self, text, md_type, font_size, font=None):
        self.text = text
        self.type = md_type
        self.font_size = font_size
        self.font = font
