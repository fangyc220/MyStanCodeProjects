"""
File: boggle.py
Name: Steven
----------------------------------------
TODO: 使用者將會輸入固定的格式的英文字母(4x4)，之後這個code將會跑出由任意字母組成之英文單字(預設為字母長度>=4)，範例如下：

e.g.
	user_input_row_1: f u y l
	user_input_row_2: i o m g
	user_input_row_3: o r i l
	user_input_row_1: h j h u

	output: firm, room, roof....

"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
read_dic = {}
row_data = []
user_data = {}
all_word = []


def main():
	"""
	TODO: 使用者將會輸入固定的格式的英文字母(4x4)，之後這個code將會跑出由任意字母組成之英文單字(預設為字母長度>=4)，範例如下：

	e.g.
		user_input_row_1: f u y l
		user_input_row_2: i o m g
		user_input_row_3: o r i l
		user_input_row_1: h j h u

		output: firm, room, roof....
	"""
	if userdata(row_data):
		print('Illegal input')
	else:
		# -----start-----
		start = time.time()
		# 讀取字典
		read_dictionary(' '.join(row_data).split(' '))
		find_anagram()
		print(f'There are {len(all_word)} words in total.')
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(data):

	"""
	:param data: str, 使用者輸入的每一行字
	:return: dic, 字典的dictionary

	將會把使用者輸入的字母以及字典中的每個單字的字母進行比對，字典中的單字字母都要包含在使用者的輸入字母內．

	e.g.
		user_input_row_1: f u y l
		user_input_row_2: i o m g
		user_input_row_3: o r i l
		user_input_row_1: h j h u

		roof --> 加入到字典的dictionary
		firm --> 加入到字典的dictionary
		banana --> 不會加入到字典的dictionary

		可以減少字典的資料，加快比對時間

	"""
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""

	with open(FILE, 'r') as f:
		for lines in f:
			word = lines.strip()
			count = 0
			for s in word:
				if s in data:
					count += 1
			if count == len(word):
				read_dic[word] = 0


def has_prefix(sub_lst):
	"""
	:param sub_lst: (list) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	word = ''
	for num in sub_lst:
		word += user_data[num]

	for words in read_dic:
		if words.startswith(word):
			return False
	return True


def userdata(row_data):
	"""
	:return: bool, 使用者輸入資料的格式必須要符合要求，不符合要求會return Turn
	"""
	location = 0
	for i in range(4):
		# 檢查使用者輸入資料的格式
		data = input(f'{i + 1} row of letters: ')
		row_data.append(data)
		if row_data_check(row_data[-1]):
			return True

		"""
		把使用者輸入的資料轉換成dict, 並且是座標：字母
			e.g.
				dict = {(1, 1): 'f', (1, 2): 'y', ...}
		"""
		for num in data:
			if num.isalpha():
				location += 1
				user_data[i+1, location] = num
		location = 0


def row_data_check(row_data):
	"""
	:param row_data: list, 使用者所輸入的資料
	:return: bool, 協助判斷使用者輸入的資料是否有符合格式
	"""
	count = 0
	if len(row_data) == 7:
		for st in row_data:
			if count % 2 == 0:
				if st.isalpha():
					pass
				else:
					return True
			else:
				if st == ' ':
					pass
				else:
					return True
			count += 1
	else:
		return True


def find_anagram():
	"""
	:return: no return data

	開始跑anagram
	"""
	for i in range(4):
		for j in range(4):
			find_anagram_helper(i+1, j+1, [])


def find_anagram_helper(x, y, cur):
	"""
	:param x: int, 搜尋字母組合的起點座標x
	:param y: int, 搜尋字母組合的起點座標y
	:param cur: list(tuple), 儲存字母組合的每個座標
	:return: str, 在console顯示出有找到存在字典的單字

	Base case的條件:
		1. 搜尋到字母組合的數量為16

	"""
	if len(cur) == 16:
		word = ''
		for t in cur:
			word += user_data[t]

		if word in read_dic:
			if word not in all_word:
				all_word.append(word)
				print(word)
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				local_x = x + i
				local_y = y + j
				local = (local_x, local_y)
				if 5 > local_x > 0 and 5 > local_y > 0:
					if local not in cur:
						# early stopping
						if has_prefix(cur):
							break
						# choose
						cur.append(local)

						# 因為也要抓取字母排列>=4, 因此在這邊做攔截，如果字母排列>=4就比對字典，如果有在字典內就顯示在console
						if len(cur) >= 4:
							word = ''
							for t in cur:
								word += user_data[t]
							if word in read_dic:
								if word not in all_word:
									all_word.append(word)
									print(word)

						# explore
						find_anagram_helper(local_x, local_y, cur)
						# un-choose
						cur.pop()


if __name__ == '__main__':
	main()
