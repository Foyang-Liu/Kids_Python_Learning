"""
在真正的pygame窗口里运行你写的方块（Square）
=================================================
用法：
    python3 square_game.py

应该会弹出一个真正的窗口，用方向键（上下左右）移动红色方块，
移到窗口边缘会停住不会跑出去，点窗口右上角的关闭按钮可以退出。

下面的 make_square 函数就是你自己在Day70 Checkpoint里写的那一版，
只是把缩进重新整理好了，逻辑完全没有改动。
"""

import sys
import pygame


def make_square(x, y, size, screen_w, screen_h, speed=5, color=(200, 0, 0)):
    class Square:
        def __init__(self, x, y, size, screen_w, screen_h, speed=5, color=(200, 0, 0)):
            self.x = x
            self.y = y
            self.size = size
            self.screen_h = screen_h
            self.screen_w = screen_w
            self.speed = speed
            self.color = color

        def move(self, pressed_keys):
            dx = 0
            dy = 0
            if pygame.K_RIGHT in pressed_keys:
                dx += self.speed
            if pygame.K_LEFT in pressed_keys:
                dx -= self.speed
            if pygame.K_UP in pressed_keys:
                dy -= self.speed
            if pygame.K_DOWN in pressed_keys:
                dy += self.speed
            self.x = self.x + dx
            self.y = self.y + dy
            if self.x < 0:
                self.x = 0
            if self.x > self.screen_w - self.size:
                self.x = self.screen_w - self.size
            if self.y < 0:
                self.y = 0
            if self.y > self.screen_h - self.size:
                self.y = self.screen_h - self.size
            return (self.x, self.y)

        def draw(self, surface):
            pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
            return surface

    square = Square(x, y, size, screen_w, screen_h, speed, color)
    return square


def main():
    pygame.init()

    screen_w, screen_h = 400, 300
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("我的方块 - 方向键移动")
    clock = pygame.time.Clock()

    square = make_square(100, 100, 30, screen_w, screen_h, speed=5, color=(200, 0, 0))

    running = True
    while running:
        # 第一步：处理事件（比如点了关闭按钮）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 第二步：把真实的按键状态，转换成 move() 方法需要的"集合"
        # pygame.key.get_pressed() 返回的是一长串"每个键是不是按着"的状态，
        # 不能直接用 in 判断，所以这里把"当前按着的方向键"挑出来，
        # 重新组装成一个集合，格式和notebook里测试用的 {pygame.K_LEFT} 这种是一样的。
        keys = pygame.key.get_pressed()
        pressed_keys = {
            k for k in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
            if keys[k]
        }

        # 第三步：更新方块位置
        square.move(pressed_keys)

        # 第四步：画面——先把背景清空，再把方块画上去
        screen.fill((255, 255, 255))  # 白色背景
        square.draw(screen)

        # 第五步：把画好的内容真正显示到窗口上
        pygame.display.flip()

        # 控制帧率，每秒最多跑60次循环
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
