# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 15:35
# @Author  : Lvpengfei


# 2D DP
def findTargetSumWays1(nums, S):
	n = len(nums)
	dp = [[0]*2001 for _ in range(n)]
	dp[0][nums[0]+1000] = 1
	dp[0][-nums[0]+1000] += 1
	for i in range(1, n):
		for psum in range(-1000, 1001):
			if dp[i-1][psum+1000] > 0:
				dp[i][psum+nums[i]+1000] += dp[i-1][psum+1000]
				dp[i][psum-nums[i]+1000] += dp[i-1][psum+1000]
	return 0 if S>1000 else dp[n-1][S+1000]


# 1D DP
def findTargetSumWays2(nums, S):
	n = len(nums)
	dp = [0]*2001
	dp[nums[0]+1000] = 1
	dp[-nums[0]+1000] += 1
	for i in range(1, n):
		post = [0]*2001
		for j in range(2001):
			if dp[j]>0:
				post[j+nums[i]] += dp[j]
				post[j-nums[i]] += dp[j]
		dp = post[:]
	return 0 if S>1000 else dp[S+1000]


# 问题转化
def findTargetSumWays3(nums, S):
	if not nums: return 0
	total = sum(nums)
	if (total+S) % 2 == 1 or total < S: return 0
	target = (total+S) // 2
	dp = [1] + [0]*target
	for n in nums:
		for i in range(target, n-1, -1):
			dp[i] += dp[i-n]
	return dp[-1]


if __name__ == "__main__":
	nums = [1, 1, 1, 1, 1]
	print(findTargetSumWays1(nums, 3))
	print(findTargetSumWays2(nums, 3))
	print(findTargetSumWays3(nums, 3))



