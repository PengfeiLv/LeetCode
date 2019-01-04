# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 15:44
# @Author  : Lvpengfei


def isPalindrome1(x):
	if x < 0: return False
	ret, z = 0, x
	while x > 0:
		x, y = divmod(x, 10)
		ret = ret * 10 + y
	return ret == z

def isPalindrome2(x):
	if x < 0 or x > 0 and x % 10 == 0: return False  # 负数或10的倍数，直接为 False
	ret = 0
	while x > ret:  # 只比较一半即可，此时要注意 10的倍数不符合下面的情况
		x, y = divmod(x, 10)
		ret = ret * 10 + y
	return ret == x or ret//10 == x

if __name__ == '__main__':
	x = 131
	print(isPalindrome1(x))
	print(isPalindrome2(x))

