# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 10:29
# @Author  : Lvpengfei


def symmetricTree(root):
	def isMirror(left_root, right_root):
		if not left_root and not right_root: return True
		if not left_root or not right_root: return False
		return left_root.val == right_root.val \
		       and isMirror(left_root.left, right_root.right) \
		       and isMirror(left_root.right, right_root.left)