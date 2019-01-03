# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 15:18
# @Author  : Lvpengfei

"""
不含重复元素
"""

def subsets1(nums):
	def backtracking(start, nums, temp, ret):
		ret.append(temp)  # 因为是求所有子集，不需要判断
		for i in range(start, len(nums)):  # 递归停止条件由 start控制，当 start==len(nums)时，退出
			backtracking(i+1, nums, temp+[nums[i]], ret)

	ret = []
	backtracking(0, nums, [], ret)
	return ret

"""
迭代法：
	初始化：ret = [[]]
	第一步：将 1 加到所有子集中，ret = [[],[1]]
	第二步：将 2 加到所有子集中，ret = [[],[1],[2],[1,2]]
	第三步：将 3 加到所有子集中，ret = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""
def subsets2(nums):
	ret = [[]]
	for n in nums:
		ret += [s+[n] for s in ret]
	return ret

"""
位操作：bit-manipulation
"""
def subsets3(nums):
	ret = []
	for i in range(1<<len(nums)):  # pow(2, len(nums))
		temp = []
		for j in range(len(nums)):
			if i & 1 << j:
				temp.append(nums[j])
		ret.append(temp)
	return ret

if __name__ == '__main__':
	nums = [1, 2, 3]
	print(subsets1(nums))
	print(subsets2(nums))
	print(subsets3(nums))
	"""
	[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
	[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
	[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
	"""



