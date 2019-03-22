# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 13:58
# @Author  : Lvpengfei


def lowestCommonAncestor(root, p, q):
	self.ret = None
	def recursion(node):
		if not node: return False
		left = recursion(node.left)
		right = recursion(node.right)
		mid = node==p or node==q
		if left+right+mid>1:
			self.ret = node
		return left or right or mid
	recursion(root)
	return self.ret
