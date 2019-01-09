# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 10:24
# @Author  : Lvpengfei


# 方案一：动态规划， Time: O(n^2)  Space：O(n^2) 也可优化到 O(n)
def longestPalindrome1(s):
	maxi, ret, n = 0, '', len(s)
	dp = [[0]*n for _ in range(n)]
	for i in range(n-1, -1, -1):
		for j in range(i, n):
			if i == j:
				dp[i][j] = 1
			elif j - i == 1:
				dp[i][j] = 2 if s[i] == s[j] else 0
			else:
				dp[i][j] = (2+dp[i+1][j-1]) if dp[i+1][j-1] and s[i] == s[j] else 0
			if dp[i][j] > maxi:
				maxi = dp[i][j]
				ret = s[i:j+1]
	return ret


# 方案二：按回文中心扩展， Time: O(n^2)  Space：O(1)
def longestPalindrome2(s):
	def expand(left, r, s, start, maxi):
		while left >= 0 and r < n and s[left] == s[r]:
			left -= 1
			r += 1
		if maxi < r - left - 1:
			start = left + 1
			maxi = r - left - 1
		return start, maxi

	start, maxi = 0, 0
	n = len(s)
	if n < 2: return s
	for i in range(n-1):
		start, maxi = expand(i, i, s, start, maxi)
		start, maxi = expand(i, i + 1, s, start, maxi)
	return s[start:start+maxi]


# 方案三：最优解 Manacher，Time: O(n)  Space：O(1)
def longestPalindrome3(s):

	pass


if __name__ == '__main__':
	s = 'as'
	print(longestPalindrome2(s))