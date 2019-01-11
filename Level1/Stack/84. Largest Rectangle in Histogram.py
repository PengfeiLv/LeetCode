# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 17:08
# @Author  : Lvpengfei

"""
代码虽然简单，但是为何用单调栈？如何用？递增栈还是递减栈？
"""
def largestRectangleArea(heights):
	ret, stack = 0, [-1]
	heights.append(0)
	for i in range(len(heights)):
		while stack and heights[i]<heights[stack[-1]]:
			h = heights[stack.pop()]
			w = i - stack[-1] - 1
			ret = max(ret, h*w)
		stack.append(i)
	return ret