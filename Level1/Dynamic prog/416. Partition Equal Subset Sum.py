# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 17:01
# @Author  : Lvpengfei


def canPartition(nums):
	total = sum(nums)
	if total % 2 != 0: return False
	target = int(total // 2)
	had = {0}  # 不包含任何元素时，和为0
	for n in nums:
		sum_with_n = []
		for i in had:
			if i+n == target: return True
			if i+n < target:
				sum_with_n.append(i+n)  # 到目前为止包含 n 的子集的和
		had.update(sum_with_n)  # 并集
	return False


if __name__ == '__main__':
	nums = [1, 5, 5, 11]
	print(canPartition(nums))
