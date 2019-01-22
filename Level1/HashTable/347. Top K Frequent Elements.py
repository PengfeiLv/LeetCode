# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 12:51
# @Author  : Lvpengfei


def topKFrequent(nums, k):
	freq = {}
	for n in nums:
		freq[n] = freq.get(n, 0) + 1
	ret = sorted(freq.items(), key=lambda x:x[1], reverse=True)[:k]
	return [x[0] for x in ret]


if __name__ == '__main__':
	nums = [1, 1, 1, 2, 2, 3, 3]
	k = 2
	print(topKFrequent(nums, k))
