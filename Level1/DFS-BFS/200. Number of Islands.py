# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 16:37
# @Author  : Lvpengfei


def numIslands(grid):
	def dfs(x, y):
		if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]):
			return
		if grid[x][y] == '1':
			grid[x][y] = '0'
			dfs(x-1, y)
			dfs(x+1, y)
			dfs(x, y+1)
			dfs(x, y-1)

	cnt = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j]=='1':
				dfs(i, j)
				cnt += 1
	return cnt


if __name__ == '__main__':
	grid = [["1","1","1","1","0"],
	        ["1","1","0","1","0"],
	        ["1","1","0","0","1"],
	        ["0","0","0","1","0"]]
	print(numIslands(grid))

