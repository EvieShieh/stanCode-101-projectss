"""
File: my_drawing.py
Name: Evie
----------------------
Baymax is a cartoon character made of ovals.
Introduction is made in binary font, represents how the robot speaks
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow

# Global variables
window = GWindow(width=1000, height=750, title='BAYMAX!')


def main():
    """
    use campy class to draw a image
    """
    body_y = 250

    background = GRect(1000, 750)
    background.filled = True
    background.fill_color = 'firebrick'
    background.color = 'firebrick'
    window.add(background)

    # arm line
    color = 'black'
    arm_l1 = GOval(233, 353)
    arm_l1.filled = True
    arm_l1.fill_color = color
    arm_l1.color = color
    window.add(arm_l1, x=window.width / 2 + 5 - arm_l1.width, y=body_y + 22)

    arm_r1 = GOval(233, 353)
    arm_r1.filled = True
    arm_r1.fill_color = color
    arm_r1.color = color
    window.add(arm_r1, x=window.width / 2 - 5, y=body_y + 22)

    color = 'black'
    arm_l2 = GOval(207, 346)
    arm_l2.filled = True
    arm_l2.fill_color = color
    arm_l2.color = color
    window.add(arm_l2, x=window.width / 2 - 60 - arm_l2.width, y=arm_l1.y + 39)

    arm_r2 = GOval(207, 346)
    arm_r2.filled = True
    arm_r2.fill_color = color
    arm_r2.color = color
    window.add(arm_r2, x=window.width / 2 + 60, y=arm_l1.y + 39)

    # arm color
    color = 'white'
    arm_l1 = GOval(230, 350)
    arm_l1.filled = True
    arm_l1.fill_color = color
    arm_l1.color = color
    window.add(arm_l1, x=window.width / 2 + 5 - arm_l1.width, y=body_y + 25)

    arm_r1 = GOval(230, 350)
    arm_r1.filled = True
    arm_r1.fill_color = color
    arm_r1.color = color
    window.add(arm_r1, x=window.width / 2 - 5, y=body_y + 25)

    arm_l2 = GOval(205, 340)
    arm_l2.filled = True
    arm_l2.fill_color = color
    arm_l2.color = color
    window.add(arm_l2, x=window.width / 2 - 60 - arm_l2.width, y=arm_l1.y + 40)

    arm_r2 = GOval(205, 340)
    arm_r2.filled = True
    arm_r2.fill_color = color
    arm_r2.color = color
    window.add(arm_r2, x=window.width / 2 + 60, y=arm_l1.y + 40)

    # body line
    color = 'black'
    body1 = GOval(343, 403)
    body1.filled = True
    body1.fill_color = color
    body1.color = color
    window.add(body1, x=window.width / 2 - body1.width / 2, y=body_y - 3)

    body2 = GOval(394, 420)
    body2.filled = True
    body2.fill_color = color
    body2.color = color
    window.add(body2, x=body1.x + body1.width / 2 - body2.width / 2, y=body1.y + 60 - 4)

    # body color
    color = 'white'
    body1 = GOval(340, 400)
    body1.filled = True
    body1.fill_color = color
    body1.color = color
    window.add(body1, x=window.width / 2 - body1.width / 2, y=body_y)

    body2 = GOval(390, 410)
    body2.filled = True
    body2.fill_color = color
    body2.color = color
    window.add(body2, x=body1.x + body1.width / 2 - body2.width / 2, y=body1.y + 60)

    # body rect
    color = 'black'
    body_rect = GRect(336, 2)
    body_rect.filled = True
    body_rect.fill_color = color
    body_rect.color = color
    window.add(body_rect, x=window.width / 2 - body_rect.width / 2, y=body2.y + 93)

    # foot line
    color = 'black'
    foot_l = GOval(164, 124)
    foot_l.filled = True
    foot_l.fill_color = color
    foot_l.color = color
    window.add(foot_l, x=window.width / 2 - 9 - foot_l.width, y=body2.y + body2.height - 132)

    foot_r = GOval(164, 124)
    foot_r.filled = True
    foot_r.fill_color = color
    foot_r.color = color
    window.add(foot_r, x=window.width / 2 + 9, y=body2.y + body2.height - 132)

    # foot color
    color = 'white'
    foot_l = GOval(160, 120)
    foot_l.filled = True
    foot_l.fill_color = color
    foot_l.color = color
    window.add(foot_l, x=window.width / 2 - 10 - foot_l.width, y=body2.y + body2.height - 130)

    foot_r = GOval(160, 120)
    foot_r.filled = True
    foot_r.fill_color = color
    foot_r.color = color
    window.add(foot_r, x=window.width / 2 + 10, y=body2.y + body2.height - 130)

    # face line
    color = 'black'
    face = GOval(184, 136)
    face.filled = True
    face.fill_color = color
    window.add(face, x=window.width / 2 - face.width / 2, y=body1.y - face.height * 2.7 / 4)

    # face color
    color = 'white'
    face = GOval(180, 130)
    face.filled = True
    face.fill_color = color
    window.add(face, x=window.width / 2 - face.width / 2, y=body1.y - face.height * 2.7 / 4)

    # eyes
    eye_l = GOval(20, 18)
    eye_l.filled = True
    eye_l.fill_color = 'black'
    eye_r = GOval(20, 18)
    eye_r.filled = True
    eye_r.fill_color = 'black'
    window.add(eye_l, x=window.width / 2 - 50 - eye_l.width / 2, y=face.y + 50)
    window.add(eye_r, x=window.width / 2 + 50 - eye_l.width / 2, y=face.y + 50)

    # mouth rect
    color = 'black'
    mouth_rect = GRect(100, 2)
    mouth_rect.filled = True
    mouth_rect.fill_color = color
    mouth_rect.color = color
    window.add(mouth_rect, x=window.width / 2 - mouth_rect.width / 2, y=eye_r.y + 7)

    # logo
    logo1 = GOval(60, 60)
    logo1.filled = True
    logo1.fill_color = 'white'
    window.add(logo1, x=window.width / 2 + 40, y=body1.y + 70)

    color = 'black'
    logo2 = GRect(60, 1)
    logo2.filled = True
    logo2.fill_color = color
    logo2.color = color
    window.add(logo2, x=logo1.x, y=logo1.y + logo1.height / 2)

    # dialog
    color = 'white'
    dialog = GRect(800, 100)
    dialog.filled = True
    dialog.fill_color = color
    dialog.color = color
    window.add(dialog, x=window.width / 2 - dialog.width / 2, y=25)

    # letter
    letter_blank = 8 * 9
    letter_start_x = dialog.x + 12
    letter_start_y = dialog.y + 15
    add_letter('I', letter_x=letter_start_x, letter_y=letter_start_y)
    add_letter('A', letter_x=letter_start_x + letter_blank * 1.5, letter_y=letter_start_y)
    add_letter('M', letter_x=letter_start_x + letter_blank * 2.5, letter_y=letter_start_y)
    add_letter('B', letter_x=letter_start_x + letter_blank * 4, letter_y=letter_start_y)
    add_letter('A', letter_x=letter_start_x + letter_blank * 5, letter_y=letter_start_y)
    add_letter('Y', letter_x=letter_start_x + letter_blank * 6, letter_y=letter_start_y)
    add_letter('M', letter_x=letter_start_x + letter_blank * 7, letter_y=letter_start_y)
    add_letter('A', letter_x=letter_start_x + letter_blank * 8, letter_y=letter_start_y)
    add_letter('X', letter_x=letter_start_x + letter_blank * 9, letter_y=letter_start_y)
    add_letter('!', letter_x=letter_start_x + letter_blank * 10, letter_y=letter_start_y)


def add_letter(letter, letter_x, letter_y):
    if letter == 'B':
        create_rect(letter_x, letter_y, 0, 0)
        create_rect(letter_x, letter_y, 1, 0)
        create_rect(letter_x, letter_y, 2, 0)
        create_rect(letter_x, letter_y, 3, 0)
        create_rect(letter_x, letter_y, 0, 1)
        create_rect(letter_x, letter_y, 0, 2)
        create_rect(letter_x, letter_y, 0, 3)
        create_rect(letter_x, letter_y, 0, 4)
        create_rect(letter_x, letter_y, 0, 5)
        create_rect(letter_x, letter_y, 0, 6)
        create_rect(letter_x, letter_y, 1, 3)
        create_rect(letter_x, letter_y, 2, 3)
        create_rect(letter_x, letter_y, 3, 3)
        create_rect(letter_x, letter_y, 1, 6)
        create_rect(letter_x, letter_y, 2, 6)
        create_rect(letter_x, letter_y, 3, 6)
        create_rect(letter_x, letter_y, 4, 1)
        create_rect(letter_x, letter_y, 4, 2)
        create_rect(letter_x, letter_y, 4, 4)
        create_rect(letter_x, letter_y, 4, 5)
    elif letter == 'A':
        create_rect(letter_x, letter_y, 1, 0)
        create_rect(letter_x, letter_y, 2, 0)
        create_rect(letter_x, letter_y, 3, 0)
        create_rect(letter_x, letter_y, 0, 1)
        create_rect(letter_x, letter_y, 0, 2)
        create_rect(letter_x, letter_y, 0, 3)
        create_rect(letter_x, letter_y, 0, 4)
        create_rect(letter_x, letter_y, 0, 5)
        create_rect(letter_x, letter_y, 0, 6)
        create_rect(letter_x, letter_y, 4, 1)
        create_rect(letter_x, letter_y, 4, 2)
        create_rect(letter_x, letter_y, 4, 3)
        create_rect(letter_x, letter_y, 4, 4)
        create_rect(letter_x, letter_y, 4, 5)
        create_rect(letter_x, letter_y, 4, 6)
        create_rect(letter_x, letter_y, 1, 3)
        create_rect(letter_x, letter_y, 2, 3)
        create_rect(letter_x, letter_y, 3, 3)
    elif letter == 'Y':
        create_rect(letter_x, letter_y, 0, 0)
        create_rect(letter_x, letter_y, 0, 1)
        create_rect(letter_x, letter_y, 4, 0)
        create_rect(letter_x, letter_y, 4, 1)
        create_rect(letter_x, letter_y, 1, 2)
        create_rect(letter_x, letter_y, 3, 2)
        create_rect(letter_x, letter_y, 2, 3)
        create_rect(letter_x, letter_y, 2, 4)
        create_rect(letter_x, letter_y, 2, 5)
        create_rect(letter_x, letter_y, 2, 6)
    elif letter == 'M':
        create_rect(letter_x, letter_y, 0, 0)
        create_rect(letter_x, letter_y, 0, 1)
        create_rect(letter_x, letter_y, 0, 2)
        create_rect(letter_x, letter_y, 0, 3)
        create_rect(letter_x, letter_y, 0, 4)
        create_rect(letter_x, letter_y, 0, 5)
        create_rect(letter_x, letter_y, 0, 6)
        create_rect(letter_x, letter_y, 4, 0)
        create_rect(letter_x, letter_y, 4, 1)
        create_rect(letter_x, letter_y, 4, 2)
        create_rect(letter_x, letter_y, 4, 3)
        create_rect(letter_x, letter_y, 4, 4)
        create_rect(letter_x, letter_y, 4, 5)
        create_rect(letter_x, letter_y, 4, 6)
        create_rect(letter_x, letter_y, 1, 1)
        create_rect(letter_x, letter_y, 2, 2)
        create_rect(letter_x, letter_y, 3, 1)
    elif letter == 'X':
        create_rect(letter_x, letter_y, 0, 0)
        create_rect(letter_x, letter_y, 0, 1)
        create_rect(letter_x, letter_y, 0, 5)
        create_rect(letter_x, letter_y, 0, 6)
        create_rect(letter_x, letter_y, 4, 0)
        create_rect(letter_x, letter_y, 4, 1)
        create_rect(letter_x, letter_y, 4, 5)
        create_rect(letter_x, letter_y, 4, 6)
        create_rect(letter_x, letter_y, 1, 2)
        create_rect(letter_x, letter_y, 1, 4)
        create_rect(letter_x, letter_y, 2, 3)
        create_rect(letter_x, letter_y, 3, 2)
        create_rect(letter_x, letter_y, 3, 4)
    elif letter == 'I':
        create_rect(letter_x, letter_y, 2, 0)
        create_rect(letter_x, letter_y, 2, 1)
        create_rect(letter_x, letter_y, 2, 2)
        create_rect(letter_x, letter_y, 2, 3)
        create_rect(letter_x, letter_y, 2, 4)
        create_rect(letter_x, letter_y, 2, 5)
        create_rect(letter_x, letter_y, 2, 6)
        create_rect(letter_x, letter_y, 1, 0)
        create_rect(letter_x, letter_y, 3, 0)
        create_rect(letter_x, letter_y, 1, 6)
        create_rect(letter_x, letter_y, 3, 6)
    elif letter == '!':
        create_rect(letter_x, letter_y, 2, 0)
        create_rect(letter_x, letter_y, 2, 1)
        create_rect(letter_x, letter_y, 2, 2)
        create_rect(letter_x, letter_y, 2, 3)
        create_rect(letter_x, letter_y, 2, 6)
    else:
        return


def create_rect(letter_x, letter_y, rect_x, rect_y):
    size = 7
    blank = size / 2
    color = 'black'
    letter_rect = GRect(size, size)
    letter_rect.filled = True
    letter_rect.fill_color = color
    letter_rect.color = color
    window.add(letter_rect, x=letter_x + (size + blank) * rect_x, y=letter_y + (size + blank) * rect_y)


if __name__ == '__main__':
    main()
