# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 16:09
# @Author  : Lvpengfei


def combine(n, k):
	def backtracking(start, temp):
		if len(temp)==k:
			ret.append(temp[:])
			return
		for i in range(start, n+1):
			backtracking(i+1, temp+[i])

	ret = []
	backtracking(1, [])
	return ret

if __name__ == "__main__":
	print(combine(4,2))