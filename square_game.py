"""
在真正的pygame窗口里运行你写的方块（Square）
=================================================
怎么用：
1. 把你自己在notebook里写的 make_square 函数（包括里面的 class Square）
   整段复制粘贴到下面标注 "把你的 make_square 粘贴到这里" 的地方，
   替换掉那个占位的 pass。
2. 在自己电脑的终端里运行：
       python3 square_game.py
3. 应该会弹出一个真正的窗口，用方向键（上下左右）试着移动红色方块，
   移到窗口边缘会停住不会跑出去，点窗口右上角的关闭按钮可以退出。

这个脚本本身不需要你改动（除了粘贴你的函数），
重点是感受一下：你写的 move / draw 这两个方法，
被套进一个"不断重复"的主循环之后，就变成了一个真的能玩的小程序。
"""

import sys
import pygame

# ============================================================
# 把你的 make_square 粘贴到这里（替换下面这一行 pass）
# ============================================================
def make_square(x, y, size, screen_w, screen_h, speed=5, color=(200, 0, 0)):
    pass
# ============================================================


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

        # 第二步：把真实的按键状态，转换成你的 move() 方法需要的"集合"
        # pygame.key.get_pressed() 返回的是一长串"每个键是不是按着"的状态，
        # 不能直接用 in 判断，所以这里把"当前按着的方向键"挑出来，
        # 重新组装成一个集合，格式和你notebook里测试用的 {pygame.K_LEFT} 这种是一样的。
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
