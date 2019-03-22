# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 10:16
# @Author  : Lvpengfei


def inorder(root):
	if not root: return []
	stack = []
	ret = []

	while stack or root:
		while root:
			stack.append(root)   #
			root = root.left  # 找到当前root的最左结点

		node = stack.pop()
		ret.append(node.val)
		root = node.right
	return ret