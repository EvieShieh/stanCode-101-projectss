"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the original image
    :return: the blurred image
    """
    newImg = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_r = 0
            new_g = 0
            new_b = 0
            cnt = 0
            for j in range(3):  # x loop: x-1, x, x+1
                for i in range(3):  # y loop: y-1, y, y+1
                    if not (x + j - 1 == x and y + i - 1 == y):  # not itself
                        if 0 <= x + j - 1 < img.height and 0 <= y + i - 1 < img.width:  # in the region
                            # x-1 case: (x-1, y-1), (x-1, y), (x-1, y+1)
                            # x   case: (x  , y-1),           (x,   y+1)
                            # x+1 case: (x+1, y-1), (x+1, y), (x+1, y+1)
                            old_pixel = img.get_pixel(x + j - 1, y + i - 1)
                            new_r += old_pixel.red
                            new_b += old_pixel.blue
                            new_g += old_pixel.green
                            cnt += 1
            """
            # for debug 
            if (x == 0 and y == 0) or (x < 3 and y < 3):
                print(str(x) + ", " + str(y) + ": cnt=" +str(cnt))
            """
            new_pixel = newImg.get_pixel(x, y)
            new_pixel.red = new_r // cnt
            new_pixel.blue = new_b // cnt
            new_pixel.green = new_g // cnt
    return newImg


def main():
    """
    blur the image, show the before and after
    """
    old_img = SimpleImage("images/smiley-face.png")
    #old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
