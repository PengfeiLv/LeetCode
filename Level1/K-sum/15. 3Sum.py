# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 10:54
# @Author  : Lvpengfei

"""
two-pointer
"""

def threeSum1(nums):
	ret = []
	nums.sort()  # 控制去重
	for i in range(len(nums)):
		if nums[i] > 0: break  # 3个正数的和一定大于0，早停止，提高速度
		if i>0 and nums[i]==nums[i-1]: continue  # 控制去重
		l, r = i+1, len(nums)-1
		while l<r:
			csum = nums[i]+nums[l]+nums[r]
			if csum == 0:
				ret.append([nums[i], nums[l], nums[r]])
				l += 1
				while l<r and nums[l]==nums[l-1]:  # 控制去重
					l += 1
			elif csum > 0:
				r -= 1
			else:
				l += 1
	return ret


from bisect import bisect_left, bisect_right

def threeSum2(nums):
	""" 既然要排序，就充分利用有序性"""
	pass


if __name__ == '__main__':
	nums = [-1, 0, 1, 2, -1, -4]
	print(threeSum1(nums))

