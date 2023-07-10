"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            new_img_pixel = new_img.get_pixel(x, y)
            img_pixel_red = 0
            img_pixel_blue = 0
            img_pixel_green = 0
            count = 0


            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                for i in range(0, 2):
                    for j in range(0, 2):
                        img_pixel = img.get_pixel(x + i, y + j)
                        img_pixel_red += img_pixel.red
                        img_pixel_blue += img_pixel.blue
                        img_pixel_green += img_pixel.green
                        count += 1

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                for i in range(-1, 1, 1):
                    for j in range(0, 2):
                        img_pixel = img.get_pixel(x + i, y + j)
                        img_pixel_red += img_pixel.red
                        img_pixel_blue += img_pixel.blue
                        img_pixel_green += img_pixel.green
                        count += 1

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                for i in range(0, 2):
                    for j in range(-1, 1, 1):
                        img_pixel = img.get_pixel(x + i, y + j)
                        img_pixel_red += img_pixel.red
                        img_pixel_blue += img_pixel.blue
                        img_pixel_green += img_pixel.green
                        count += 1

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                for i in range(-1, 1, 1):
                    for j in range(-1, 1, 1):
                        img_pixel = img.get_pixel(x + i, y + j)
                        img_pixel_red += img_pixel.red
                        img_pixel_blue += img_pixel.blue
                        img_pixel_green += img_pixel.green
                        count += 1
 
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                for i in range(-1, 2, 1):
                    for j in range(0, 2):
                        img_pixel = img.get_pixel(x + i, y + j)
                        img_pixel_red += img_pixel.red
                        img_pixel_blue += img_pixel.blue
                        img_pixel_green += img_pixel.green
                        count += 1

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                for i in range(-1, 2, 1):
                    for j in range(-1, 1, 1):
                        img_pixel = img.get_pixel(x + i, y + j)
                        img_pixel_red += img_pixel.red
                        img_pixel_blue += img_pixel.blue
                        img_pixel_green += img_pixel.green
                        count += 1

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                for i in range(0, 2):
                    for j in range(-1, 2, 1):
                        img_pixel = img.get_pixel(x + i, y + j)
                        img_pixel_red += img_pixel.red
                        img_pixel_blue += img_pixel.blue
                        img_pixel_green += img_pixel.green
                        count += 1

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                for i in range(-1, 1, 1):
                    for j in range(-1, 2, 1):
                        img_pixel = img.get_pixel(x + i, y + j)
                        img_pixel_red += img_pixel.red
                        img_pixel_blue += img_pixel.blue
                        img_pixel_green += img_pixel.green
                        count += 1

            else:
                # Inner pixels.
                for i in range(-1, 2, 1):
                    for j in range(-1, 2, 1):
                        img_pixel = img.get_pixel(x + i, y + j)
                        img_pixel_red += img_pixel.red
                        img_pixel_blue += img_pixel.blue
                        img_pixel_green += img_pixel.green
                        count += 1

            avg_red = img_pixel_red / count
            avg_blue = img_pixel_blue / count
            avg_green = img_pixel_green / count

            new_img_pixel.red = avg_red
            new_img_pixel.blue = avg_blue
            new_img_pixel.green = avg_green
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
