# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 10:15
# @Author  : Lvpengfei


def canFinish(numCourses, prerequisites):
	def dfs(i):
		if visited[i] == -1: return False  # 如果遇到了本次深搜过程中已经访问过的结点，说明有环
		if visited[i] == 1: return True  # 如果已经得知该路径无环，直接返回True
		visited[i] = -1  # 标记该结点已经访问过
		for j in graph[i]:
			if not dfs(j):
				return False
		visited[i] = 1  # 都没有环，则次路径无环，标记为1，下次再遇到该结点，可直接知道此路径无环
		return True

	graph = [[] for _ in range(numCourses)]
	visited = [0]*numCourses
	for x, y in prerequisites:  # 构造邻接表
		graph[x].append(y)

	for i in range(numCourses):
		if not dfs(i): return False
	return True