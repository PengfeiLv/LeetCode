# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 10:36
# @Author  : Lvpengfei


def buildTree(preorder, inorder):
	if not inorder: return  # 注意这里只能是inorder，不能是preorder

	v = preorder.pop(0)
	node = TreeNode(v)

	idx = inorder.index(v)
	node.left = buildTree(preorder, inorder[:v])
	node.right = buildTree(preorder, inorder[v+1:])
	return node