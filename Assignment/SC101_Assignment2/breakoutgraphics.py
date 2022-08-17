"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

彈珠工廠
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=self.window.width / 2 - self.paddle.width / 2,
                        y=self.window.height - self.paddle.height - paddle_offset)

        # Create a filled ball
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.__is_ball_moving = False
        self.ball.x = self.window.width / 2 - self.ball.width / 2
        self.ball.y = self.window.height / 2 - self.ball.height / 2

        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.paddle_follow_mouse)

        # Draw bricks
        color_list = ['red', 'orange', 'yellow', 'green', 'blue']
        for col in range(0, brick_cols):
            for row in range(0, brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color_list[int(row / 2)]
                brick_x = (self.brick.width + brick_spacing) * col
                brick_y = brick_offset + (self.brick.height + brick_spacing) * row
                self.window.add(self.brick, x=brick_x, y=brick_y)

    def init_ball(self):
        self.__dx = 0
        self.__dy = 0
        self.__is_ball_moving = False
        # center the ball in the graphical window
        self.ball.x = self.window.width / 2 - self.ball.width / 2
        self.ball.y = self.window.height / 2 - self.ball.height / 2

    def paddle_follow_mouse(self, event):
        new_x = event.x - self.paddle.width / 2
        if new_x <= 0:
            new_x = 0
        elif new_x + self.paddle.width >= self.window.width:
            new_x = self.window.width - self.paddle.width
        self.paddle.x = new_x

    def set_ball_velocity(self, event):
        if not self.__is_ball_moving:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__is_ball_moving = True

    def get_ball_dx(self):
        return self.__dx

    def get_ball_dy(self):
        return self.__dy

    def bounce_ball_x_direction(self):
        if self.__is_ball_moving:
            self.__dx = -self.__dx

    def bounce_ball_y_direction(self):
        if self.__is_ball_moving:
            self.__dy = -self.__dy
