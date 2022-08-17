"""
File: bouncing_ball.py
Name: Evie
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 5  # 球的水平速度
DELAY = 20  # 動畫停格多少毫秒(ms)
GRAVITY = 1  # 重力加速度;每一圈 while loop 垂直速度要加上的數值
SIZE = 20  # 球的直徑
REDUCE = 0.9  # 每一次反彈時，在垂直速度所剩之比例
START_X = 100  # 球的起始 x 座標
START_Y = 100  # 球的起始 y 座標

# Global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
flag = True
cnt = 0


def bounce(vx, vy):
    """
    球進行一次彈跳
    @param vx: 水平速度
    @param vy: 垂直速度
    """
    y0 = ball.y  # save the y location before bouncing
    while ball.y + ball.height < window.height:
        ball.move(vx, vy)
        vy = vy + GRAVITY  # 重力加速度
        pause(DELAY)

    # ball is on the floor
    vy = - vy
    # y0' = 地板到球的高度 = window.height - y0
    # y1' = 第一次彈跳後，地板到球的高度 = y0' * REDUCE
    while window.height - ball.y <= (window.height - y0) * REDUCE:
        ball.move(vx, vy)
        vy = vy + GRAVITY  # 往上速度應該減慢
        pause(DELAY)


def trigger_falling(mouse):
    global flag, cnt
    # print('flag=', flag)
    if flag:
        flag = False
        while ball.x <= window.width:
            # bounce the ball
            bounce(VX, VX)

        if ball.x > window.width:
            if cnt < 2:
                flag = True
            cnt += 1
            # print('cnt=', cnt)
            ball.move(0, 0)
            ball.x = START_X
            ball.y = START_Y


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(trigger_falling)


if __name__ == "__main__":
    main()
