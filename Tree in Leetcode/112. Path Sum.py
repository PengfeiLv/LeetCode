# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 10:59
# @Author  : Lvpengfei


def hasPathSum(root, sum):
	if not root: return False
	if not root.left and not root.right and root.val == sum:
		return True
	return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)