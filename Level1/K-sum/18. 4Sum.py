# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:08
# @Author  : Lvpengfei


"""
从nums中找到所有无重复的 a+b+c+d=target 的组合
"""

def ksum(nums, target, k, res, ret):
	if len(nums)<k or k<2 or nums[0]*k>target or nums[-1]*k<target: return  # 早停止，提高速度
	if k==2:
		l, r = 0, len(nums)-1
		while l<r:
			csum = nums[l] + nums[r]
			if csum==target:
				ret.append(res+[nums[l], nums[r]])
				l += 1
				while l<r and nums[l]==nums[l-1]:  # 控制去重
					l += 1
			elif csum<target:
				l += 1
			else:
				r -= 1
		return
	else:
		for i in range(len(nums)-k+1):
			if i==0 or nums[i]!=nums[i-1]:  # 控制去重
				ksum(nums[i+1:], target-nums[i], k-1, res+[nums[i]], ret)


def fourSum(nums, target):
	nums.sort()
	ret = []
	ksum(nums, target, 4, [], ret)
	return ret


if __name__ == '__main__':
	nums = [-3,-2,-1,0,0,1,2,3]
	target = 0
	print(fourSum(nums, target))