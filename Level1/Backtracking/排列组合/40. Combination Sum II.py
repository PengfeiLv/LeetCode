# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 16:46
# @Author  : Lvpengfei


"""


"""

def helper(start, target, temp, ret):
	if target<0:
		return
	elif target==0:
		if temp not in ret:  # 控制去重
			ret.append(temp)
		return
	else:
		for i in range(start, len(candidates)):
			helper(i+1, target-candidates[i], temp+[candidates[i]], ret)
			# i+1 控制每个元素用一次


def combinationSum2(candidates, target):
	candidates.sort()
	ret = []
	helper(0, target, [], ret)
	return ret


if __name__ == '__main__':
	candidates = [10,1,2,7,6,1,5]
	target = 8
	print(combinationSum2(candidates, target))
	pass