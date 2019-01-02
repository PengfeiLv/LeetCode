# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 12:56
# @Author  : Lvpengfei

"""


"""

def threeSumClosest(nums, target):
	nums.sort()
	ret = float('inf')
	for i in range(len(nums)):
		if i>0 and nums[i]==nums[i-1]: continue
		l, r = i + 1, len(nums)-1
		while l<r:
			csum = nums[i]+nums[l]+nums[r]
			if csum == target: return target
			if abs(csum-target)<abs(ret-target):
				ret = csum
			if csum-target>0: r -= 1
			else: l += 1
	return ret


if __name__ == '__main__':
	nums = [1, 1, 1, 0]
	target = 100
	print(threeSumClosest(nums, target))

