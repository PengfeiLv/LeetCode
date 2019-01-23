# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 17:01
# @Author  : Lvpengfei


def canPartition1(nums):
	total = sum(nums)
	if total % 2 != 0: return False
	target = int(total // 2)
	had = {0}  # 不包含任何元素时，和为0
	for n in nums:
		sum_with_n = []
		for i in had:
			if i+n == target: return True
			if i+n < target:
				sum_with_n.append(i+n)  # 到目前为止包含 n 的子集的和
		had.update(sum_with_n)  # 并集
	return False


# 方法二：2维 无优化 DP数组
def canPartition2(nums):
	target = sum(nums)
	if (target & 1) == 1: return False
	target //= 2
	n = len(nums) + 1
	dp = [[False]*(target+1) for _ in range(n)]  # dp[i][j]表示使用前 i 个元素，是否能组合出 j
	dp[0][0] = True
	for i in range(1, target+1):
		dp[0][i] = False
	for i in range(1, n):
		dp[i][0] = True
	for i in range(1, n):
		for j in range(1, target+1):
			dp[i][j] = dp[i-1][j]  # 如果不 pick 第i个数
			if j >= nums[i-1]:  # 如果第 i 个数小于 j 才可能被 pick
				dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
	return dp[-1][-1]


# 方法三：1维 优化 DP数组
def canPartition3(nums):
	target = sum(nums)
	if (target & 1) == 1: return False
	target //= 2
	dp = [True] + [False]*target
	for n in nums:
		for i in range(target, n-1, -1):
			dp[i] = dp[i] or dp[i-n]
	return dp[-1]


# 方法四：位操作
def canPartition4(nums):
	total, bits = 0, 1
	for n in nums:
		total += n
		bits |= bits << n
	return (total % 2 == 0) and (bits >> (total // 2)) & 1 == 1
#      只有当 total为偶数  且  可以组成 total // 2 时，才返回 True


if __name__ == '__main__':
	nums = [1, 5, 5, 11]
	print(canPartition1(nums))
	print(canPartition2(nums))
	print(canPartition3(nums))
	print(canPartition4(nums))



