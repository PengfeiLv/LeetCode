# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 12:36
# @Author  : Lvpengfei


def invertTree(root):
	if root:
		root.left, root.right = root.right, root.left
		invertTree(root.left)
		invertTree(root.right)
	return root
