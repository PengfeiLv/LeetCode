# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 11:35
# @Author  : Lvpengfei

def maxProfit(k, prices):
	if len(prices) < 2: return 0
	n = len(prices)
	if 2 * k >= n:
		ret = 0
		for i in range(1, n):
			if prices[i] > prices[i - 1]:
				ret += prices[i] - prices[i - 1]
		return ret

	dp = [[0] * n for _ in range(k + 1)]
	for i in range(1, k + 1):
		temp = -prices[0]
		for j in range(1, n):
			dp[i][j] = max(dp[i][j - 1], temp + prices[j])
			temp = max(temp, dp[i - 1][j - 1] - prices[j])
	return dp[-1][-1]