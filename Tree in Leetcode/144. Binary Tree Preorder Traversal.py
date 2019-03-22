# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 12:24
# @Author  : Lvpengfei


def preorderTraversal(root):
	if not root: return []
	ret = []
	stack = [root]

	while stack:
		node = stack.pop()
		ret.append(node.val)

		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)
	return ret

