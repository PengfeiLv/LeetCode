# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 14:10
# @Author  : Lvpengfei

# Boyer-Moore Majority Vote algorithm
# Time: O(N)  Space: O(1)
def majorityElement(nums):
	candidate = 0
	count = 0
	for n in nums:
		if count == 0:
			candidate = n
		count += 1 if n == candidate else -1
	return candidate