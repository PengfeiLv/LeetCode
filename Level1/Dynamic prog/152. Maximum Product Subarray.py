# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 10:53
# @Author  : Lvpengfei


def maxProduct(nums):
	if not nums: return 0
	ret, cmax, cmin = nums[0], nums[0], nums[0]
	for n in nums[1:]:
		if n<0:
			cmax, cmin = cmin, cmax
		cmax = max(n, n*cmax)
		cmin = min(n, n*cmin)
		ret = max(ret, cmax)
	return ret


if __name__ == '__main__':
	nums = [-1,-2,-9,-6]
	print(maxProduct(nums))
