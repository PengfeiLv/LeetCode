# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 15:40
# @Author  : Lvpengfei

# 荷兰国旗问题：快排思想
def sortColors(nums):
	lo, hi = -1, len(nums)
	i = 0
	while i<hi:
		if nums[i]<1:
			nums[i], nums[lo+1] = nums[lo+1], nums[i]
			lo += 1
			i += 1
		elif nums[i]>1:
			nums[i], nums[hi-1] = nums[hi-1], nums[i]
			hi -= 1
		else:
			i += 1


