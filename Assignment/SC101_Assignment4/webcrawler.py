"""
File: webcrawler.py
Name: Evie
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
	for year in ['2010s', '2000s', '1990s']:
		print('---------------------------')
		print(year)
		url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

		response = requests.get(url)
		html = response.text
		soup = BeautifulSoup(html, features="html.parser")

		# ----- Write your code below this line ----- #
		data = []
		male_number = 0
		female_number = 0
		web_items = soup.find_all('table', {'class': 't-stripe'})

		for item in web_items:
			data = item.tbody.text.split()
		for i in range(len(data)):
			num = data[i].replace(',', '')
			if num.isdigit():
				if i % 5 == 2:  # male
					male_number += int(num)
				elif i % 5 == 4:  # female
					female_number += int(num)

		print('male_number: ' + str(male_number))
		print('female_number: ' + str(female_number))


if __name__ == '__main__':
	main()
