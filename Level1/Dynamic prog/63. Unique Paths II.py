# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 14:05
# @Author  : Lvpengfei


def uniquePathsWithObstacles(obstacleGrid):
	m, n = len(obstacleGrid), len(obstacleGrid[0])
	if obstacleGrid[0][0]: return 0
	obstacleGrid[0][0] = 1
	for i in range(1, n):
		obstacleGrid[0][i] = int(obstacleGrid[0][i]==0 and obstacleGrid[0][i-1]==1)
	for i in range(1, m):
		obstacleGrid[i][0] = int(obstacleGrid[i][0]==0 and obstacleGrid[i-1][0]==1)
	for i in range(1, m):
		for j in range(1, n):
			if obstacleGrid[i][j]:
				obstacleGrid[i][j] = 0
			else:
				obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
	return obstacleGrid[-1][-1]