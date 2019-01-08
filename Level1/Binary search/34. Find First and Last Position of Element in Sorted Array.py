# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 15:22
# @Author  : Lvpengfei

"""
如果target 存在 nums中时：
找target在有序数组nums中第一次出现的位置，等价于 bisect.bisect_left
找target在有序数组nums中最后一次出现的位置，等价于 bisect.bisect_right-1
"""
import bisect

def searchRange(nums, target):
	def bisect_left(nums, target):
		lo, hi = 0, len(nums)-1
		while lo < hi:
			mid = (lo + hi) // 2
			if nums[mid] < target: lo = mid + 1
			else: hi = mid
		return lo if nums[lo]==target else -1

	def bisect_right(nums, target):
		lo, hi = 0, len(nums)-1
		while lo < hi:
			mid = (lo + hi) // 2 + 1
			if target < nums[mid]: hi = mid -1
			else: lo = mid
		return lo if nums[lo]==target else -1

	if not nums: return [-1, -1]
	return [bisect_left(nums, target), bisect_right(nums, target)]


if __name__ == '__main__':
	nums = [5,7,7,8,8,10]
	target = 8
	print(searchRange(nums, target))
	print([bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)-1])


