# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 17:30
# @Author  : Lvpengfei

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


if __name__ == '__main__':
	nums = [0, 1, 0, 3, 12]
	print(nums)
	moveZeroes(nums)
	print(nums)

