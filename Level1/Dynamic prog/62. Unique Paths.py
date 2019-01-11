# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 11:32
# @Author  : Lvpengfei


def uniquePaths(m, n):
	dp = [1]*(m)
	for _ in range(n-1):
		for i in range(1, m):
			dp[i] = dp[i-1] + dp[i]
	return dp[-1]


if __name__ == "__main__":
	print(uniquePaths(7, 3))