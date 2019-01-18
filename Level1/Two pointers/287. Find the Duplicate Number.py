# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 10:10
# @Author  : Lvpengfei

# 方法一：two-pointer
def findDuplicate1(nums):
	fast = nums[nums[nums[0]]]  # .next.next  fast走两步
	slow = nums[nums[0]]        # .next       slow走一步
	while fast != slow:
		fast = nums[nums[fast]]
		slow = nums[slow]

	fast = nums[0]  # 这里和链表不一样，只重置fast，slow不用动
	while fast != slow:
		fast = nums[fast]
		slow = nums[slow]
	return fast

# 方法二：hash + index
def findDuplicate2(nums):
	for i in range(len(nums)):
		loc = nums[i]
		while loc != i+1:
			if nums[loc-1] != loc:
				nums[loc-1], nums[i] = nums[i], nums[loc-1]
				loc = nums[i]
			else:
				return loc


if __name__ == '__main__':
	nums= [1, 3, 2, 4, 1]
	print(findDuplicate2(nums))