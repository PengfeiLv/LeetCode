# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 9:50
# @Author  : Lvpengfei

"""
如何求比当前排列大的下一个排列（最小排列）？
如：          1,5,8,4,7,6,5,3,1
下一排列为：   1,5,8,5,1,3,4,6,7

"""


def nextPermutation(nums):
	loc = -1
	for i in range(len(nums)-1, 0, -1):  # 从右向左，找一个逆序对 4,7
		if nums[i-1]<nums[i]:
			loc = i - 1  # loc记录 4的位置
			break
	if loc==-1:  # 如果不存在逆序对，即当前排列为 降序，如 5,4,3,2,1
		nums.reversed()  # 直接返回最小排列， 1,2,3,4,5
		return
	for i in range(len(nums)-1, loc, -1):  # 从右向左，找比 nums[loc]大的最小数
		if nums[i]>nums[loc]:
			nums[loc], nums[i] = nums[i], nums[loc]  # 交换
			break
	nums[loc+1:] = nums[:loc:-1]  # 交换后，将loc后面重新排序成升序


if __name__ == '__main__':
	# nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
	nums = [1, 5, 1]

	nextPermutation(nums)
	print(nums)

	pass