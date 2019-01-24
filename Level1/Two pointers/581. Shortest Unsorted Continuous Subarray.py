# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 11:38
# @Author  : Lvpengfei


# 排序：Time: O(NlogN)
def findUnsortedSubarray1(nums):
	snums = sorted(nums)
	start, end = 0, 0
	for i in range(len(nums)):
		if nums[i] != snums[i]:
			start = i
			break
	for i in range(len(nums)-1, -1, -1):
		if nums[i] != snums[i]:
			end = i
			break
	return 0 if start==end else end-start+1


# two-pointer: Time: O(N)
def findUnsortedSubarray2(nums):
	flag, n = False, len(nums)
	mini, maxi = float('inf'), -float('inf')
	for i in range(1, n):
		if nums[i] < nums[i-1]:
			flag = True
		if flag:
			mini = min(mini, nums[i])
	flag = False
	for i in range(n-2, -1, -1):
		if nums[i] > nums[i+1]:
			flag = True
		if flag:
			maxi = max(maxi, nums[i])
	left, right = 0, 0
	for i in range(n):
		if nums[i] >= mini:
			left = i
			break
	for i in range(n-1, -1, -1):
		if nums[i] <= maxi:
			right = i
			break
	return 0 if left==right else right-left+1


def findUnsortedSubarray3(nums):
	stack, n = [], len(nums)
	left, right =  n, 0
	for i in range(n):
		while stack and nums[stack[-1]]>nums[i]:
			left = min(stack.pop(), left)
		stack.append(i)
	for i in range(n-1, -1, -1):
		while stack and nums[stack[-1]]<nums[i]:
			right = max(stack.pop(), right)
		stack.append(i)
	return right-left+1 if right>left else 0



if __name__ == '__main__':
	nums = [1, 2, 5, 4, 3, 7, 6, 8]
	print(findUnsortedSubarray1(nums))
	print(findUnsortedSubarray2(nums))
	print(findUnsortedSubarray3(nums))