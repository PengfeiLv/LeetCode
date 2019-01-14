# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 11:21
# @Author  : Lvpengfei


def maximalRectangle(matrix):
	if not matrix or not matrix[0]: return 0
	ret, n = 0, len(matrix[0])
	heights = [0]*(n+1)
	for row in matrix:
		stack = [-1]
		# 统计高度
		for i in range(n):
			heights[i] = (heights[i]+1) if row[i]=='1' else 0
		# 算最大矩形面积
		for i in range(n+1):
			while heights[i]<heights[stack[-1]]:
				h = heights[stack.pop()]
				w = i - stack[-1] - 1
				ret = max(ret, h*w)
			stack.append(i)
	return ret


if __name__ == '__main__':
	matrix = [["1","0","1","0","0"],
			  ["1","0","1","1","1"],
			  ["1","1","1","1","1"],
			  ["1","0","0","1","0"]]
	print(maximalRectangle(matrix))




