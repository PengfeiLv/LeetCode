# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 10:43
# @Author  : Lvpengfei

import random

# BFPRT: Time: O(N)  Space: O(1)
def findKthLargest(nums, k):
	def partition(left, right, pivot_index):
		pivot = nums[pivot_index]  #
		nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
		loc = left
		for i in range(left, right):
			if nums[i]<pivot:
				nums[i], nums[loc] = nums[loc], nums[i]
				loc += 1
		nums[loc], nums[right] = nums[right], nums[loc]
		return loc

	def select(left, right, k_smallest):
		if left==right: return nums[left]
		pivot_index = random.randint(left, right)
		pivot_loc = partition(left, right, pivot_index)
		if pivot_loc==k_smallest:
			return nums[pivot_loc]
		elif pivot_loc<k_smallest:
			return select(pivot_loc+1, right, k_smallest)
		else:
			return select(left, pivot_loc-1, k_smallest)

	return select(0, len(nums)-1, len(nums)-k)


if __name__ == "__main__":
	nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
	k = 4
	print(findKthLargest(nums, k))
	print(sorted(nums, reverse=True))
