"""
File: mirror_lake.py
Name:
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the filepath of an image.
    :return: SimpleImage, a mirror image
    """
    ori_img = SimpleImage(filename)
    new_img = SimpleImage.blank(ori_img.width, ori_img.height * 2)

    for i in range(ori_img.width):  # 先做鏡向上半部
        for j in range(ori_img.height):
            ori_img_pixel = ori_img.get_pixel(i, j)
            new_img_pixel = new_img.get_pixel(i, j)
            new_img_pixel.red = ori_img_pixel.red
            new_img_pixel.blue = ori_img_pixel.blue
            new_img_pixel.green = ori_img_pixel.green

    for i in range(ori_img.width):  # 這邊再做鏡像的下半部
        for j in range(ori_img.height):
            ori_img_pixel = ori_img.get_pixel(i, j)
            new_img_pixel = new_img.get_pixel(i, new_img.height - j -1)
            new_img_pixel.red = ori_img_pixel.red
            new_img_pixel.blue = ori_img_pixel.blue
            new_img_pixel.green = ori_img_pixel.green
    return new_img


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
