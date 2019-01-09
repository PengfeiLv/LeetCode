# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 17:23
# @Author  : Lvpengfei



def generateParenthesis(n):

	def backtracking(left, right, temp, ret):
		if len(temp) == 2 * n:
			ret.append(temp)
			return
		if left < n:
			backtracking(left + 1, right, temp + ['('], ret)
		if right < left:
			backtracking(left, right + 1, temp + [')'], ret)

	ret = []
	backtracking(0, 0, [], ret)
	return ret


if __name__ == '__main__':
	print(generateParenthesis(3))