# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 11:11
# @Author  : Lvpengfei


def flatten(root):
	def flat(root, pre):
		if not root: return pre
		pre = flat(root.right, pre)
		pre = flat(root.left, pre)
		root.right = pre
		root.left = None
		pre = root
		return pre

	flat(root, None)