"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))  # 5
    print(find_largest_digit(281))  # 8
    print(find_largest_digit(6))  # 6
    print(find_largest_digit(-111))  # 1
    print(find_largest_digit(-9453))  # 9


def find_largest_digit(n):
    """
    :param n: input integers
    :return: largest digit
    """
    n = abs(n)

    if n == 0:
        return 0  # base case, no more digit in n

    digit_1 = n % 10  # get the digit
    remain_n = int((n - digit_1) / 10)  # the remain number in n
    digit_2 = find_largest_digit(remain_n)
    # print(digit_1, remain_n, digit_2)
    return max(digit_1, digit_2)


if __name__ == '__main__':
    main()
