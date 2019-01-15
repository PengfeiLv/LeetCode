# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 15:29
# @Author  : Lvpengfei

def wordBreak1(s, wordDict):
	lens = set()
	for w in wordDict:
		lens.add(len(w))
	dp = [False]*len(s)
	start = 0
	while start<len(s):
		for l in lens:
			if start+l<=len(s):
				if start==0:
					if s[:l] in wordDict:
						dp[l-1] = True
				else:
					if dp[start-1] and s[start:start+l] in wordDict:
						dp[start+l-1] = True
		start += 1
	return dp[-1]


def wordBreak2(s, wordDict):
	dp = [True] + [False]*len(s)
	for end in range(1, len(s)+1):
		for start in range(0, end):
			if dp[start] and s[start:end] in wordDict:
				dp[end] = True
				break
	return dp[-1]



