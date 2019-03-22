# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 10:47
# @Author  : Lvpengfei


def buildBST(nums):
	if not nums: return None
	mid = len(nums)//2
	root = TreeNode(nums[mid])
	root.left = buildBST(nums[:mid])
	root.right = buildBST(nums[mid+1:])
	return root
