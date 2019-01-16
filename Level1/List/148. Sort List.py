# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 10:22
# @Author  : Lvpengfei


# Time: O(NlogN)  Space: O(1)
# 既然要求O(NlogN)的时间和常量空间，只能用归并思想
def sortList(head):
	def mergeList(head1, head2):
		dummy = head = ListNode(0)
		while head1 and head2:
			if head1.val<head2.val:
				head.next = head1
				head1 = head1.next
			else:
				head.next = head2
				head2 = head2.next
			head = head.next
		head.next = head1 if head1 else head2
		return dummy.next  # 注意返回 .next

	if not head or not head.next:  # base case
		return head

	prev, fast, slow = None, head, head
	while fast and fast.next:  # 找到中点
		prev, fast, slow = slow, fast.next.next, slow.next
	prev.next = None   # 断开
	left = sortList(head)  # 递归对左半边排序
	right = sortList(slow)  # 递归对右半边排序
	return mergeList(left, right)  # 合并