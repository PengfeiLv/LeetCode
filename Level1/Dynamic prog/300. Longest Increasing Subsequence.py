# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 11:31
# @Author  : Lvpengfei


# 方法一： Time: O(N^2)
def lengthOfLIS1(nums):
	if not nums: return 0
	ret, n = 1, len(nums)
	dp = [1]*n
	for i in range(1, n):
		maxi = 0
		for j in range(i, -1, -1):
			if nums[j]<nums[i]:
				maxi = max(maxi, dp[j])
		dp[i] = maxi + 1
		ret = max(ret, dp[i])
	return ret


# 方法二： Time: O(NlogN)
def lengthOfLIS2(nums):
	size, n = 0, len(nums)
	dp = [0]*n  # dp存放的是到目前为止，各元素都尽可能小的最长递增序列
	for x in nums:
		i, j = 0, size
		while i != j:
			m = (i + j) // 2
			if dp[m] < x:
				i = m + 1
			else:
				j = m
		dp[i] = x
		size = max(i+1, size)
	return size

# 方法二的解释版本：
import bisect
def lengthOfLIS3(nums):
	size, n = 0, len(nums)
	dp = [-float('inf')]*n
	for x in nums:
		if not dp or x>dp[size-1]: # 如果x大于dp最后一个元素，则直接追加
			dp[size] = x
			size += 1
		else:
			i = bisect.bisect_left(dp, x, 0, size)  # 找到 x再dp中应该处的位置，替换掉
			dp[i] = x
	return size

if __name__ == '__main__':
	nums = [10,9,2,5,3,7,101,18]
	print(lengthOfLIS1(nums))
	print(lengthOfLIS2(nums))
	print(lengthOfLIS3(nums))
