# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 11:21
# @Author  : Lvpengfei

# Time: O(mn) Space: O(mn)
def maximalSquare1(matrix):
	if not matrix or not matrix[0]: return 0
	ret, m, n = 0, len(matrix), len(matrix[0])
	dp = [[0]*(n+1) for _ in range(m+1)]
	for i in range(1, m+1):
		for j in range(1, n+1):
			if matrix[i-1][j-1] == '1':
				dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
				ret = max(ret, dp[i][j])
	return ret**2

# Time: O(mn) Space: O(n)
def maximalSquare2(matrix):
	if not matrix or not matrix[0]: return 0
	ret, m, n = 0, len(matrix), len(matrix[0])
	prev, dp = 0, [0]*(n+1)

	for i in range(1, m+1):
		for j in range(1, n+1):
			temp = dp[j]
			if matrix[i-1][j-1] == '1':
				dp[j] = min(prev, min(dp[j], dp[j-1])) + 1
				ret = max(ret, dp[j])
			else:
				dp[j] = 0
			prev = temp
	return ret**2



if __name__ == "__main__":
	matrix = [["1","0","1","0","0"],
	          ["1","0","1","1","1"],
	          ["1","1","1","1","1"],
	          ["1","0","0","1","0"]]
	print(maximalSquare1(matrix))
	print(maximalSquare2(matrix))

