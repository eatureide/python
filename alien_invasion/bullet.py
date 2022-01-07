import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.color = self.setting.bullet_color
        # 在(0,0)坐标创建一个子弹的矩形，再设置正确位置
        self.rect = pygame.Rect(
            0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用小数标识子弹位置
        self.y = float(self.rect.y)

    def update(self):
        # 更新表示子弹位置的小数值
        self.y -= self.setting.bullet_speed
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
