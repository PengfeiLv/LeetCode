# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 16:33
# @Author  : Lvpengfei

# 方法一：HashTable
def singleNumber1(nums):
	had = {}
	for n in nums:
		if n not in had:
			had[n] = 1
		else:
			had.pop(n)
	return had.popitem()[0]

# 方法二：数学计算  2*(a+b+c+d)-(a+a+b+b+c+c+d)=d
def singleNumber2(nums):
	return 2*(sum(set(nums)))-sum(nums)

"""
位操作：XOR 异或
	根据异或运算的性质，恰好可以找出只出现一次的数
"""
def singleNumber3(nums):
	b = 0  # 由性质 0 XOR b = b，所以应初始化为 0
	for n in nums:
		b ^= n
	return b


if __name__ == "__main__":

	nums = [4,1,2,1,2]
	print(singleNumber1(nums))
	print(singleNumber2(nums))
	print(singleNumber3(nums))