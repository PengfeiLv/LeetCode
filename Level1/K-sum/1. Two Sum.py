# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 10:24
# @Author  : Lvpengfei


"""
one-pass hashTable:
	两种实现细节：
	1.存 nums[i]，用 target-nums[i]查
	2.存 target-nums[i]，用 nums[i]查
"""

def twoSum1(nums, target):
		hashMap = {}
		for i in range(len(nums)):
			res = target-nums[i]
			if res in hashMap:
				return [hashMap[res], i]
			hashMap[nums[i]] = i


def twoSum2(nums, target):
	hashMap = {}
	for i in range(len(nums)):
		res = target - nums[i]
		if nums[i] in hashMap:
			return [hashMap[nums[i]], i]
		hashMap[res] = i


if __name__ == '__main__':
	print(twoSum1([0,1,2,3,4,5], 9))
	print(twoSum2([0,1,2,3,4,5], 9))