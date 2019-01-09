# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 9:54
# @Author  : Lvpengfei

"""
全排列，用回溯法
46题给定数据 nums中是不包含重复数据的
"""

def permute(nums):
	def backtracking(nums, temp, ret):
		if len(temp)==len(nums):
			ret.append(temp)
			return
		for i in range(len(nums)):
			if nums[i] in temp:
				continue
			backtracking(nums, temp+[nums[i]], ret)

	ret = []
	backtracking(nums, [], ret)
	return ret


if __name__ == '__main__':
	print(permute([1, 2, 3, 4, 5]))