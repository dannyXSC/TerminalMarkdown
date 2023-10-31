from typing import List

import pygame

from Markdown.Item import Item


class PygameTextTool(object):
    def __init__(self, name, width=400, height=600, margin_left=0, margin_top=0, font=None):
        self.name = name
        self.width = width
        self.height = height
        self.margin_left = margin_left
        self.margin_top = margin_top
        if font is None:
            self.default_font = 'Times'
        else:
            self.default_font = font

        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        self.window.fill((255, 255, 255))

    def GetFont(self, font, font_size):
        if font is None:
            return pygame.font.SysFont(self.default_font, font_size)
        else:
            return pygame.font.Font(font, font_size)

    def WriteLines(self, item_list: List[Item]):
        margin_top = self.margin_top
        self.window.fill((255, 255, 255))
        for item in item_list:
            font = self.GetFont(item.font, item.font_size)
            text = font.render(item.text, True, (0, 0, 0), (255, 255, 255))
            self.window.blit(text, (self.margin_left, margin_top))
            text_w, text_h = text.get_size()
            margin_top += text_h
        pygame.display.update()


#
# pygame.init()
# window = pygame.display.set_mode((400, 600))
# pygame.display.set_caption('显示文字')
# window.fill((255, 255, 255))
# # ==============显示文字============
# # 1.创建字体对象(选笔)
# # font.SysFont(字体名,字体大小, 是否加粗=False, 是否倾斜=False)   - 创建系统字体对象
# # font.Font(字体文件路径, 字体大小)
# # font = pygame.font.SysFont('Times', 30)
# font = pygame.font.SysFont('Times', 30)
#
# # 2.通过字体创建文字对象
# # 字体对象.render(文字内容,True,文字颜色,背景颜色=None)
# text = font.render('hello\n pygame', True, (0, 0, 0), (255, 255, 255))
#
# # 3.显示文字
# window.blit(text, (0, 0))
#
# # 4.获取文字内容的宽度和高度
# text_w, text_h = text.get_size()
# window.blit(text, (400 - text_w, 0))
#
# # 5.文字缩放和旋转
# new_text = pygame.transform.rotozoom(text, 45, 1.5)
# window.blit(new_text, (100, 200))
#
# pygame.display.flip()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
if __name__ == '__main__':
    tool = PygameTextTool('test')
    tool.WriteLines([Item('hello\n', 10), Item('world', 20)])
    input()
