# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 16:25
# @Author  : Lvpengfei

"""
带重复元素
"""
def subsetsWithDup1(nums):
	def backtracking(start, temp, ret):
		ret.append(temp)
		for i in range(start, len(nums)):
			if i>start and nums[i]==nums[i-1]:  # 控制去重
				continue
			backtracking(i+1, temp+[nums[i]], ret)
	ret = []
	nums.sort()
	backtracking(0, [], ret)
	return ret

# 迭代法
def subsetsWithDup2(nums):
	ret, temp = [[]], []
	nums.sort()
	for i in range(len(nums)):
		if i>0 and nums[i]==nums[i-1]:  # 当遇到重复数据时，仅能加到temp中，不能算作新的一轮
			temp = [s+[nums[i]] for s in temp]
		else:
			temp = [s+[nums[i]] for s in ret]
		ret += temp
	return ret

if __name__ == '__main__':
	nums = [4,4,4,1,4]
	print(subsetsWithDup1(nums))
	print(subsetsWithDup2(nums))
