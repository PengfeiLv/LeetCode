# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 11:14
# @Author  : Lvpengfei


def merge(intervals):
	intervals.sort(key=lambda x:x.start)
	ret = []
	for inter in intervals:
		if not ret or inter.start>ret[-1].end:
			ret.append(inter)
		else:
			ret[-1].end = max(ret[-1].end, inter.end)
	return ret