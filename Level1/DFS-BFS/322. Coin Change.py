# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 9:59
# @Author  : Lvpengfei

"""
这和 Combination Sum 思想类似
"""
def coinChange1(coins, amount):
	def BFS():
		if amount == 0: return 0
		curr = {0}
		visited = [1] + [0]*amount
		level = 0
		while curr:
			level += 1
			temp = set()
			for rem in curr:
				for c in coins:
					val = rem + c  # 从小到大，不断加
					if val == amount:
						return level
					if val > amount:
						break
					elif not visited[val]:
						visited[val] = 1
						temp.add(val)
			curr = temp
		return -1

	coins.sort()
	return BFS()


def coinChange2(coins, amount):
	def BFS():
		if amount == 0: return 0
		rem = {amount}
		had = {amount}  # 同一个值只需出现一次
		level = 0
		while rem:
			level += 1
			temp = set()
			for r in rem:
				for c in coins:
					newrem = r - c
					if newrem == 0:
						return level
					if newrem < 0:
						break
					elif newrem not in had:
						had.add(newrem)
						temp.add(newrem)
			rem = temp
		return -1

	coins.sort()
	return BFS()


if __name__ == '__main__':
	coins = [1, 2, 5]
	amount = 11
	print(coinChange1(coins, amount))
