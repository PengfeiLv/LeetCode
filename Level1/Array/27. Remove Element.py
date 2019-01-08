# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 16:31
# @Author  : Lvpengfei

# 和26题一样的思路
def removeElement(nums, val):
	if not nums: return 0
	j = 0  # j+1 记录unique值的个数
	for i in range(len(nums)):
		if nums[i]!=val:
			nums[j] = nums[i]
			j += 1
	return j


if __name__ == '__main__':
	nums = [3, 4, 5, 2, 2, 2]
	val = 2
	print(nums[:removeElement(nums, val)])
