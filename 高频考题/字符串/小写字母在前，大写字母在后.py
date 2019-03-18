# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:10
# @Author  : Lvpengfei


"""
描述：将字符串中所有小写字母放在大写字母前边，且小写字母相对顺序不能改变，大写字母同样
要求：O(1) Space
"""


def lowerBeforeUpper():
	"""
	:param s: 用字符数组表示的字符串
	:return:
	"""
	s = list(input("input str:..\n"))
	n = len(s)
	j =  0
	for i in range(n-1, 0, -1):
		if s[i].islower():
			j = i
			while s[j].islower() and j>=1:
				j -= 1
			if j==0 and s[j].islower():
				break
			if s[j].isupper():
				char = s[j]
				for k in range(j, i):
					s[k] = s[k+1]
				s[i] = char
	print(s)
	return


if __name__ == "__main__":
	lowerBeforeUpper()