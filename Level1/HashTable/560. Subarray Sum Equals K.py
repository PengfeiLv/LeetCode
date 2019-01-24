# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 9:52
# @Author  : Lvpengfei


# 方法一：暴力枚举所有可能连续子数组，肯定超时，如何据此优化？？？
def subarraySum1(nums, k):
	cnt = 0
	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			if sum(nums[i:j+1]) == k:
				cnt += 1
	return cnt


# 方法二：由连续求和的累加性
def subarraySum2(nums, k):
	cnt, n = 0, len(nums)
	total = [0]*(n+1)
	for i in range(1, n+1):
		total[i] = total[i-1] + nums[i-1]  # 求出截至到第i个元素的和
	for start in range(n):
		for end in range(start+1, n+1):
			if (total[end] - total[start]) == k:  #  sum(i,j) = sum(0,j) - sum(0,i-1)
				cnt += 1
	return cnt


# 方法三：python 超时
def subarraySum3(nums, k):
	cnt, n = 0, len(nums)
	for i in range(n):
		temp = 0  # 对每一个 start
		for j in range(i, n):
			temp += nums[j]
			if temp == k:
				cnt += 1
	return cnt


# 方法四：hash  Time: O(N) Space: O(N)
def subarraySum4(nums, k):
	sum_cnt = {0:1}
	cnt, csum = 0, 0
	for n in nums:
		csum += n
		cnt += sum_cnt.get(csum-k, 0)
		sum_cnt[csum] = sum_cnt.get(csum, 0) + 1
	return cnt






if __name__ == "__main__":
	nums = [1, 2, 3, 4, 5, 6]
	print(subarraySum1(nums, 7))