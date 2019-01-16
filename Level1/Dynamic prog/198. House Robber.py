# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 15:41
# @Author  : Lvpengfei

# Space: O(N)
def rob(nums):
	if not nums: return 0
	dp = [0]*len(nums)
	for i in range(len(nums)):
		if i == 0:
			dp[0] = nums[0]
		elif i == 1:
			dp[1] = max(nums[0], nums[1])
		else:
			dp[i] = max(dp[i-1], dp[i-2]+nums[i])
	return dp[-1]

# Space: O(1)
def rob1(nums):
	if not nums: return 0
	if len(nums)<3: return max(nums)

	first = nums[0]
	second = max(nums[0], nums[1])
	for n in nums[2:]:
		temp = first
		first = second
		second = max(second, temp+n)
	return second


if __name__ == '__main__':
	nums= [1,2,3,4]
	print(rob(nums))
	print(rob1(nums))