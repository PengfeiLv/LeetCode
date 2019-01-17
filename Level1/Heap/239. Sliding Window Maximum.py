# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 15:12
# @Author  : Lvpengfei

from collections import deque


def maxSlidingWindow(nums, k):
	ret, que = [], deque()
	for i in range(len(nums)):
		while que and nums[i]>nums[que[-1]]:
			que.pop()
		que.append(i)
		while i-que[0]>=k:
			que.popleft()
		if i+1>=k:
			ret.append(nums[que[0]])
	return ret


if __name__ == '__main__':
	nums = [1,3,-1,-3,5,3,6,7]
	k = 3
	print(maxSlidingWindow(nums, k))