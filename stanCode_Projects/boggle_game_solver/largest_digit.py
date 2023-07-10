"""
File: largest_digit.py
Name: Steven
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, 一個int
	:return: int, 回傳輸入n的所有位數中最大的
	"""
	ans_max = 0  # 準備要傳入recursion的param.
	max_num = 0  # 準備要傳入recursion的param.
	x = 10  # 初始的除數，也是會傳入recursion
	n = int_check(n)  # 如果是負數，乘以-1讓它變正數
	return find_largest_digit_helper(n, ans_max, max_num, x)


def find_largest_digit_helper(n, ans_max, max_num, x):
	if n == 0:  # basic case, 當n == 0時return max_num
		return max_num
	else:
		"""
		用n除以除數x, 得到餘數num，再用餘數num除以除數x的(1/10)，就可以得到位數的值ans
		"""
		num = n % x
		ans = num // (x//10)

		"""
		得到位數的值ans後, 比大小，如果ans比max_num大，把ans的值丟入max_num，並且會傳給下一個recursion
		"""
		if max_num < ans:
			max_num = ans

		"""
		因為n的最右邊的位數已經取出來了，所以n扣掉餘數num，變成new_n
		之後準備要取第2位數(十位數)，把x乘以10，讓它在下一個recursion可以取到第2位數
		"""
		new_n = n - num
		x *= 10
		ans_max = find_largest_digit_helper(new_n, ans_max, max_num, x)
		return ans_max


def int_check(n):
	if n >= 0:
		return n
	else:
		new_n = n * (-1)
		return new_n


if __name__ == '__main__':
	main()
