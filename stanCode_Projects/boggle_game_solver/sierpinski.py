"""
File: sierpinski.py
Name: Steven
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO: 使用者可輸入層數，code會畫出對應層數的sierpinski triangle
	"""

	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, 常數, 表示三角形疊層的層數
	:param length: int, 第一層三角形的邊長
	:param upper_left_x: int, 第一層倒立三角形左上角的x點座標
	:param upper_left_y: int, 第一層倒立三角形左上角的y點座標
	:return:
	"""
	if order == 0:
		pass
	else:
		# Upper left
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# Upper right
		sierpinski_triangle(order-1, length/2, upper_left_x + length/2, upper_left_y)
		# Lower
		sierpinski_triangle(order-1, length/2, upper_left_x + length/4, upper_left_y + length*0.433)

		poly_1 = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
		poly_2 = GLine(upper_left_x + length * 0.5, upper_left_y + length * 0.866, upper_left_x + length, upper_left_y)
		poly_3 = GLine(upper_left_x + length, upper_left_y, upper_left_x, upper_left_y)

		window.add(poly_1)
		window.add(poly_2)
		window.add(poly_3)
		pause(10)

if __name__ == '__main__':
	main()
