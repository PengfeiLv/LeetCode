# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 16:22
# @Author  : Lvpengfei

"""
一题多解，每种思路都要熟悉
"""

# Vertical scanning
def longestCommonPrefix1(strs):
	if not strs: return ''
	for i, c in enumerate(strs[0]):
		for s in strs:
			if i >= len(s) or s[i] != c:
				return strs[0][:i]
	return strs[0]

# Horizontal scanningl
def longestCommonPrefix2(strs):
	if not strs: return ''
	prefix = strs[0]
	for i in range(1, len(strs)):
		j = 0
		while j < min(len(prefix), len(strs[i])) and strs[i][j] == prefix[j]:
			j += 1
		prefix = prefix[:j]
	return prefix

# Divide and conquer
def longestCommonPrefix3(strs):

	pass

# Prefix trie：前缀树

if __name__ == '__main__':
	strs = ['leet', 'leetcode', 'leets', 'lee']
	print(longestCommonPrefix1(strs))
	print(longestCommonPrefix2(strs))