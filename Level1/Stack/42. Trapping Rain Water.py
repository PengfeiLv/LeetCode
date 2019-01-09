# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 17:52
# @Author  : Lvpengfei

def trap(height):
	ret = 0
	stack = [0]
	for i in range(1, len(height)):
		if stack and height[stack[-1]]>height[i]:

			ret += height[i]*(i-height[stack.pop()])
		stack.append(i)
	return ret


if __name__ == "__main__":
	nums = [0,1,0,2,1,0,1,3,2,1,2,1]
	print(trap(nums))
