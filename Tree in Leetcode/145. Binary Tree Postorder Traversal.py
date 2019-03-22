# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 12:30
# @Author  : Lvpengfei


def postorderTraversal(root):
	if not root: return []
	ret = []
	stack = [root]

	while stack:
		node = stack.pop()
		ret.append(node.val)

		if node.left:
			stack.append(node.left)
		if node.right:
			stack.append(node.right)
	return ret[::-1]

