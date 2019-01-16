# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 10:10
# @Author  : Lvpengfei


def findDuplicate(nums):
	fast = nums[nums[nums[0]]]  # .next.next  fast走两步
	slow = nums[nums[0]]        # .next       slow走一步
	while fast != slow:
		fast = nums[nums[fast]]
		slow = nums[slow]

	fast = nums[0]  # 这里和链表不一样，只重置fast，slow不用动
	while fast != slow:
		fast = nums[fast]
		slow = nums[slow]
	return fast