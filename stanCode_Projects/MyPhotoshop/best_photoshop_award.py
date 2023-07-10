"""
File: best_photoshop_award.py
Name:
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

HURDLE_FACTOR = 1.5


def main():
    """
    創作理念：

    男：跟我結婚吧
    女：你有什麼？

    男：我家有蛋

    """
    ori_img = SimpleImage('best_photoshop作品及創作理念/me.jpeg')
    ori_img.show()
    egg_img = SimpleImage('best_photoshop作品及創作理念/egg-624x416.jpg')

    me_egg_img = me_egg(ori_img, egg_img)
    me_egg_img.show()


def me_egg(ori_img, egg_img):
    me_egg_img = SimpleImage.blank(egg_img.width, egg_img.height)  # 新增空白畫布

    for x in range(ori_img.width):  # 這邊先把我的臉Ｐ過去空白畫布，並且要往右對齊，這樣子蛋蛋才會在左邊，才會在我的視線範圍
        for y in range(ori_img.height):
            ori_img_pixel = ori_img.get_pixel(x, y)
            me_egg_img_pixel = me_egg_img.get_pixel(x + (me_egg_img.width - ori_img.width), y)

            avg = (ori_img_pixel.red + ori_img_pixel.blue + ori_img_pixel.green) / 3
            if ori_img_pixel.red < avg * HURDLE_FACTOR:
                me_egg_img_pixel.red = ori_img_pixel.red
                me_egg_img_pixel.blue = ori_img_pixel.blue
                me_egg_img_pixel.green = ori_img_pixel.green

    for x in range(me_egg_img.width):  # 這邊把空白畫布空白的地方用蛋蛋圖填滿
        for y in range(me_egg_img.height):
            me_egg_img_pixel = me_egg_img.get_pixel(x, y)
            egg_img_pixel = egg_img.get_pixel(x, y)

            # 空白的地方基本上一定是255x255x255
            if (me_egg_img_pixel.red + me_egg_img_pixel.green + me_egg_img_pixel.blue) / 3 == 255:
                me_egg_img_pixel.red = egg_img_pixel.red
                me_egg_img_pixel.blue = egg_img_pixel.blue
                me_egg_img_pixel.green = egg_img_pixel.green

    return me_egg_img


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
