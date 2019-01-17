# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 15:41
# @Author  : Lvpengfei


def searchMatrix(matrix, target):
	if not matrix: return False
	m, n = len(matrix), len(matrix[0])
	x, y = 0, n-1
	while x<m and y>=0:
		if matrix[x][y] == target:
			return True
		elif matrix[x][y] > target:
			y -= 1
		else:
			x += 1
	return False


if __name__ == '__main__':
	matrix = [[1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
	target = 20
	print(searchMatrix(matrix, target))