# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 14:23
# @Author  : Lvpengfei


def diameterOfBinaryTree(root):
	def recursion(node):
		if not node: return 0
		L = recursion(node.left)
		R = recursion(node.right)
		dm = max(dm, L+R)
		return max(L, R)+1

	dm = 0
	recursion(root)
	return dm