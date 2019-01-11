# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 15:18
# @Author  : Lvpengfei



# 方法一：dp with Time O(N) and Space O(N)
def climbStairs1(n):
	if n<3: return n
	ret = [0, 1, 2]
	for _ in range(3, n + 1):
		ret.append(ret[-1]+ret[-2])
	return ret[-1]

# 方法二：dp with Time O(N) and Space O(1)
def climbStairs2(n):
	if n<3: return n
	first, second = 1, 2
	for i in range(3, n+1):
		temp = first + second
		first, second = second, temp
	return second

# 还有两种 Time O(log(N))的方法
