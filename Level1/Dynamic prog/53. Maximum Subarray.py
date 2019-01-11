# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 9:42
# @Author  : Lvpengfei

"""
dp问题的关键在于：
	1.定义子问题的状态
	2.找到状态转移方程
"""

def maxSubArray(nums):
	dp = [nums[0]]*len(nums)
	ret = 0
	for i in range(1, len(nums)):
		dp[i] = max(nums[i], dp[i-1]+nums[i])
		ret = max(ret, dp[i])
	return ret


if __name__ == "__main__":
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print(maxSubArray(nums))
