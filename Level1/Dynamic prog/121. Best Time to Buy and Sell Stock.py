# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 14:41
# @Author  : Lvpengfei

# 动态规划
def maxProfit1(prices):
	if not prices or len(prices)<2: return 0
	profits = [0]*len(prices)
	for i in range(1, len(prices)):
		profits[i] = prices[i] - prices[i-1]
	dp = [0]*len(profits)
	maxi = 0
	for i in range(1, len(dp)):
		dp[i] = max(dp[i-1]+profits[i], profits[i])
		maxi = max(maxi, dp[i])
	return maxi

# one-pass
def maxProfit2(prices):
	miniPrice = float('inf')
	maxi = 0
	for p in prices:
		miniPrice = min(p, miniPrice)
		maxi = max(maxi, p-miniPrice)
	return maxi

if __name__ == "__main__":
	prices = [1,2]
	print(maxProfit1(prices))
	print(maxProfit2(prices))



