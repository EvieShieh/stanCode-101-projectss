"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

這是一款很基本的彈珠遊戲
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    live = NUM_LIVES

    # Add the animation loop here!
    while True:
        graphics.ball.move(graphics.get_ball_dx(), graphics.get_ball_dy())
        pause(FRAME_RATE)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.bounce_ball_x_direction()
        if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.bounce_ball_y_direction()

        # Check object the ball hits
        ball_check_position1 = [graphics.ball.x, graphics.ball.y]
        ball_check_position2 = [graphics.ball.x + graphics.ball.width, graphics.ball.y]
        ball_check_position3 = [graphics.ball.x, graphics.ball.y + graphics.ball.height]
        ball_check_position4 = [graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height]
        if not is_ball_hit(graphics, ball_check_position1):
            if not is_ball_hit(graphics, ball_check_position2):
                if not is_ball_hit(graphics, ball_check_position3):
                    is_ball_hit(graphics, ball_check_position4)

        pause(FRAME_RATE)

        # manage lives
        if is_ball_missed_catch(graphics):
            live -= 1
            graphics.init_ball()
            if live <= 0:  # Game over la
                break


def is_ball_hit(graphics, position):
    """
    確認球是否有擊中物件
    :param graphics: class的物件
    :param position: 要確認的擊中位置
    :return: 是否球擊中object
    """
    obj = graphics.window.get_object_at(position[0], position[1])
    if obj is None:
        return False
    elif obj == graphics.paddle:
        graphics.bounce_ball_y_direction()
    else:  # object is brick
        graphics.window.remove(obj)
        graphics.bounce_ball_y_direction()
    return True


def is_ball_missed_catch(graphics):
    """
    確認球是否沒被板子接住
    :param graphics: class的物件
    :return: 球是否超過window底部
    """
    return graphics.ball.y + graphics.ball.height >= graphics.window.height


if __name__ == '__main__':
    main()
