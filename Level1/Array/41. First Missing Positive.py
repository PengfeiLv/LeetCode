# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 16:52
# @Author  : Lvpengfei

"""
数组+索引

当遇到数组题目，且要求O(N)时间和O(1)空间时，
很大可能是需要将 索引作为 HashTable的键，利用 索引与值 的映射关系来求解

nums.append(0)
for i in range(len(nums)):
    while nums[i]>=0 and nums[i]<len(nums) and nums[nums[i]]!=nums[i]:
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
for i in range(len(nums)):
    if nums[i]!=i:
        return i
return len(nums)
"""

def firstMissingPositive(nums):
	nums.append(0)
	for i in range(len(nums)):
		loc = nums[i]
		while loc>=0 and loc<len(nums) and nums[loc]!=loc:
			nums[loc], loc = loc, nums[loc]  # 注意这里是将nums[loc]与loc交换，而不是与nums[i]交换
	for i in range(len(nums)):
		if nums[i]!=i:
			return i
	return len(nums)

if __name__ == '__main__':
	nums = [3,4,-1,1]
	print(firstMissingPositive(nums))


