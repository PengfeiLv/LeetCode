# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 14:48
# @Author  : Lvpengfei


"""
Boyer-Moore Majority Vote algorithm generalization
Time: O(N)  Space: O(1)
"""
def majorityElement(nums):
	if not nums:
		return []
	count1, count2, candidate1, candidate2 = 0, 0, 0, 1  # 两个候选，应该初始化为不同的数

	for i in nums:
		if i == candidate1:
			count1 += 1
		elif i == candidate2:
			count2 += 1
		elif count1 == 0:
			candidate1, count1 = i, 1
		elif count2 == 0:
			candidate2, count2 = i, 1
		else:
			count1 -= 1
			count2 -= 1
	res = []
	if nums.count(candidate1) > len(nums) // 3:
		res.append(candidate1)
	if nums.count(candidate2) > len(nums) // 3:
		res.append(candidate2)
	return res


if __name__ == '__main__':
	nums = [2,2]
	print(majorityElement(nums))