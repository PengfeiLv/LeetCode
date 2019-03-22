# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 14:55
# @Author  : Lvpengfei


def patition(nums, lo, hi):
	if lo<hi:
		idx = random.randint(lo, hi)
		pivot = nums[idx]
		nums[hi], nums[idx] = nums[idx], nums[hi]

		loc = lo
		for i in range(lo, hi):
			if nums[i]<pivot:
				nums[i], nums[loc] = nums[loc], nums[i]
				loc += 1
		nums[hi], nums[loc] = nums[loc], nums[hi]
		return loc

def quickSort(nums, lo, hi):
	if lo<hi:
		mid = patition(nums, lo, hi)
		quickSort(nums, lo, mid-1)
		quickSort(nums, mid+1, hi)


if __name__ == "__main__":
	quickSort(nums, 0, len(nums)-1)