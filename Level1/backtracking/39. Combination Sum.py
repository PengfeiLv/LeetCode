# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 16:05
# @Author  : Lvpengfei

"""
这里用到的是回溯法 backtracking：
	更明显的写法是
	if target<0:
		return
	elif target==0:
		ret.append(temp[:])  # 注意这里要写成 temp[:] 而不能是 temp，temp[:]相当于将值传进来，temp 传的是引用
		return
	else:
		for i in range(start, len(candidates)):
			temp.append(candidates[i])
			helper(i, target-candidates[i], temp, ret)
			temp.pop()  # 回溯，恢复到上一步时的状态

"""


def helper(start, target, temp, ret):
	if target<0:
		return
	elif target==0:
		ret.append(temp)
		return
	else:
		for i in range(start, len(candidates)):
			helper(i, target-candidates[i], temp+[candidates[i]], ret)


def combinationSum(candidates, target):
	candidates.sort()
	ret = []
	helper(0, target, [], ret)
	return ret


if __name__ == '__main__':
	candidates = [2, 3, 6, 7]
	target = 8
	print(combinationSum(candidates, target))
	pass