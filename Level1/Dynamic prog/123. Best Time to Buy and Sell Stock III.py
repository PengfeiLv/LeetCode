# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 15:53
# @Author  : Lvpengfei


"""
dp[k, i] 表示最多k次交易，在第i天卖出或不卖出，这k次交易所有利润总和
dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), for j=[0..i-1]
				不卖出      卖出
"""

def maxProfit(prices):
	if len(prices)<2: return 0
	k, n = 3, len(prices)  # k=允许的最多交易次数+1
	dp = [[0]*n for _ in range(k)]
	for i in range(1, k):  # 0次交易时
		mini = prices[0]
		for j in range(1, n):
			mini = min(mini, prices[j]-dp[i-1][j-1])
			dp[i][j] = max(dp[i][j-1], prices[j]-mini)
	return dp[-1][-1]


if __name__ == '__main__':
	prices = [7,6,4,3,1]
	print(maxProfit(prices))
