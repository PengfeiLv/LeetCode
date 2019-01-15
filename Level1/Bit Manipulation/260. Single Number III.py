# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 15:07
# @Author  : Lvpengfei


def singleNumber(nums):
	diff, a, b = 0, 0, 0
	for n in nums:
		diff ^= n
	diff &= -diff
	for n in nums:
		if n & diff == 0:
			a ^= n
		else:
			b ^= n
	return a, b


if __name__ == "__main__":
	nums = [1, 2, 1, 2, 3, 4]
	print(singleNumber(nums))
