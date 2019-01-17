# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 14:45
# @Author  : Lvpengfei


def productExceptSelf(nums):
	ret = [1]*len(nums)
	for i in range(1, len(nums)):  # 第一轮，ret[i]存放 i以左的乘积
		ret[i] = ret[i-1]*nums[i-1]

	mul = 1
	for i in range(len(nums)-1, -1, -1):  # 第二轮
		ret[i] = ret[i]*mul
		mul *= nums[i]  # mul记录 i以右的乘积
	return ret


if __name__ == '__main__':
	nums = [1, 2, 3, 4]
	print(productExceptSelf(nums))