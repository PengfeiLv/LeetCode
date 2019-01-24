# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 15:35
# @Author  : Lvpengfei

ret = 0
def findTargetSumWays(nums, S):
	def calculate(start, csum):
		global ret
		if start==len(nums):
			if csum == S:
				ret += 1
		else:
			calculate(start+1, csum+nums[start])
			calculate(start+1, csum-nums[start])
	calculate(0, 0)
	return ret


if __name__ == "__main__":
	nums = [1, 1, 1, 1, 1]
	print(findTargetSumWays(nums, 3))

