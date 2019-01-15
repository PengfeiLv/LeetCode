# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 16:25
# @Author  : Lvpengfei

# 超时了
def wordBreak(s, wordDict):
	def backtracking(start, temp):
		if start==len(temp) and temp[:-1] not in ret:
			ret.append(temp[:-1])
			return
		for w in wordDict:
			off = len(w)
			if w==temp[start:start+off]:
				loc = start+off
				ss = temp[:loc]+" "+temp[loc:]
				backtracking(loc+1,ss)
		return

	ret = []
	backtracking(0, s)
	return ret


if __name__ == '__main__':
	s = "pineapplepenapple"
	wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
	for w in wordBreak(s, wordDict):
		print(w)