# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 16:00
# @Author  : Lvpengfei

""" 一步一步分析，最终推出最优解的形式 """

"""
On day[i], we can choose:    cooldown, buy, or sell:

1.Under what condition we can choose to cooldown on day[i]?
	there is not requirement. We can choose to cooldown on anyday.
2.Under what condition we can choose to buy a stock on day[i]?
	The answer is we do not own any stock at end of day[i-2] because there is one day cooldown requirement.
3.Under what condition we can choose to sell a stock on day[i]?
	The answer is we must own a stock at the end of day[i-1].
	
own[i] = max(own[i-1], not_own[i-2]-prices[i])
not_own[i] = max(not_own[i-1], own[i-1]+prices[i])
"""
def maxProfit(prices):
	if len(prices)<2:
		return 0
	ret = 0
	own_last = -prices[0]
	not_own_last2 = 0
	not_own_last = 0
	for p in prices[1:]:
		own = max(own_last, not_own_last2 - p)
		not_own = max(not_own_last, own_last + p)

		ret = max(ret, max(own, not_own))

		own_last = own
		not_own_last2 = not_own_last
		not_own_last = not_own
	return ret


if __name__ == '__main__':
	nums = [1,2,4,0,1,2]
	print(maxProfit(nums))
