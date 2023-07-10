"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    live = NUM_LIVES
    graphics.live.text = ('Live:' + str(live))
    # Add the animation loop here!
    while True:
        graphics.ball.move(graphics.get_vx(), graphics.get_vy())
        graphics.remove_brick()
        if graphics.ball.y > graphics.window.height:
            live -= 1
            graphics.live.text = ('Live:' + str(live))
            graphics.replace_ball()
            if live == 0:
                graphics.live.text = 'YOU LOSE!'
                break
        if graphics.game_check():
            graphics.live.text = 'YOU WIN!'
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
