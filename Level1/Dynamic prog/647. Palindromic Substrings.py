# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 14:22
# @Author  : Lvpengfei


# DP: O(N^2)
def countSubstrings1(s):
	ret, n = 0, len(s)
	dp = [[False]*n for _ in range(n)]  # False/True 比用 0/1 更快
	for i in range(n-1, -1, -1):
		for j in range(i, n):
			if j==i:
				dp[i][j] = True
			elif j==i+1:
				dp[i][j] = (s[i]==s[j])
			else:
				dp[i][j] = (s[i]==s[j] and dp[i+1][j-1])
			if dp[i][j]:
				ret += 1
	return ret


# Manacher: O(N)
def countSubstrings2(s):


	pass


if __name__ == '__main__':
	print(countSubstrings1('aaa'))