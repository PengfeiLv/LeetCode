# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 15:35
# @Author  : Lvpengfei


def findTargetSumWays(nums, S):
	# def DFS(start, temp, rem):
	# 	if rem == 0:
	# 		ret.append(temp[:])
	# 		return
	# 	for i in range(start, len(nums)):
	# 		if nums[i] <= rem:
	# 			DFS(i+1, temp+[nums[i]], rem-nums[i])
	#
	# target = (sum(nums) - S)/2
	# if target<0: return 0
	# ret = []
	# nums.sort()
	# DFS(0, [], target)
	# return len(ret)


if __name__ == "__main__":
	nums = [1, 1, 1, 1, 1]
	print(findTargetSumWays(nums, 2))

