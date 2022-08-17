"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def random_flip(input_num):
	cnt = 0
	flag = 1
	flip_str = ''
	while input_num != cnt:
		if r.randint(0, 1) == 1:
			flip_str += 'H'
		else:
			flip_str += 'T'

		if len(flip_str) > 1:
			if flip_str[len(flip_str) - 1] != flip_str[len(flip_str) - 2]:
				flag = 1
			elif flag == 1:
				cnt += 1
				flag = 0
		print("now str: " + flip_str + " , cnt: " + str(cnt))

	return flip_str


def main():
	"""
	TODO:
	"""
	print("Let's flip the coin!")
	run_num = int(input("Number of runs: "))
	print(random_flip(run_num))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
