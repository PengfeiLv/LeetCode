# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 11:11
# @Author  : Lvpengfei

# 方法一：组合问题，可以用回溯法
def letterCombinations1(digits):
	def backtracking(start, charMap, temp, ret):
		if len(temp)==len(digits):
			ret.append(temp)
			return
		for c in charMap[digits[start]]:
			backtracking(start+1, charMap, temp+c, ret)

	charMap = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
	           '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
	           '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
	ret = []
	if len(digits)<1: return ret
	backtracking(0, charMap, '', ret)
	return ret


# 方法二：迭代
def letterCombinations2(digits):
	charMap = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
	           '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
	           '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
	ret = ['']
	if len(digits)<1: return []
	for d in digits:
		temp = [s+c for s in ret for c in charMap[d]]
		ret = temp[:]
	return ret



if __name__ == '__main__':
	digits = '23'
	print(letterCombinations1(digits))
	print(letterCombinations2(digits))

