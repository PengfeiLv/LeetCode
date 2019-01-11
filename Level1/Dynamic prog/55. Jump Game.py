# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 10:06
# @Author  : Lvpengfei


def canJump0(nums):
	maxLen = 0  # 记录到该元素为止，可以到达的最远位置
	for i in range(len(nums)):
		maxLen = max(maxLen, i+nums[i])
		if maxLen<=i: return False  # 如果不能超过该位置，
	return True

"""
回溯法应该是最直接、最符合大脑习惯的解决方案，但是会超时
Time: O(2^N)  Space: O(N)
"""
def canJump1(nums):
	def backtracking(loc):
		if loc==len(nums)-1: return True
		mostJump = min(loc+nums[loc], len(nums)-1)
		for i in range(loc+1, mostJump+1):
			if backtracking(i):
				return True
		return False

	return backtracking(0)


if __name__ == "__main__":
	nums = [3,2,1,0,4]
	print(canJump0(nums))
	print(canJump1(nums))
