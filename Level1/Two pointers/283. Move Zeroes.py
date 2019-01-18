# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 17:30
# @Author  : Lvpengfei


#
def moveZeroes(nums):
	zero, value, n = 0, 0, len(nums)
	while value<n:
		if nums[value] == 0:
			zero = value
			while value<n and nums[value]==0:
				value += 1
			if value == n:
				return
			nums[zero], nums[value] = nums[value], nums[zero]
			value = zero
		value += 1

# Time: O(N)  Space: O(1)
def moveZeroes2(nums):
	value, n = 0, len(nums)  # value 记录下一个非零元素应该放的位置
	for i in range(n):
		if nums[i] != 0:
			nums[value] = nums[i]
			value += 1
	for i in range(value, n):
		nums[i] = 0


if __name__ == '__main__':
	nums = [0, 1, 0, 3, 12]
	print(nums)
	moveZeroes2(nums)
	print(nums)

