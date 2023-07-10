"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 3  # Number of rows of bricks
BRICK_COLS = 3  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball

CHANGE_BALL_X_SPEED = 2  # 改變x方向的速度
LONGER_WIDTH = 20
LONGER_HEIGHT = 20
LONGER_RANGE = 20


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self._window_width = window_width
        self._window_height = window_height
        # Create a paddle
        self._paddle_width = paddle_width
        self._paddle_height = paddle_height
        self._paddle_offset = paddle_offset
        self.paddle = GRect(self._paddle_width, self._paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - self._paddle_width) / 2,
                        y=window_height - self._paddle_height - self._paddle_offset)
        # Center a filled ball in the graphical window
        self._ball_radius = ball_radius
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width / 2 - ball_radius, y=window_height / 2 - ball_radius)
        # Default initial velocity for the ball
        self._change_ball_x = CHANGE_BALL_X_SPEED
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.check_point)
        self.__vx = 0
        self.__vy = 0
        self.check = 0
        self.touch = 0
        self.total = brick_rows * brick_cols
        self.brick_num = 0
        # Draw bricks
        dx = 0
        dy = 0
        for i in range(brick_rows):  # 新增磚塊
            if i > 0:
                dx += brick_width + brick_spacing
            self.count = 0
            for j in range(brick_cols):
                if j == 0:
                    dy = 0
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.color = 'black'

                self.brick.fill_color = self.brick_color()
                self.count += 1

                self.window.add(self.brick, x=dx, y=brick_offset + dy)
                dy += brick_spacing + self.brick.height

        # Create a label
        self.live = GLabel('Live:')
        self.live.font = '-30'
        self.window.add(self.live, x=0, y=self.window.height - 10)

        self._longer_width = LONGER_WIDTH
        self._longer_height = LONGER_HEIGHT
        self.no_bonus = True
        self.longer = GRect(self._longer_width, self._longer_height)
        self.longer.filled = True
        self.longer.fill_color = 'tomato'
        self._longer_range = LONGER_RANGE

    def brick_color(self):  # 產生磚塊的顏色
        if self.count == 0:
            return 'red'
        elif self.count == 1:
            return 'red'
        elif self.count == 2:
            return 'orange'
        elif self.count == 3:
            return 'orange'
        elif self.count == 4:
            return 'yellow'
        elif self.count == 5:
            return 'yellow'
        elif self.count == 6:
            return 'green'
        elif self.count == 7:
            return 'green'
        else:
            return 'blue'

    def paddle_move(self, event):  # 新增paddle，並讓paddle保持在滑鼠的中間以及不掉出window視窗外
        """
        :param event: int, 滑鼠的座標
        :return: object, 新增一個paddle在window上
        """
        self.paddle_x = event.x - self.paddle.width / 2
        if self.paddle_x <= 0:
            self.paddle_x = 0
        elif self.paddle_x >= self.window.width - self._paddle_width:
            self.paddle_x = self.window.width - self._paddle_width
        self.window.add(self.paddle, x=self.paddle_x, y=self.window.height - self._paddle_height - self._paddle_offset)

    def get_vx(self):  # 製作一個method，讓main()得到球的x方向的速度值
        """
        :return: int, ball的x方向的速度值
        """
        if self.ball.x <= 0 or self.ball.x + self._ball_radius * 2 >= self.window.width:
            self.__vx = -self.__vx
        return self.__vx

    def get_vy(self):  # 製作一個method，讓main()得到球的y方向的速度值
        """
        :return: int, ball的y方向的速度值
        """
        if self.ball.y <= 0:
            self.__vy = -self.__vy
        return self.__vy

    def remove_brick(self):
        if self.check_touch():
            if self.touch != self.paddle and self.touch != self.live and self.touch != self.longer:
                self.window.remove(self.touch)
                self.brick_num += 1
                print(self.brick_num)
                self.__vy = -self.__vy
            elif self.touch == self.paddle:
                rand = random.random()
                if rand < 0.5:
                    self.__vx += self._change_ball_x
                if rand > 0.5:
                    self.__vx -= self._change_ball_x
                self.__vy = -self.__vy

    def stop_move(self, event):  # 製作pass method讓失去3命以及遊戲開始後點擊滑鼠不會有作動
        pass

    def check_point(self, event):
        # 遊戲一開始球在window上時，要不能動，必須等待滑鼠點擊後才能動，因此有設定self.check當作開關
        # 一開始self.check == 0, if保持False, 直到點擊後self.check +=1才會進入if, 並且x, y獲得初始速度
        """
        :param event: int, 滑鼠的座標
        """
        self.check += 1
        if self.check > 0:
            self.__vy = INITIAL_Y_SPEED
            self.__vx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__vx = -self.__vx
            onmouseclicked(self.stop_move)

    def replace_ball(self):  # 每當失去一命，self.check -= 1, 讓球保持不動；x, y速度變為0, 並新增一顆球在window
        """
        :return:
        """
        self.check -= 1
        self.__vy = 0
        self.__vx = 0
        self.window.add(self.ball, x=self._window_width / 2 - self._ball_radius,
                        y=self._window_height / 2 - self._ball_radius)
        onmouseclicked(self.check_point)

    def check_touch(self):  # 每當ball移動一個位置，針對ball的4個端點進行偵測，確認是否有碰到東西
        """
        :return: bool, 回傳ball是否有碰到東西
        """
        ball_x = self.ball.x
        ball_y = self.ball.y
        for i in range(0, self._ball_radius * 2 + 1, self._ball_radius * 2):
            for j in range(0, self._ball_radius * 2 + 1, self._ball_radius * 2):
                self.touch = self.window.get_object_at(ball_x + i, ball_y + j)
                if self.touch is not None:
                    return True

    def game_check(self):
        if self.brick_num == self.total:
            return True
        else:
            return False
