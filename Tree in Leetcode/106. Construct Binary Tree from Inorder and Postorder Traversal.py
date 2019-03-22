# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 10:42
# @Author  : Lvpengfei


def buildTree(inorder, postorder):
	if not inorder: return

	v = postorder.pop()
	node = TreeNode(v)

	idx = postorder.index(v)
	node.right = buildTree(inorder[v+1:], postorder)  # 先构建右子树
	node.left = buildTree(inorder[:v], postorder)  # 再左
	return node