"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def final_print(class_name, cnt, max, min, sum):
    print("=======" + class_name + "=======")
    if cnt == 0:
        print("No score for " + class_name)
    else:
        print("MAX (" + class_name + "):" + str(max))
        print("MIN (" + class_name + "):" + str(min))
        print("AVG (" + class_name + "):" + str(float(sum/cnt)))


def main():
    """
    TODO:
    """

    cnt001, max001, min001, sum001 = 0, 0, 0, 0
    cnt101, max101, min101, sum101 = 0, 0, 0, 0

    while True:
        class_name = input("Which class: ")
        class_name = class_name.upper()  # case insensitive
        if class_name == 'SC001':
            score = int(input("Score? "))
            # record 001
            cnt001 += 1
            if score > max001:
                max001 = score
            if min001 == 0 or score < min001:
                min001 = score
            sum001 = sum001 + score
        elif class_name == 'SC101':
            score = int(input("Score? "))
            # record 101
            cnt101 += 1
            if score > max101:
                max101 = score
            if min101 == 0 or score < min101:
                min101 = score
            sum101 = sum101 + score
        elif class_name == '-1':
            break
    if cnt001 + cnt101 == 0:
        print("No class scores were entered.")
    else:
        final_print('SC001', cnt001, max001, min001, sum001)
        final_print('SC101', cnt101, max101, min101, sum101)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
