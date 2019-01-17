# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 16:00
# @Author  : Lvpengfei

import math

# 方法一：动态规划，python会超时
def numSquares1(n):
	if n<=0: return 0
	dp = [0] + [float('inf')]*n
	for i in range(1, n+1):
		for j in range(1, int(math.sqrt(i))+1):
			dp[i] = min(dp[i], dp[i-j**2]+1)
	return dp[-1]

# 方法二：数学法，答案只能是：1，2，3，4中的一个
def numSquares2(n):
	def is_square(n):
		return n==((int)(math.sqrt(n))**2)
	# 1
	if is_square(n): return 1
	# 4 if and only if n= 4^k*(8*m + 7)
	while (n & 3) == 0:
		n >>= 2
	if (n & 7) == 7: return 4
	# 2
	sqrt_n = int(math.sqrt(n))
	for i in range(1, sqrt_n+1):
		if is_square(n- i**2): return 2
	# 3
	return 3

# 方法三：BFS
def numSquares3(n):
	squares = [i*i for i in range(1, n+1) if i*i<=n]
	level, toCheck = 0, {n}
	while toCheck:
		level += 1
		curr = set()
		for i in toCheck:
			for j in squares:
				if j == i: return level
				elif j < i: curr.add(i-j)
				else: break
			toCheck = curr


if __name__ == '__main__':
	print(numSquares2(12129087))
	print(numSquares3(12129087))

