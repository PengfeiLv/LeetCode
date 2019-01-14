# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 15:28
# @Author  : Lvpengfei

# dp
def maxProfit1(prices):
	if not prices or len(prices)<2: return 0
	profits = [0]*len(prices)
	for i in range(1, len(prices)):
		profits[i] = prices[i] - prices[i-1]
	ret = 0
	for p in profits:
		ret += p if p>0 else 0
	return ret

def maxProfit2(prices):
	if not prices or len(prices)<2: return 0
	ret, buy = 0, prices[0]
	for p in prices[1:]:
		if p>buy:
			ret += p - buy
		buy = p
	return ret

def maxProfit3(prices):
	if not prices or len(prices)<2: return 0
	ret = 0
	for i in range(1, len(prices)):
		profit = prices[i] - prices[i-1]
		ret += profit if profit>0 else 0
	return ret





