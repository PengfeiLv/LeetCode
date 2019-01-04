# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 16:06
# @Author  : Lvpengfei


def maxArea(height):
	left, right = 0, len(height) - 1
	ret = 0
	while left < right:
		area = min(height[left], height[right]) * (right - left)
		ret = max(ret, area)
		if height[left] < height[right]:  # 面积由短边决定，哪边小，哪边移动更新
			left += 1
		else:
			right -= 1
	return ret

if __name__ == '__main__':
	nums = [1,8,6,2,5,4,8,3,7]
	print(maxArea(nums))