"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    使用者輸入單字後，程式將開始嘗試各種單字組合，並判斷組合出來的單字是否存在於字典裡
    """
    while True:
        start = time.time()
        ####################
        print(f'Welcome to stanCode \'\'Anagram Generator\'\' (or {EXIT} to quit)')
        input_str = input("Find anagrams for: ")
        if input_str == EXIT:
            break
        find_anagrams(input_str)
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(dic_lst):
    '''
    read the file
    :param dic_lst: the words in file are keep in this dictionary list
    :return: none
    '''
    with open(FILE, 'r') as f:
        for line in f:
            dic_lst.append(line.rstrip('\n'))


def find_anagrams(s):
    """
    :param s: user input string
    :return: none
    """
    dictionary_lst = []
    read_dictionary(dictionary_lst)
    anagrams_lst = []
    print('Searching...')
    cnt = [0]  # for record
    find_anagrams_helper(s, anagrams_lst, '', dictionary_lst, len(s), cnt)
    print(f'{len(anagrams_lst)} anagrams: {anagrams_lst}')
    print(f' total {cnt[0]} runs')


def find_anagrams_helper(s, anagrams_lst, cur_str, dic_lst, input_str_len, cnt):
    '''
    :param s: sting, 待排列組合的字元
    :param anagrams_lst: list, 儲存所有合規的組合單字
    :param cur_str: string, 正在組合的單字
    :param dic_lst: dictionary list
    :param input_str_len: int, length of input string
    :param cnt: int, for debug, count the total loop
    :return: none
    '''
    cnt[0] += 1
    if len(cur_str) == input_str_len:
        # base cases
        if cur_str in dic_lst and cur_str not in anagrams_lst:
            print(f'Found: {cur_str}')
            anagrams_lst.append(cur_str)
            print('Searching...')
    else:
        for i in range(len(s)):
            new_s = s[0:i] + s[i + 1:]
            # choose
            temp_str = cur_str + s[i]
            # early stopping
            # if has_prefix(temp_str, dic_lst) and not in_anagrams(temp_str, anagrams_lst):
            if not in_anagrams(temp_str, anagrams_lst):
                if has_prefix(temp_str, dic_lst):
                    # explore
                    find_anagrams_helper(new_s, anagrams_lst, temp_str, dic_lst, input_str_len, cnt)
                    # un-choose


def in_anagrams(sub_s, lst):
    '''
    :param sub_s: string, 要確認的開頭
    :param lst: list, 儲存所有合規的組合單字
    :return: boolean, 組合單字裡是否存在由 sub_s 開頭的字彙
    '''
    for word in lst:
        if word.startswith(sub_s):
            return True
    return False


def has_prefix(sub_s, lst):
    '''
    :param sub_s: string, 要確認的開頭
    :param lst: list, 字典
    :return: boolean, 字典裡是否存在由 sub_s 開頭的字彙
    '''
    for word in lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
