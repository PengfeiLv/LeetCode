# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 17:08
# @Author  : Lvpengfei

"""
栈的应用之一：括号匹配
"""

def isValid(s):
	cmap = {')': '(', ']': '[', '}': '{'}
	stack = []
	for c in s:
		if c in cmap:
			if not stack or stack.pop()!=cmap[c]:
				return False
		else:
			stack.append(c)
	return not stack  # 任何对象都可做 boolean 判断


if __name__ == '__main__':
	s = '{[]}'
	print(isValid(s))
