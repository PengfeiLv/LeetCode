# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 14:48
# @Author  : Lvpengfei

def numJewelsInStones(J, S):
	jj = set(J)
	ret = 0
	for c in S:
		if c in jj:
			ret += 1
	return ret