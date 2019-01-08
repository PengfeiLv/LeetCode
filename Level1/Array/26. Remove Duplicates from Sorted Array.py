# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 15:57
# @Author  : Lvpengfei


def removeDuplicates(nums):
	if not nums: return 0
	j = 0  # j+1 记录unique值的个数
	for i in range(1, len(nums)):
		if nums[i]!=nums[j]:
			nums[j+1] = nums[i]
			j += 1
	return j+1


if __name__ == '__main__':
	nums = [1,1,1,2,2,3,3,4,4,5]
	print(nums[:removeDuplicates(nums)])