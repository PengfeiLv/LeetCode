# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 15:00
# @Author  : Lvpengfei


def minPathSum(grid):
	m, n = len(grid), len(grid[0])
	for i in range(1, n):
		grid[0][i] += grid[0][i-1]
	for i in range(1, m):
		grid[i][0] += grid[i-1][0]
	for i in range(1, m):
		for j in range(1, n):
			grid[i][j] += min(grid[i][j-1], grid[i-1][j])
	return grid[-1][-1]
