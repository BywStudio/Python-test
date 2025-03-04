import sys

import pygame

from settings import Settings


# 管理游戏资源和行为的类
class AlienInvasion:
    def __init__(self):
        # 初始化游戏并创建游戏资源
        pygame.init()
        # 定义时钟
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # 显示窗口，宽：1200px，高: 800px
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        ))
        # 创建窗口标题：Alien Invasion
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        # 开始游戏的主循环
        while True:
            # 侦听鼠标、键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重新绘制屏幕
            self.screen.fill(self.settings.bg_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()