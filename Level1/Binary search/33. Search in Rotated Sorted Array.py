# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 14:11
# @Author  : Lvpengfei


def search1(nums, target):
	lo, hi = 0, len(nums) - 1
	while lo < hi:  # break until lo==hi
		mid = (lo + hi) // 2
		if nums[mid] < nums[hi]:
			hi = mid
		else:
			lo = mid + 1
	# after while above, get smallest=nums[lo]=num[hi]
	rot = lo  # 记录偏移量
	lo, hi = 0, len(nums) - 1
	while lo <= hi:  # 注意这里是 <=
		mid = (lo + hi) // 2
		realmid = (mid + rot) % len(nums)
		if nums[realmid] == target:
			return realmid
		if nums[realmid] > target:
			hi = mid - 1
		else:
			lo = mid + 1
	return -1

# 改进的二分搜索
def search2(nums, target):
	lo, hi = 0, len(nums) - 1
	while lo < hi:
		mid = (lo + hi) // 2
		if nums[mid] == target: return mid
		if nums[mid] > nums[hi]:
			if nums[lo] <= target < nums[mid]:
				hi = mid -1
			else:
				lo = mid + 1
		else:
			if nums[mid] < target <= nums[hi]:
				lo = mid + 1
			else:
				hi = mid - 1
	return lo if nums[lo]==target else -1


if __name__ == "__main__":
	nums = [5, 6, 0, 2, 3]
	target = 3
	print(search1(nums, target))
	print(search2(nums, target))


