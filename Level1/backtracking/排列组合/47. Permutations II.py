# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 10:24
# @Author  : Lvpengfei

"""
包含重复数据的全排列
"""

def permuteUnique(nums):
	def backtracking(nums, used, temp, ret):
		if len(temp)==len(nums):  # 如果仅在这里控制去重 if temp not in ret: ret.append(temp)，这相当于没有剪枝，是完全生长树
			ret.append(temp)
			return
		for i in range(len(nums)):
			if used[i] or i>0 and nums[i]==nums[i-1] and not used[i-1]: continue  # 剪枝，早停止
			used[i] = True
			backtracking(nums, used, temp+[nums[i]], ret)
			used[i] = False

	ret, used = [], [False]*len(nums)
	nums.sort()
	backtracking(nums, used, [], ret)
	return ret


if __name__ == '__main__':
	print(permuteUnique([1, 2, 1]))