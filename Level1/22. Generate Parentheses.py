# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 10:17
# @Author  : Lvpengfei


def generateParenthesis(n):
	if n < 1: return
	if n == 1: return ["()"]

	ret = [['(', ')']]
	for i in range(n - 1):
		left = []
		for s in ret:
			for j in range(1, len(s)):
				s.insert(j, '(')
				left.append(s.copy())
				s.pop(j)


		right = []
		for s in left:
			for j in range(1, len(s)):
				s.insert(j, ')')
				right.append(s.copy())
				s.pop(j)

		ret = right

	res = []
	for ls in ret:
		s = ''
		for c in ls:
			s += c
		res.append(s)
	ret = set(res)

	non = set()
	for s in ret:
		num = 0
		for c in s:
			if num < 0:
				non.add(s)
				break
			if c=='(':
				num += 1
			else:
				num -= 1

	return list(ret - non)

def catalan(n):
	if n < 2:
		return 1
	else:
		return int(catalan(n - 1)*(4*n-2)/(n+1))


if __name__ == '__main__':
	# ret = generateParenthesis(6)
	# for s in ret:
	# 	print(s)
	for i in range(10):
		print(catalan(i))