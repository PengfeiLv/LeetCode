# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 14:03
# @Author  : Lvpengfei

# Time: O(N) + Space: O(1) ----> hash with index
def findDisappearedNumbers(nums):
	ret = []
	nums.append(0)
	for i in range(len(nums)):
		while nums[i] != i and nums[nums[i]] != nums[i]:
			nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
	for i in range(len(nums)):
		if nums[i] != i:
			ret.append(i)
	return ret


if __name__ == "__main__":
	nums = [4,3,2,7,8,2,3,1]
	print(findDisappearedNumbers(nums))