"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ROW = 4
COL = 4


def main():
	"""
	play a boggle game
	"""
	start = time.time()
	#############
	# char_arr = []
	# get_input_arr(char_arr)
	char_arr = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	find_anagrams(char_arr)
	#############
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def get_input_arr(char_arr):
	row_lst = []
	index = 0
	while index < COL:
		input_str = input(str(index + 1) + ' row of letters: ')
		input_str = input_str.lower()  # case insensitive
		row_lst = input_str.rsplit()
		if check_illegal(row_lst):
			print('Illegal input')
		else:
			char_arr.append(row_lst)
			row_lst = []
			index += 1


def check_illegal(s):
	if len(s) != ROW:
		return True
	for char in s:
		if not char.isalpha() or len(char) != 1:
			return True
	return False


def read_dictionary(dic_lst):
	'''
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:param dic_lst: the words in file are keep in this dictionary list
	:return: none
	'''
	with open(FILE, 'r') as f:
		for line in f:
			dic_lst.append(line.rstrip('\n'))


def find_anagrams(arr):
	"""
	:param arr: 4x4 list, record input characters
	:return: none
	"""
	dictionary_lst = []
	read_dictionary(dictionary_lst)
	anagrams_lst = []
	mark = []
	cnt = [0]  # for record
	for i in range(ROW):
		for j in range(COL):
			mark.append([i, j])
			find_anagrams_helper(arr, mark, anagrams_lst, arr[i][j], [i, j], dictionary_lst, cnt)
			mark.pop()
	print(f'There are {len(anagrams_lst)} words in total')
	print(f'Total {cnt[0]} runs')


def find_anagrams_helper(arr, mark, anagrams_lst, cur_str, a, dic_lst, cnt):
	'''
	:param arr: list, 待排列組合的4x4 list
	:param mark: list, 紀錄選過的位置
	:param anagrams_lst: list, 儲存所有合規的組合單字
	:param cur_str: string, 正在組合的單字
	:param a: list, 前一個所選字母的位置
	:param dic_lst: dictionary list
	:param cnt: int, for debug, count the total loop
	:return: none
	'''
	cnt[0] += 1
	if len(cur_str) >= 4:
		# base cases
		if cur_str in dic_lst and cur_str not in anagrams_lst:
			print(f'Found: {cur_str}')
			anagrams_lst.append(cur_str)
	# 左上 正上 右上 (a[0]-1, a[1]-1) (a[0]-1, a[1]) (a[0]-1, a[1]+1)
	# 正左 自己 正右 (a[0]  , a[1]-1) (a[0]  , a[1]) (a[0],   a[1]+1)
	# 左下 正下 右下 (a[0]+1, a[1]-1) (a[0]+1, a[1]) (a[0]+1, a[1]+1)
	for i in range(a[0] - 1, a[0] + 2):
		for j in range(a[1] - 1, a[1] + 2):
			if 0 <= i < COL and 0 <= j < ROW:
				if i != a[0] or j != a[1]:  # 不是自己
					if [i, j] not in mark:
						temp_str = cur_str + arr[i][j]
						if has_prefix(temp_str, dic_lst):
							mark.append([i, j])
							find_anagrams_helper(arr, mark, anagrams_lst, temp_str, [i, j], dic_lst, cnt)
							mark.pop()


def has_prefix(sub_s, lst):
	'''
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param lst: list, 字典
	:return: (bool) If there is any words with prefix stored in sub_s
	'''
	for word in lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
