# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 12:47
# @Author  : Lvpengfei


def lowestCommonAncestor(root, p, q):
	while root:
		if root.val<p.val and root.val<q.val:
			root = root.right
		elif root.val>p.val and root.val>q.val:
			root = root.left
		else:
			return root