# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 13:59
# @Author  : Lvpengfei


def searchInsert(nums, target):
	lo, hi = 0, len(nums)
	while lo < hi:
		mid = (lo + hi) // 2
		if nums[mid] < target:
			lo = mid + 1
		else:
			hi = mid
	return lo


if __name__ == "__main__":
	nums = [1, 2, 3, 4, 5]
	target = 5
	print(searchInsert(nums, target))