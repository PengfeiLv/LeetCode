# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 15:30
# @Author  : Lvpengfei

from collections import defaultdict

def groupAnagrams(strs):
	had = defaultdict(list)
	for s in strs:
		had[tuple(sorted(s))].append(s)
	return list(had.values())


if __name__ == "__main__":
	strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
	print(groupAnagrams(strs))